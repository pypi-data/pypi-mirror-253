import os
import enum
import pathlib
import time
import colorama
from collections import namedtuple
from typing import Dict, Any, Optional, List, Tuple, AsyncGenerator, Union
from opus import opus_logging, frameworks
from opus.utils import db_utils, common_utils
from opus.common_types import JobConfig
from opus.frameworks import Framework
from opus.clouds import CloudProviders

logger = opus_logging.init_logger(__name__)

db_path = os.path.expanduser('~/.opus/opus.db')
os.makedirs(pathlib.Path(db_path).parents[0], exist_ok=True)
db = db_utils.SQLiteDB(db_path)
db.cursor.execute("""CREATE TABLE IF NOT EXISTS jobs (
                            job_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            job_name VARCHAR(256),
                            framework_id INTEGER,
                            framework_job_id VARCHAR(256),
                            submitted_at INTEGER,
                            status VARCHAR(16),
                            start_at INTEGER,
                            end_at INTEGER
                        )""")
db.conn.commit()

record_field_order = ('job_id', 
                      'job_name', 
                      'framework_id', 
                      'framework_job_id', 
                      'submitted_at', 
                      'status', 
                      'start_at', 
                      'end_at')

JobInfo = namedtuple('JobInfo', ['status', 'start_at', 'end_at'])


class JobStatus(enum.Enum):
    """Job status."""

    # INIT: The `job_id` has been generated, but the job program has not started yet.
    INIT = 'INIT'
    # PENDING: The job is waiting for the required resources.
    PENDING = 'PENDING'
    # RUNNING: The job is running.
    RUNNING = 'RUNNING'
    # SUCCEEDED: The job finished successfully.
    SUCCEEDED = 'SUCCEEDED'
    # FAILED: The job fails due to the user's code.
    FAILED = 'FAILED'
    # STOPPED: The job is stopped by the user.
    STOPPED = 'STOPPED'
    # TERMINATED: The job is terminated due to the framework is stopped or down.
    TERMINATED = 'TERMINATED'
    
    @classmethod
    def unfinished(cls) -> List[str]:
        return [cls.INIT.value, 
                cls.PENDING.value, 
                cls.RUNNING.value]
    
    def with_color(self) -> str:
        return f'{job_status_color_map[self]}{self.value}{colorama.Style.RESET_ALL}'


job_status_color_map = {
    JobStatus.INIT: colorama.Fore.CYAN,
    JobStatus.PENDING: colorama.Fore.CYAN,
    JobStatus.RUNNING: colorama.Fore.GREEN,
    JobStatus.SUCCEEDED: colorama.Fore.GREEN,
    JobStatus.FAILED: colorama.Fore.RED,
    JobStatus.STOPPED: colorama.Fore.YELLOW,
    JobStatus.TERMINATED: colorama.Fore.MAGENTA,
}


