"""Defines the methods of manage workloads and jobs for ray compute frameworks."""
import click
from typing import AsyncGenerator, Union
import requests
import ray
from ray.job_submission import JobSubmissionClient
from ray.job_submission import JobStatus as RayJobStatus
from ray.job_submission import JobDetails as RayJobDetails
from opus import opus_logging
from opus.frameworks.frameworks import Framework, FrameworkStatus
from opus.utils import common_utils
from opus.jobs import JobStatus, JobInfo, Job
from opus.common_types import RayLaunchParams, JobConfig

logger = opus_logging.init_logger(__name__)

job_status_map = {
    RayJobStatus.PENDING: JobStatus.PENDING,
    RayJobStatus.RUNNING: JobStatus.RUNNING,
    RayJobStatus.SUCCEEDED: JobStatus.SUCCEEDED,
    RayJobStatus.FAILED: JobStatus.FAILED,
    RayJobStatus.STOPPED: JobStatus.STOPPED,
}

DefaultDashboardPort = 8265
DefaultDashboardAgentListenPort = 52365
RayDashboardGCSHealthPath = "api/gcs_healthz"
RayAgentRayletHealthPath = "api/local_raylet_healthz"

class RayFramework(Framework):
    """Ray Compute Framework."""
    def __init__(self, dashboard_port: int = None, agent_listen_port: int = None, **kwargs):
        super().__init__(**kwargs)
        if hasattr(self.cloud, "ray_head_port_forward") \
            and self.cloud_job_info.job_id \
            and self.cloud.is_ray_ready(self.cloud_job_info):
            dashboard_port = self.cloud.ray_head_port_forward(self.cloud_job_info, DefaultDashboardPort)
            agent_listen_port = self.cloud.ray_head_port_forward(self.cloud_job_info, DefaultDashboardAgentListenPort)
        self.dashboard_port = dashboard_port
        self.agent_listen_port = agent_listen_port

    @property
    def job_client(self) -> 'JobSubmissionClient':
        ray_status = self.get_status()
        if ray_status != FrameworkStatus.UP.value:
            raise ConnectionError(f'Framework `{self.framework_id}` is not UP.')
        return JobSubmissionClient(address = f'http://{self.head_external_ip}:{self.dashboard_port or DefaultDashboardPort}')

    def launch(self) -> None:
        """Launch Ray Framework."""
        rayLaunchParams = RayLaunchParams(
            framework_id = self.framework_id,
            name = self.name,
            group = self.cloud_job_info.group,
            setupCommand = self.setupCommand,
            envs = self.envs, 
            workerNum = self.workerNum,
            headCpu = self.headCpu, 
            headMem = self.headMem, 
            headAccelerator = self.headAccelerator, 
            headLogicCpu = self.headStartParams.get('numsCpus'),
            headLogicGpu = self.headStartParams.get('numsGpus'),
            headCustomResource = self.headStartParams.get('customResources'),
            workerCpu = self.workerCpu,
            workerMem = self.workerMem,
            workerAccelerator = self.workerAccelerator,
            workerLogicCpu = self.workerStartParams.get('numsCpus'),
            workerLogicGpu = self.workerStartParams.get('numsGpus'),
            workerCustomResource = self.workerStartParams.get('customResources'),
            workdir=self.workdir
        )
        self.cloud_job_info = self.cloud.launch_ray(rayLaunchParams)
        self._update_db()
        click.secho("The framework has been launched, "
                    "you can check the status of the framework with the Framework ID {}"
                    .format(self.framework_id), fg='yellow', nl=True)
    
    def stop(self) -> None:
        """Stop Ray Framework."""
        if self.status in FrameworkStatus.unstopped():
            Job.terminate_jobs_before_framework_stop(self.framework_id)
            self.cloud.stop_ray(self.cloud_job_info)
            self.head_external_ip = None
            self.status = FrameworkStatus.STOPPED.value
            self._update_db()
        else:
            raise Exception(f"Framework was {self.status}, should not stop it again.")

    def _connect(self) -> None:
        if not ray.is_initialized():
            ray.init(address=f'ray://{self.head_external_ip}:10001')
        
    def is_healthy(self) -> bool:
        """Check GCS and Raylet status of the head node."""
        dashboard_port = self.dashboard_port or DefaultDashboardPort
        dashboard_agent_listen_port = self.agent_listen_port or DefaultDashboardAgentListenPort
        try:
            gcs_healthz_response = requests.get("http://{}:{}/{}".format(
                self.head_external_ip, dashboard_port, RayDashboardGCSHealthPath))
            raylet_healthz_response = requests.get("http://{}:{}/{}".format(
                self.head_external_ip, dashboard_agent_listen_port, RayAgentRayletHealthPath))
        except Exception as e:
            logger.error(f"Health check: Connection failed {e}")
            return False
        if gcs_healthz_response.content == b'success' and raylet_healthz_response.content == b'success':
            return True
        return False
    
    def get_status(self) -> str:  
        """Get the latest status."""
        if self.status == FrameworkStatus.STOPPED.value:  
            return self.status   
        if hasattr(self.cloud, "ray_head_port_forward"):
            self.head_external_ip = '127.0.0.1'
        else:
            self.head_external_ip = self.cloud.get_ray_head_ip(self.cloud_job_info)
        self._update_status()
        self._update_db()
        return self.status
    
    def _update_status(self):
        if self.head_external_ip:
            if self.is_healthy():
                self.status = FrameworkStatus.UP.value
            else:
                self.status = FrameworkStatus.UNKNOWN.value
        elif self.status != FrameworkStatus.INIT.value:
            self.status = FrameworkStatus.UNKNOWN.value

    def run_job(self, job_id: int, job: 'JobConfig', autostop: bool) -> str:
        """Run a job on RAY framework.
        
        Arg:
            - job_id: The unique ID of the job.
            - job: The JobConfig includes fields about its submission definition.
            - autostop: If True, stop the framework automatically once job finished.
        
        Return:
            The submission ID of the job on RAY.
        
        Raise:
            RuntimeError: Failed to request to the job server of RAY.
        """
        ray_sub_id = f'{job_id}_{job.jobname}'
        if autostop:
            job.run += f"; sleep 5; scancel {self.cloud_job_info.job_id}"
        self.job_client.submit_job(
            entrypoint = common_utils.format_shell_cmds(job.run),
            submission_id = ray_sub_id,
            runtime_env = {
                'working_dir': job.workdir,
            }
        )
        return ray_sub_id
    
    def get_job_info(self, ray_submission_id: str) -> 'JobInfo':
        """Get the job's info on RAY framework.
        
        Arg:
            - ray_submission_id: The unique ID of the job on RAY framework. 
        
        Return:
            `JobInfo` with three fields: `status`, `start_at`, `end_at`.
        """
        ray_job_info: RayJobDetails
        ray_job_info = self.job_client.get_job_info(ray_submission_id)
        return JobInfo(
            status = job_status_map[ray_job_info.status].value,
            start_at = ray_job_info.start_time,
            end_at = ray_job_info.end_time,
        )
    
    def stop_job(self, ray_submission_id: str) -> bool:
        """Stop the job on RAY framework.
        
        Arg:
            - ray_submission_id: The unique ID of the job on RAY framework.

        Return:
            True if the job was unfinished, otherwise False.
        """
        # NOTE: The `ray.job_submission.JobSubmissionClient.stop_job` API only stops
        # `RUNNING` jobs immediately now (~2023/11/10), not support `PENDING` jobs yet.
        # Issue Ref: https://github.com/ray-project/ray/issues/36858
        return self.job_client.stop_job(ray_submission_id)

    def get_job_logs(self, ray_submission_id: str, follow: bool) -> Union[AsyncGenerator, str]:
        """Get the logs of the job on RAY framework.
        
        Arg:
            - ray_submission_id: The unique ID of the job on RAY framework. 
            - follow: If true, tail the logs. Otherwise, get the logs so far.

        Return:
            Return a AsyncGenerator to tail the logs if `follow` is true
            else return a string.
        """
        if follow:
            return self.job_client.tail_job_logs(ray_submission_id)
        else:
            return self.job_client.get_job_logs(ray_submission_id)