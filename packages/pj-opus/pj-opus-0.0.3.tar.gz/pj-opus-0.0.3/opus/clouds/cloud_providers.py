import enum
from opus import clouds

class CloudProviders(enum.Enum):
    """All supported clouds."""
    SLURM = clouds.Slurm
    KUBERNETES = clouds.Kubernetes