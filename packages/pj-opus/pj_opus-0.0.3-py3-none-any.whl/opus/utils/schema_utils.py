from schema import Schema, Optional, Or

def get_framework_schema():
    """Compute Framework Schema"""
    return Schema({
        'computeFramework': {
            'type': str,
            'name': str
        },
        'head': {
            'resources': {
                'cpu': int,
                'memory': str,
                Optional('accelerators'): str,
            },
            Optional('startParams'): {
                Optional('numsCpus'): int,
                Optional('numsGpus'): int,
                Optional('customResources'): {
                    Optional(str): Or(float, int),
                },
            }
        },
        Optional('worker'): {
            'replicas': int,
            'resources': {
                'cpu': int,
                'memory': str,
                Optional('accelerators'): str,
            },
            Optional('startParams'): {
                Optional('numsCpus'): int,
                Optional('numsGpus'): int,
                Optional('customResources'): {
                    Optional(str): Or(float, int),
                },
            }
        },
        Optional('setup'): str,
        Optional('envs'): {
            Optional(str): str
        },
        Optional('workdir'): [{
            'name': str,
            'hostPath': str
        }]
    })