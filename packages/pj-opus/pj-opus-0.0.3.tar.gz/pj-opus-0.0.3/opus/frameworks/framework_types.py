import enum
from opus.frameworks.ray import RayFramework

class FrameworkType(enum.Enum):
    RAY = RayFramework