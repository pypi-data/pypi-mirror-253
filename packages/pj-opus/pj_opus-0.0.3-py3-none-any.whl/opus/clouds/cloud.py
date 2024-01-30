from typing import Tuple, Optional, List, Dict, Any
from opus.common_types import CloudJobInfo
import json

class Cloud:
    """A cloud provider, including slurm, kubernetes, and cloud VMs."""

    def __init__(self, name: str = None, 
                 cloud_type: str = None, 
                 login_node: str = None, 
                 auth_config: str = None,
                 group: str = None) -> None:
        """Init cloud."""
        self.name = name
        self.cloud_type = cloud_type
        self.login_node = login_node
        self.auth_config = auth_config
        self.group = group

    def to_json(self):
        """Convert the Cloud object to a JSON string."""
        return json.dumps(self.__dict__)
    
    def launch_ray() -> Optional[Dict[str, Any]]:
        """Launch ray compute framework."""
        raise NotImplementedError
    
    def stop_ray(self, cloud_job_info: CloudJobInfo) -> None:
        """Stop ray Framework."""
        raise NotImplementedError

    def get_resources_info(self) -> Tuple[bool, Optional[List[str]]]:
        """Checks if the user has access credentials to this cloud.
        """
        raise NotImplementedError
    
    def get_ray_head_ip(self, cloud_job_info: CloudJobInfo) -> str:
        """Retrieve Head IP of ray that running on the cloud."""
        raise NotImplementedError