from opus.clouds import cloud
from typing import Tuple, Optional, List, Type
from opus import opus_logging
from opus.common_types import CloudJobInfo, RayLaunchParams, RayClusterDetails
from opus.utils import common_utils
from kubernetes import config, dynamic, client
from kubernetes.dynamic.exceptions import ResourceNotFoundError
import os
import click
import json
import yaml
import urllib3
import portforward

RAY_TEMPLATE = 'kubernetes-ray-template.yaml.j2'
# Store the YAML file defined by each generated Ray cluster.
RAY_CLUSTER_YAML_PREFIX = '~/opus/kubernetes_ray_cluster_yaml'
# TODO: replace image
RAY_IMAGE = 'redpanda123321/pj-ray-llm:2.3.1-py310-cu118'

logger = opus_logging.init_logger(__name__)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class Kubernetes(cloud.Cloud):
    """Kubernetes cluster."""
    def get_client(self) -> Type[client.ApiClient]:
        """Get k8s client"""
        config.load_kube_config(self.auth_config)
        return client.ApiClient()
    
    def get_core_v1_api(self):
        """Get CoreV1 api"""
        config.load_kube_config(self.auth_config)
        return client.CoreV1Api()

    def get_raycluster_client(self):
        """Get raycluster api"""
        k8s_client = self.get_client()
        try:
            raycluster_api = dynamic.DynamicClient(k8s_client).resources.get(
                api_version="ray.io/v1alpha1", kind="RayCluster"
            )
        except ResourceNotFoundError:
            click.secho("RayCluster CRD not found, KubeRay should be installed first.")
        return raycluster_api

    def get_resources_info(self) -> Tuple[bool, Optional[List[str]]]:
        """Get user group and resources."""
        return True, [self.name, self.cloud_type, self.group or "*", "*"]
    
    def launch_ray(self, ray: RayLaunchParams) -> 'CloudJobInfo':
        """Launch ray compute framework."""
        yaml_path = os.path.join(os.path.expanduser(RAY_CLUSTER_YAML_PREFIX),
                            f'{ray.framework_id}-{ray.name}.yaml')
        
        setup_command = [common_utils.format_shell_cmds(ray.setupCommand) if ray.setupCommand else '']
        headAcceleratorNum = ray.headAccelerator.split(":")[1] if ray.headAccelerator and ":" in ray.headAccelerator else '0'
        workerAcceleratorNum = ray.workerAccelerator.split(":")[1] if ray.workerAccelerator and ":" in ray.workerAccelerator else '0'
        vars_to_fill = {
            'RAY_CLUSTER_NAME': f'{ray.name}-{ray.framework_id}',
            'NAMESPACE': ray.group,
            'SETUP_COMMAND': setup_command,
            'LOAD_ENV': ray.envs if ray.envs != None else {},
            'NUM_WORKER_NODES': ray.workerNum,
            'IMAGE': RAY_IMAGE,
            'NUM_CPUS_OF_HEAD': ray.headCpu,
            'MEM_OF_HEAD': ray.headMem,
            'NUM_ACCELS_OF_HEAD': headAcceleratorNum,
            'RAY_HEAD_NUM_CPUS': ray.headLogicCpu if ray.headLogicCpu != None else ray.headCpu,
            'RAY_HEAD_NUM_GPUS': ray.headLogicGpu if ray.headLogicGpu != None else headAcceleratorNum,
            'RAY_HEAD_CUSTOM_RESOURCES': json.dumps(ray.headCustomResource).replace('"', '\\"') if ray.headCustomResource != None else '{}',
            'NUM_CPUS_PER_WORKER': ray.workerCpu,
            'MEM_PER_WORKER': ray.workerMem,
            'NUM_ACCELS_PER_WORKER': workerAcceleratorNum,
            'RAY_WORKER_NUM_CPUS': ray.workerLogicCpu if ray.workerLogicCpu != None else ray.workerCpu,
            'RAY_WORKER_NUM_GPUS': ray.workerLogicGpu if ray.workerLogicGpu != None else workerAcceleratorNum,
            'RAY_WORKER_CUSTOM_RESOURCES': json.dumps(ray.workerCustomResource).replace('"', '\\"') if ray.workerCustomResource != None else '{}',
            'WORKDIR': ray.workdir
        }

        common_utils.fill_template(RAY_TEMPLATE, vars_to_fill, output_path=yaml_path)
        click.secho("Ray framework Launching! Script file is at: <{}>.".format(yaml_path), fg='yellow', nl=True)

        with open(yaml_path, 'r') as f:
            body = yaml.load(f, Loader=yaml.FullLoader)
        try:
            raycluster_api = self.get_raycluster_client()
            # TODO: using apply instead of create would be better
            raycluster_api.create(body=body, namespace=ray.group)
        except Exception as e:
            click.secho("Failed to launch framework on kubernetes {}, Reason: {}"
                        .format(self.name, e.reason if hasattr(e, 'reason') else e), fg='red', nl=True)
        return CloudJobInfo(group=ray.group, job_id=f'{ray.name}-{ray.framework_id}')
    
    def is_ray_ready(self, cloud_job_info: CloudJobInfo) -> bool:
        """Check if the Ray cluster is ready."""
        return self.get_raycluster_details(cloud_job_info).Status == 'ready'

    def get_ray_head_ip(self, cloud_job_info: CloudJobInfo) -> str:
        """Retrieve Head IP of ray that running on the cloud."""
        return self.get_raycluster_details(cloud_job_info).HeadServiceIP

    def _get_ray_head_pod_name(self, cloud_job_info: CloudJobInfo) -> str:
        """Retrieve Head pod name of ray that running on the cloud."""
        core_v1_api = self.get_core_v1_api()
        label_selector = f"ray.io/identifier={cloud_job_info.job_id}-head"
        pods = core_v1_api.list_namespaced_pod(
            cloud_job_info.group, label_selector=label_selector
        )
        if pods.items:
            return pods.items[0].metadata.name
        return None
        
    def get_raycluster_details(self, cloud_job_info: CloudJobInfo) -> 'RayClusterDetails':
        """Get raycluster state details."""
        try:
            if cloud_job_info.job_id:
                raycluster_api = self.get_raycluster_client()
                raycluster = raycluster_api.get(name=cloud_job_info.job_id, namespace=cloud_job_info.group)
                return RayClusterDetails(
                    Status=getattr(raycluster.status, "state", None), 
                    HeadServiceIP=raycluster.status.head.serviceIP
                )
        except Exception as e:
            logger.info(f"Failed to get framework on kubernetes {cloud_job_info.job_id}, Reason: {e.reason if hasattr(e, 'reason') else e}")
        return RayClusterDetails(Status=None, HeadServiceIP=None)
    
    def stop_ray(self, cloud_job_info: CloudJobInfo) -> None:
        """Stop ray Framework."""
        raycluster_api = self.get_raycluster_client()
        try:
            raycluster_api.delete(name=cloud_job_info.job_id, namespace=cloud_job_info.group)
            logger.info(f"Stopping Ray cluster: {cloud_job_info.job_id}")
        except Exception as e:
            logger.warn(f"Failed to stop raycluster {cloud_job_info.job_id}, Reason: {e.reason if hasattr(e, 'reason') else e}")
            raise Exception(f"Failed to stop raycluster {cloud_job_info.job_id}, Reason: {e.reason if hasattr(e, 'reason') else e}")

    def ray_head_port_forward(self, cloud_job_info: CloudJobInfo, ray_port: int) -> int:
        """Forward ray port to local."""
        pod_name = self._get_ray_head_pod_name(cloud_job_info)            
        local_port = common_utils.find_free_port()
        try:
            forwarder = portforward.PortForwarder(cloud_job_info.group, pod_name, local_port, ray_port, os.path.expanduser(self.auth_config))
            forwarder.forward()
        except Exception as e:
            logger.info(f"Port forward Failed. Reason: {e.reason if hasattr(e, 'reason') else e}")
        return local_port