import os
from pydantic import BaseModel, Field, validator
from typing import Optional, Dict, List

class CloudJobInfo(BaseModel):
    group: str
    job_id: str

class RayLaunchParams(BaseModel):
    framework_id: int
    name: str
    group: str
    setupCommand: Optional[str]
    envs: Optional[Dict]
    workerNum: int
    headCpu: int
    headMem: str
    headAccelerator: Optional[str]
    headLogicCpu: Optional[int]
    headLogicGpu: Optional[int]
    headCustomResource: Optional[Dict]
    workerCpu: int
    workerMem: str 
    workerAccelerator: Optional[str]
    workerLogicCpu: Optional[int]
    workerLogicGpu: Optional[int]
    workerCustomResource: Optional[Dict]
    workdir: Optional[List[Optional[Dict]]]

class JobConfig(BaseModel):
    """JobConfig includes fields about its submission definition."""

    jobname: Optional[str] = Field(
        None, 
        description = 'The display name for this job.'
    )
    workdir: Optional[str] = Field(
        None, 
        description = 'The working directory for this job.'
    )
    run: str = Field(
        ..., 
        description = 'The run command for this job.'
    )
    upload: Optional[Dict[str, str]] = Field(
        None,
        description = 'Upload the local files/directories to the remote before the job submission.'
    )

    @validator('workdir')
    def check_workdir_if_not_None(cls, workdir):
        if workdir is None:
            return
        workdir = os.path.abspath(os.path.expanduser(workdir))
        if not os.path.exists(workdir):
            raise ValueError(f'The workdir {workdir!r} not found.')
        return workdir
    
    def override_if_cli_option_not_None(self, **kwargs):
        for arg_name, arg_value in kwargs.items():
            if arg_value is not None:
                setattr(self, arg_name, arg_value)


class SlurmJobDetails(BaseModel):
    JobState: str
    BatchHostIP: str

class RayClusterDetails(BaseModel):
    Status: Optional[str]
    HeadServiceIP: Optional[str]