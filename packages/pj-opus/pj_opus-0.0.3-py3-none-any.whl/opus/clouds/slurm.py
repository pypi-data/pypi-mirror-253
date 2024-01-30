from opus.clouds import cloud
from opus import opus_logging
from opus.utils import common_utils
from opus.common_types import CloudJobInfo, RayLaunchParams, SlurmJobDetails
from typing import Tuple, Optional, List
import os
import time
import click
import sys
import json
import re

RAY_TEMPLATE = 'slurm-ray-template.sh.j2'
SBTCH_SCRIPT_PREFIX = '~/opus/slurm_ray_sbatch_script'
LOG_FILE_PREFIX = '~/opus/logs'

logger = opus_logging.init_logger(__name__)
class Slurm(cloud.Cloud):
    
    def get_resources_info(self) -> Tuple[bool, Optional[List[str]]]:
        sinfo_command = "sinfo -s"
        try:
            exec_output = common_utils.execute_command(sinfo_command, self.login_node)
            output_lines = exec_output.split('\n')
            # get node resources
            partition, nodes = output_lines[1].split()[0], output_lines[1].split()[3].split("/")
            current_nodes = f"{nodes[1]}/{nodes[3]}"
            return True, [self.name, self.cloud_type, partition, current_nodes]
        except Exception as e:
            logger.error(f"slurm is not available, tying call `sinfo` failed: {e}")
            return False, None
        
    def launch_ray(self, ray: RayLaunchParams) -> 'CloudJobInfo':
        """Launch ray compute framework."""
        log_file_path = os.path.join(os.path.expanduser(LOG_FILE_PREFIX),
                                     f'{ray.framework_id}-{ray.name}.log')
        os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
        script_path = os.path.join(os.path.expanduser(SBTCH_SCRIPT_PREFIX),
                                 f'{ray.framework_id}-{ray.name}.sh')
        
        headAcceleratorNum = ray.headAccelerator.split(":")[1] if ray.headAccelerator != None else '0'
        workerAcceleratorNum = ray.workerAccelerator.split(":")[1] if ray.workerAccelerator != None else '0'
        vars_to_fill = {
            'JOB_NAME': ray.name,
            'PARTITION_OPTION': ray.group,
            'SETUP_COMMAND': ray.setupCommand if ray.setupCommand != None else "",
            'LOAD_ENV': ray.envs if ray.envs != None else {},
            'OUT_PUT_PATH': log_file_path,
            'NUM_NODES': ray.workerNum + 1,
            'NUM_CPUS_OF_HEAD': ray.headCpu,
            'MEM_OF_HEAD': ray.headMem,
            'RAY_HEAD_NUM_CPUS': ray.headLogicCpu if ray.headLogicCpu != None else ray.headCpu,
            'RAY_HEAD_NUM_GPUS': ray.headLogicGpu if ray.headLogicGpu != None else headAcceleratorNum,
            'RAY_HEAD_CUSTOM_RESOURCES': f"'{json.dumps(ray.headCustomResource)}'" if ray.headCustomResource != None else '{}',
            'NUM_ACCELS_OF_HEAD': headAcceleratorNum,
            'NUM_CPUS_PER_WORKER': ray.workerCpu,
            'MEM_PER_WORKER': ray.workerMem,
            'NUM_ACCELS_PER_WORKER': workerAcceleratorNum,
            'RAY_WORKER_NUM_CPUS': ray.workerLogicCpu if ray.workerLogicCpu != None else ray.workerCpu,
            'RAY_WORKER_NUM_GPUS': ray.workerLogicGpu if ray.workerLogicGpu != None else workerAcceleratorNum,
            'RAY_WORKER_CUSTOM_RESOURCES': f"'{json.dumps(ray.workerCustomResource)}'" if ray.workerCustomResource != None else '{}'
        }

        common_utils.fill_template(RAY_TEMPLATE, 
                            vars_to_fill, 
                            output_path=script_path)

        click.secho("Ray framework Launching! Script file is at: <{}>. Log file is at: <{}>".format(script_path, log_file_path), 
            fg='yellow', nl=True)
        
        exclude_nodes = []
        retry_count = 0
        slurm_node_is_healthy = False
        try:
            while not slurm_node_is_healthy:
                job_id = self.launch_batch_job(script_path, exclude_nodes=exclude_nodes)
                
                while self.get_job_details(job_id).JobState == 'PENDING':
                    click.secho("Ray framework queuing for resources. You can wait until ray launched or using Ctrl+C to stop.", 
                                fg='yellow', nl=True)
                    time.sleep(10)

                click.secho("Slurm job is {}, waiting for node checking...".format(self.get_job_details(job_id).JobState), fg='yellow', nl=True)
                while self.get_job_details(job_id).JobState == 'RUNNING':
                    try:
                        check_result = common_utils.execute_command(f"cat {os.path.expanduser(log_file_path)} | grep 'The node healthy check finished'", 
                                                                self.login_node)
                        if check_result:
                            logger.info("Found target string.")
                            if re.search('ALL_HEALTH', check_result):
                                slurm_node_is_healthy = True
                            break
                        time.sleep(1)
                    except Exception:
                        logger.info(f"Waiting for slurm log reading...")
                        time.sleep(1)
                        continue
                
                if not slurm_node_is_healthy:
                    try:
                        exec_output = common_utils.execute_command(f"cat {os.path.expanduser(log_file_path)} | grep UNHEALTHY_NODES", 
                                                                    self.login_node)
                        exclude_nodes += exec_output.split(':')[1].split()
                    except Exception as e:
                        logger.info(f"Exclude nodes: {exclude_nodes}. The error is: {e}")
                    retry_count += 1
                    click.secho("Retring launch {}, Exclude nodes: {}".format(retry_count, exclude_nodes), fg='yellow', nl=True)
            return CloudJobInfo(group=ray.group, job_id=job_id)
        except KeyboardInterrupt:
            logger.info("KeyboardInterrupt received.")
            return CloudJobInfo(group=ray.group, job_id=job_id)
        except Exception:
            click.secho("Failed to launch framework on slurm {}".format(self.name), fg='red', nl=True)
            sys.exit(1)

    def get_ray_head_ip(self, cloud_job_info: CloudJobInfo) -> str:
        """Retrieve Head IP of ray that running on the cloud."""
        return self.get_job_details(cloud_job_info.job_id).BatchHostIP
    
    def stop_ray(self, cloud_job_info: CloudJobInfo) -> None:
        """Stop ray Framework."""
        self.stop_job(cloud_job_info.job_id)

    def launch_batch_job(self, batch_script_path: str, exclude_nodes: List = None) -> str:
        """Submit slurm batch job.
        """
        logger.info("Starting to submit job!")
        try:
            # TOOD: Using string command instead of tmp file.
            # Sync file to remote node then delete
            if self.login_node:
                common_utils.execute_command(f'mkdir -p {os.path.expanduser(SBTCH_SCRIPT_PREFIX)} {os.path.expanduser(LOG_FILE_PREFIX)}', 
                                             self.login_node)
                common_utils.rsync(batch_script_path, 
                                   os.path.expanduser(SBTCH_SCRIPT_PREFIX)+'/', 
                                   self.login_node)
                batch_script_path = os.path.expanduser(SBTCH_SCRIPT_PREFIX)+'/'+os.path.basename(batch_script_path)
            sbatch_command = 'sbatch --exclude={} {}'.format('' if exclude_nodes is None else ",".join(exclude_nodes), batch_script_path)
            exec_output = common_utils.execute_command(sbatch_command, self.login_node)
            job_id = exec_output.split(" ")[3].strip()
            logger.info("slurm batch job id is: {}".format(job_id))
            return job_id
        except KeyboardInterrupt:
            logger.info("KeyboardInterrupt received.")
            raise e
        except Exception as e:
            logger.error(f"Failed to submit slurm batch job: {e}")
            raise e
    
    @staticmethod
    def launch_srun_job(command: str, partition: str, cpus_per_task: int, nodes_num: int, options: str="") -> None:
        """Launch an SRUN job with the specified options.
        """
        srun_command = f"srun {options} -p {partition} -N {nodes_num} --cpus-per-task {cpus_per_task} {command}"
        try:
            common_utils.execute_command(srun_command)
        except Exception as e:
            logger.error(f"Failed to execute srun: {e}")

    def get_job_details(self, job_id: str) -> 'SlurmJobDetails':
        """Retrieve information about the job running on the slurm."""
        job_details = SlurmJobDetails(JobState="", BatchHostIP="")
        if job_id == "":
            return job_details
        scontrol_command = f"scontrol show job {job_id}"
        try:
            exec_output = common_utils.execute_command(scontrol_command, self.login_node)
            if not exec_output:
                raise Exception
        except:
            logger.info("The slurm job {} does not exist!".format(job_id))
            return job_details
        job_state = common_utils.execute_command("grep JobState", input=exec_output.encode('utf-8'))
        job_state = job_state.split()[0].split("=")[1]
        job_details.JobState = job_state
        if job_state == 'RUNNING':
            head_node_hostname = common_utils.execute_command("grep BatchHost", input=exec_output.encode('utf-8'))
            head_node_hostname = head_node_hostname.split()[0].split("=")[1]
            try:
                job_details.BatchHostIP = common_utils.execute_command(
                    f"python -c \"import socket; print(socket.gethostbyname('{head_node_hostname}'))\"", self.login_node).strip()
            except:
                logger.info("Host not found")
        return job_details
    
    def stop_job(self, job_id: str) -> None:
        """Stop job on slurm."""
        scancel_command = f"scancel {job_id}"
        try:
            common_utils.execute_command(scancel_command, self.login_node)
            logger.info(f"Successfully stopped slurm job {job_id}")
        except Exception as e:
            logger.warn(f"Failed to stop slurm job {job_id}: {e}")
            raise Exception(f"Failed to stop slurm job {job_id}: {e}")