class Job:
    """Job: managed by the compute framework(e.g. Ray, MPI) to be run on the cloud."""

    def __init__(self, job_id: int) -> None:
        """Initialize a Job object by the given job id.
        
        Properties:
            - job_id: The unique ID of the job.
            - job_name: The display name of the job.
            - framework_id: The unique ID of the framework that the job submitted to.
            - framework: The object of the framework that the job submitted to.
            - framework_job_id: The unique ID used to map the job to the framework job.
            - submitted_at: The submitted timestamp of the job.
            - status: The status of the job.
            - start_at: The start timestamp of the job.
            - end_at: The end timestamp of the job.
        """
        self.job_id = job_id
        record = self._get_records([[('job_id', job_id)]])[0]
        self.job_name = record['job_name']
        self.framework_id = record['framework_id']
        framework_record = Framework.get_frameworks([[('id', self.framework_id)]])[0]
        framework = frameworks.FrameworkType[framework_record['framework_type'].upper()].value
        self.framework = framework.create_from_record(framework_record)
        self.framework_job_id = record['framework_job_id']
        self.submitted_at = record['submitted_at']
        self.status = record['status']
        self.start_at = record['start_at']
        self.end_at = record['end_at']
    
    @staticmethod
    def _save(job_name: Optional[str], framework_id: int) -> int:
        """Save the submitted job's info into jobs table.

        Return: 
            The job ID.
        """
        submitted_at = int(round(time.time() * 1000))
        db.cursor.execute('INSERT INTO jobs (job_name, framework_id, submitted_at, status) '
                          'VALUES (?, ?, ?, ?)',
                          (job_name, framework_id, submitted_at, JobStatus.INIT.value))
        db.conn.commit()
        return db.cursor.lastrowid
    
    def _update(self) -> None:
        """Update the job's info in the jobs table."""
        db.cursor.execute('UPDATE jobs SET '
                          'framework_job_id=(?), '
                          'status=(?), '
                          'start_at=(?), '
                          'end_at=(?) '
                          'WHERE job_id=(?)',
                          (self.framework_job_id,
                           self.status,
                           self.start_at,
                           self.end_at,
                           self.job_id))
        db.conn.commit()
    
    @staticmethod
    def _get_records(filter_options: List[List[Tuple[str, Any]]] = []) -> List[Dict[str, Any]]:
        """Get the records from the jobs table.
        
        Arg:
            - filter_options: The conditions to filter the records. It should be formatted like: 
                [
                    [('status', 'RUNNING'), ('status', 'PENDING')], 
                    [('framework_id', '1'), ('framework_id', '2')]
                ]
        
        Return:
            The list of records. Each record is a dict.
        """
        if len(filter_options) > 0:
            conditions = [' OR '.join([f"{o[0]}='{o[1]}'" for o in option]) 
                          for option in filter_options]
            conditions = ' AND '.join([f'({c})' for c in conditions])
            db.cursor.execute(f"SELECT {','.join(record_field_order)} FROM jobs "
                              f"WHERE {conditions} ORDER BY job_id DESC")
        else:
            db.cursor.execute(f"SELECT {','.join(record_field_order)} FROM jobs "
                              "ORDER BY job_id DESC")
        rows = db.cursor.fetchall()
        return [
            {
                record_field_order[i] : row[i] for i in range(len(record_field_order))
            } for row in rows
        ]
    
    @staticmethod
    def get_all_job_ids() -> List[int]:
        rows = db.cursor.execute('SELECT job_id FROM jobs')
        return [row[0] for row in rows.fetchall()]
    
    @staticmethod
    def delete(job_ids: Tuple[int]) -> None:
        if not job_ids:
            return
        sql = "DELETE FROM jobs WHERE job_id IN ({})".format(','.join([str(job_id) for job_id in job_ids]))
        db.cursor.execute(sql)
        db.conn.commit()
    
    @classmethod
    def run(cls, config: 'JobConfig', framework_id: int, autostop: bool) -> Tuple[int, Optional[RuntimeError]]:
        """Run the job on the framework.
        
        Args:
            - config: The config of the job about its submission definition.
            - framework_id: The target framework id.
            - autostop: If True, stop the framework automatically once job finished.
        
        Return:
            A tuple of the registered job id and the optional RuntimeError.
        """
        if not Framework.exists(framework_id):
            raise ValueError(f'Framework `{framework_id}` do not exist.')
        job_id = cls._save(
            job_name = config.jobname,
            framework_id = framework_id
        )
        job = cls(job_id)
        try:
            if config.upload is not None:
                remote_host = job.framework.cloud.login_node
                if job.framework.cloud_type == CloudProviders.SLURM.name.lower():
                    suser_list_cmd = 'suser list -u $(whoami)'
                    output = common_utils.execute_command(suser_list_cmd)
                    output_lines = output.split('\n')
                    partitions = output_lines[1].split()[1].split(',')
                    for destination, source in config.upload.items():
                        common_utils.rsync_through_slurm(
                            source = source,
                            destination = destination,
                            remote_host = remote_host,
                            partition = partitions[0],
                        )
            framework_job_id = job.framework.run_job(job_id, config, autostop)
        except Exception as e:
            job.status = JobStatus.FAILED.value
            job._update()
            return (job_id, RuntimeError(e))
        else:
            job.framework_job_id = framework_job_id
            job.status = JobStatus.PENDING.value
            job._update()
            return (job_id, None)
    
    @classmethod
    def list(cls, filter_options: List[List[Tuple[str, Any]]] = []) -> List[Dict[str, Any]]:
        """List the jobs by the given filter options."""
        unfinished_jobs = cls._get_records([[('status', s) for s in JobStatus.unfinished()]])
        for job in unfinished_jobs:
            job = cls(job['job_id'])
            if job.framework_job_id is None:
                continue
            try:
                job.sync_status()
            except Exception:
                # TODO(tianshihan): consider more fine-grained job status updating logic
                job.status = JobStatus.TERMINATED.value
                job.end_at = int(round(time.time() * 1000))
                job._update()
        return cls._get_records(filter_options)
    
    def stop(self) -> None:
        """Stop the current job."""
        self.framework.stop_job(self.framework_job_id)
        time.sleep(1)
        self.sync_status()
    
    def logs(self, follow: bool) -> Union[AsyncGenerator, str]:
        """Logs the current job.
        
        Arg:
            - follow: If true, tail the logs. Otherwise, get the logs so far.
        
        Return:
            Return a AsyncGenerator to tail the logs if `follow` is true
            else return a string.
        """
        return self.framework.get_job_logs(self.framework_job_id, follow)
    
    def sync_status(self) -> None:
        """Fetch and update the latest job status info."""
        self.status, self.start_at, self.end_at = self.framework.get_job_info(self.framework_job_id)
        self._update()

    @classmethod
    def terminate_jobs_before_framework_stop(cls, framework_id: int) -> None:
        """Terminate the unfinished jobs when a framework is stopping."""
        filter_options = [[('status', s) for s in JobStatus.unfinished()]]
        filter_options.append([('framework_id', framework_id)])
        unfinished_jobs_on_the_framework = cls._get_records(filter_options)
        for job in unfinished_jobs_on_the_framework:
            job = cls(job['job_id'])
            job_was_unfinished_before = job.framework.stop_job(job.framework_job_id)
            if job_was_unfinished_before:
                job.status = JobStatus.TERMINATED.value
                _, job.start_at, _ = job.framework.get_job_info(job.framework_job_id)
                job.end_at = int(round(time.time() * 1000))
            else:
                job.status, job.start_at, job.end_at = job.framework.get_job_info(job.framework_job_id)
            job._update()
