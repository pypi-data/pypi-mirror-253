"""The opus package."""
import os
from opus.execution import launch

__version__ = '0.0.3'
__root_dir__ = os.path.dirname(os.path.abspath(__file__))

__all__ = [
    '__version__',
    '__root_dir__',
    # framework management
    'launch',
]