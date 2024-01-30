"""The `opus` command line tool"""
import os
import sys
import click
import shlex
import yaml
import asyncio
import time
import datetime
import pydantic
from typing import Optional, List, Dict, Tuple, Any
import opus
from opus import opus_logging, execution, frameworks, clouds, jobs, rayjobs
from opus.utils import common_utils, validator_utils, schema_utils
from opus.common_types import JobConfig
from opus.common_types import CloudJobInfo
import json

logger = opus_logging.init_logger(__name__)

_CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
_OPUS_CONFIG = "~/.opus/opus_conf.yaml"

def _check_yaml(entrypoint: str) -> Tuple[bool, Optional[Dict[str, Any]]]:
    """Checks if entrypoint is a readable YAML file.

    Args:
        entrypoint: Path to a YAML file.
    """
    is_yaml = True
    config: Optional[List[Dict[str, Any]]] = None
    result = None
    shell_splits = shlex.split(entrypoint)
    yaml_file_provided = (len(shell_splits) == 1 and
                          (shell_splits[0].endswith('yaml') or
                           shell_splits[0].endswith('.yml')))
    try:
        with open(entrypoint, 'r') as f:
            try:
                config = list(yaml.safe_load_all(f))
                if config:
                    result = config[0]
                else:
                    result = {}
                if isinstance(result, str):
                    is_yaml = False
            except yaml.YAMLError as e:
                if yaml_file_provided:
                    logger.debug(e)
                    invalid_reason = ('contains an invalid configuration. '
                                      ' Please check syntax.')
                is_yaml = False
    except OSError:
        if yaml_file_provided:
            entry_point_path = os.path.expanduser(entrypoint)
            if not os.path.exists(entry_point_path):
                invalid_reason = ('does not exist. Please check if the path'
                                  ' is correct.')
            elif not os.path.isfile(entry_point_path):
                invalid_reason = ('is not a file. Please check if the path'
                                  ' is correct.')
            else:
                invalid_reason = ('yaml.safe_load() failed. Please check if the'
                                  ' path is correct.')
        is_yaml = False
    if not is_yaml:
        if yaml_file_provided:
            click.secho(f'{entrypoint!r} looks like a yaml path but {invalid_reason}', fg='red', nl=True)
            sys.exit(1)
    return is_yaml, result

def _check_params(config: Optional[Dict[str, Any]]) -> bool:
    # check if cloud.type and computeFramework type valid
    if config['cloud']['type'].upper() not in [member.name for member in clouds.CloudProviders]:
        click.secho('Invalid cloud type. Only {} are supported.'
                         .format([member.name.lower() for member in clouds.CloudProviders]), fg='red', nl=True)
        sys.exit(1)
            
    if config['computeFramework']['type'].upper() not in [member.name for member in frameworks.FrameworkType]:
        click.secho('Invalid computeFramework type. Only {} are supported.'
                         .format([member.name.lower() for member in frameworks.FrameworkType]), fg='red', nl=True)
        sys.exit(1)

    # check if accelerators valid
    if 'accelerators' in config['head']['resources']:
        accelerators = config['head']['resources']['accelerators']
        common_utils.check_accelerators_format(accelerators)
    
    if config.get('worker') and 'accelerators' in config['worker']['resources']:
        accelerators = config['worker']['resources']['accelerators']
        common_utils.check_accelerators_format(accelerators)


def _launch(yaml_config: Dict[str, Any], cloud: str) -> 'frameworks.Framework':
    # check all parameters in yaml config
    validator_utils.validate_schema(yaml_config, schema_utils.get_framework_schema(),
                                    'Invalid compute framework YAML: ', skip_none=False)
    # add cloud args to config
    is_yaml, cloud_config = _check_yaml(os.path.expanduser(_OPUS_CONFIG))
    if not is_yaml:
        click.secho(f'Opus config is not a yaml file.', fg='red', nl=True)
        sys.exit(1)

    cloud_name = cloud.split(":")[0]
    if cloud_config['clouds'].get(cloud_name) is None:
        click.secho('Cloud {} does not exist. Checking by `opus cloud list`'.format(cloud_name), fg='red', nl=True)
        sys.exit(1)
    
    yaml_str = yaml.dump(yaml_config)
    for key, value in cloud_config.get('clouds').get(cloud_name).get('env', {}).items():
        yaml_str = yaml_str.replace('${' + key + '}', value)
    
    yaml_str = yaml_str.replace('$(whoami)', os.environ.get("USER", ""))
    yaml_config = yaml.load(yaml_str, Loader=yaml.FullLoader)

    yaml_config['cloud'] = {
        'name': cloud_name,
        'type': cloud_config.get('clouds').get(cloud_name).get('type'),
        'login_node': cloud_config.get('clouds').get(cloud_name).get('loginNode'),
        'auth_config': cloud_config.get('clouds').get(cloud_name).get('authConfig'),
        'group': cloud.split(":")[1],
    }
    _check_params(yaml_config)

    compute_framework_type = yaml_config.get('computeFramework').get('type')
    framework = frameworks.FrameworkType[compute_framework_type.upper()].value
    framework = framework.create_from_config(yaml_config)
    opus.launch(framework)
    
    return framework


def format_framework_list(rows: List[Dict[str, Any]]) -> List[List[str]]:
    return [
        [
            row['id'], 
            row['name'], 
            common_utils.readable_time_duration(row['launched_at']),
            row['framework_type'],
            json.loads(row['cloud']).get('name'),
            CloudJobInfo.parse_raw(row['cloud_job_info']).group,
            row['head_external_ip'] if row['head_external_ip'] is not None else "",
            frameworks.FrameworkStatus(row['status']).with_color(),
        ] for row in rows
    ]

class _NaturalOrderGroup(click.Group):
    """Lists commands in the order defined in this script.

    Reference: https://github.com/pallets/click/issues/513
    """

    def list_commands(self, ctx):
        return self.commands.keys()

class _DocumentedCodeCommand(click.Command):
    """Corrects help strings for documented commands such that --help displays
    properly and code blocks are rendered in the official web documentation.
    """

    def get_help(self, ctx):
        help_str = ctx.command.help
        ctx.command.help = help_str.replace('.. code-block:: bash\n', '\b')
        return super().get_help(ctx)

@click.group(cls=_NaturalOrderGroup, context_settings=_CONTEXT_SETTINGS)
@click.version_option(opus.__version__, '--version', '-v', prog_name='opus')
def cli():
    pass

@cli.group(cls=_NaturalOrderGroup)
def cloud():
    """Managed cloud commands."""
    pass

@cloud.command('list', cls=_DocumentedCodeCommand)
def cloud_list():
    is_yaml, yaml_config = _check_yaml(os.path.expanduser(_OPUS_CONFIG))
    if is_yaml:
        # Treat entrypoint as a yaml.
        execution.list_cloud_provider(yaml_config)
    else:
        click.secho(f'{_OPUS_CONFIG} is not a yaml file.', fg='red', nl=True)
        sys.exit(1)

@cli.group(cls=_NaturalOrderGroup)
def framework():
    """Managed Compute Framework commands."""
    pass

@framework.command('launch', cls=_DocumentedCodeCommand)
@click.argument('entrypoint',
                required=True,
                type=str)
@click.option('--cloud',
              'cloud',
              required=True,
              type=str,
              help="""\
              Using available cloud and resource partition, partition means k8s namespace or slurm partition.
              Examples:

              \b
              1. ``--cloud slurm:llm_dev``: using ``slurm`` cluster and ``llm_dev`` partition.""")

def framework_launch(
    entrypoint: str,
    cloud: str,
):
    """Launch a framework from a YAML.

    If ENTRYPOINT points to a valid YAML file, it is read in as the framework
    specification. 
    """
    is_yaml, yaml_config = _check_yaml(entrypoint)
    if is_yaml:
        click.secho('Framework from YAML spec: ', fg='yellow', nl=False)
        click.secho(entrypoint, bold=True)
    else:
        click.secho(f'entrypoint is not a yaml file.', fg='red', nl=True)
        sys.exit(1)
    _launch(yaml_config, cloud)


framework_status_list = [member.name for member in frameworks.FrameworkStatus]
cloud_type_list = [member.name for member in clouds.CloudProviders]

@framework.command('list', cls=_DocumentedCodeCommand)
@click.option('--status',
              '-s',
              required = False,
              multiple = True,
              type = click.Choice(framework_status_list, case_sensitive=False),
              help = 'Filter frameworks by the framework status(es).')
@click.option('--cloud-providers',
              '-cp',
              required = False,
              multiple = True,
              type = click.Choice(cloud_type_list, case_sensitive=False),
              help = 'Filter frameworks by the cloud type(s).')
def framework_list(
    status: Tuple[str],
    cloud_providers: Tuple[str]
):
    """List frameworks' information."""
    table_head = [
        'ID',
        'NAME',
        'AGE',
        'TYPE',
        'CLOUD',
        'GROUP',
        'HEAD_IP',
        'STATUS'
    ]
    framework_table = common_utils.create_table(table_head)
    list_result = format_framework_list(execution.framework_list(status, cloud_providers))
    if len(list_result) == 0:
        click.echo('No matching frameworks.')
    else:
        framework_table.add_rows(list_result)
        click.echo(framework_table)

@framework.command('stop', cls=_DocumentedCodeCommand)
@click.argument('framework_ids',
                required = True,
                type = int,
                nargs = -1)
def framework_stop(framework_ids: Tuple[int]):
    """Stop framework(s) by framework id(s)."""
    for framework_id in framework_ids:
        try:
            execution.framework_stop(framework_id)
        except Exception as e:
            click.secho(f"Failed to stop framework `{framework_id}`. {e}", fg = 'red')
        else:
            click.secho(f"Successfully stopped framework `{framework_id}`.", fg = 'green')


@framework.command('delete', cls = _DocumentedCodeCommand)
@click.argument('framework_ids',
                required = False,
                type = int,
                nargs = -1)
@click.option('--all',
              is_flag = True,
              default = False,
              help = 'If specified, delete all framework records.')
@click.option('--force',
              is_flag = True,
              default = False,
              help = 'If specified, unstopped frameworks will be stopped forcely and deleted.')
def framework_delete(
    framework_ids: Tuple[int],
    all: bool,
    force: bool
):
    """Delete the framework records."""
    if not framework_ids and not all:
        click.secho('Please enter either the framework IDs or `--all` to specify the frameworks to delete.', 
                    fg = 'red')
        sys.exit(1)
    if framework_ids and all:
        click.secho('Framework IDs and `--all` should not be specified at the same time.', fg = 'red')
        sys.exit(1)
    execution.framework_delete(framework_ids, all, force)


@cli.group(cls = _NaturalOrderGroup)
def job():
    """Managed job commands."""
    pass


def _submit(
    config: Dict[str, Any],
    framework_id: int,
    jobname: Optional[str] = None,
    autostop: Optional[bool] = False,
) -> Tuple['jobs.Job', Optional[RuntimeError]]:
    try:
        job_config = JobConfig.parse_obj(config)
        job_config.override_if_cli_option_not_None(jobname = jobname)
        job_id, error = jobs.Job.run(job_config, framework_id, autostop)
        if error is not None:
            raise error
    except (pydantic.ValidationError, ValueError) as e:
        click.secho(f'Failed to submit the job. {e}', fg = 'red')
        sys.exit(1)
    except RuntimeError as e:
        click.secho(f'Job `{job_id}` is submitting ...', fg = 'yellow')
        click.secho(f'Failed to run it on the framework `{framework_id}`. {e}', fg = 'red')
        return (jobs.Job(job_id), RuntimeError(e))
    else:
        click.secho(f'Job `{job_id}` is submitted.', fg = 'green')
        return (jobs.Job(job_id), None)


def _follow_job_logs(job: 'jobs.Job') -> None:
    stream_logs_tips = ('Streaming the job logs ...\n'
                        'Tip: use Ctrl-C to exit log streaming (the job will not be killed).\n')
    click.secho(stream_logs_tips, fg = 'yellow')    
    asyncio.run(execution.follow_job_logs(job))


def _echo_job_final_status(job: 'jobs.Job') -> None:
    job.sync_status()
    click.secho(('\n---------------------------------------'
                 f'\n Job ended with status: {job.status}'
                 '\n---------------------------------------'),
                 fg = 'yellow')    


@job.command('submit', cls = _DocumentedCodeCommand)
@click.argument('entrypoint',
                required = True,
                type = str,
                nargs = -1)
@click.option('--framework-id',
              '-f',
              required = True,
              type = int,
              help = ('The id of a launched compute framework. '
                      'The job will be submitted to it. '))
@click.option('--jobname',
              '-j',
              required = False,
              type = str,
              help = 'The job name is an optional and customizable name you can provide for your job.')
def job_submit(
    entrypoint: Tuple[str],
    framework_id: int,
    jobname: str
):
    """Submit a job to a compute framework.
    The entrypoint can be a yaml file or the job run command strings.
    When you specify both of them, note that the yaml file should be located at the fisrt.
    """
    is_yaml, job_config = _check_yaml(entrypoint[0])
    if not is_yaml:
        job_config = {'run': ' && '.join(entrypoint)}
    else:
        if len(entrypoint) > 1:
            job_config['run'] = ' && '.join(entrypoint[1 : ])
    job, error = _submit(job_config, framework_id, jobname)
    if not error:
        next_step_tips = ('\n--------------- Next step tips ---------------\n'
                          ' To list the jobs:\t>> opus job list\n'
                          f' To stop the job:\t>> opus job stop {job.job_id}\n'
                          f' To get the job logs:\t>> opus logs {job.job_id}'
                          '\n----------------------------------------------\n')
        click.secho(next_step_tips, fg = 'cyan')
        _follow_job_logs(job)
        _echo_job_final_status(job)
    else:
        sys.exit(1)


def format_job_list(rows: List[Dict[str, Any]]) -> List[List[str]]:
    return [
        [
            row['job_id'], 
            '' if row['job_name'] is None else row['job_name'], 
            jobs.JobStatus(row['status']).with_color(), 
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(row['submitted_at'] // 1000)), 
            '-' if row['start_at'] is None else (
                str(datetime.timedelta(
                    seconds = int(time.time()) - row['start_at'] // 1000
                )) if row['end_at'] is None else 
                str(datetime.timedelta(
                    seconds = (row['end_at'] - row['start_at']) // 1000
                ))
            ), 
            row['framework_id']
        ] for row in rows
    ]


@job.command('list', cls = _DocumentedCodeCommand)
@click.option('--status',
              '-s',
              required = False,
              multiple = True,
              type = click.Choice(jobs.JobStatus._member_names_, case_sensitive = False),
              help = 'Filter jobs by the job status(es).')
@click.option('--framework-id',
              '-f',
              required = False,
              multiple = True,
              type = int,
              help = 'Filter jobs by the framework id(s).')
def job_list(
    status: Tuple[str],
    framework_id: Tuple[int]
):
    """List jobs' information."""
    table_head = [
        'JOB_ID',
        'NAME',
        'STATUS',
        'SUBMITTED',
        'RUNNING_TIME',
        'FRAMEWORK_ID'
    ]
    job_table = common_utils.create_table(table_head)
    list_result = execution.list_job(set(status), set(framework_id))
    if len(list_result) == 0:
        click.echo('No matching jobs.')
    else:
        job_table.add_rows(format_job_list(list_result))
        click.echo(job_table)


@job.command('stop', cls = _DocumentedCodeCommand)
@click.argument('job_ids',
                required = True,
                type = int,
                nargs = -1)
def job_stop(job_ids: Tuple[int]):
    """Stop job(s) by job id(s)."""
    not_found_job_ids = []
    for job_id in job_ids:
        try:
            job = jobs.Job(job_id)
            execution.stop_job(job)
        except IndexError:
            not_found_job_ids.append(job_id)
            continue
        except Exception as e:
            click.secho(f"Failed to stop Job `{job_id}`. {e}", fg = 'red')
            continue
        else:
            click.secho(f"Job `{job_id}` is stopped.", fg = 'green')
    if not_found_job_ids:
        click.secho(f'Not found the given job IDs: {tuple(not_found_job_ids)}.', fg = 'red')


@job.command('delete', cls = _DocumentedCodeCommand)
@click.argument('job_ids',
                required = False,
                type = int,
                nargs = -1)
@click.option('--all',
              is_flag = True,
              default = False,
              help = 'If specified, delete all job records.')
@click.option('--force',
              is_flag = True,
              default = False,
              help = 'If specified, unfinished jobs will be stopped forcely and deleted.')
def job_delete(
    job_ids: Tuple[int],
    all: bool,
    force: bool
):
    """Delete the job records."""
    if not job_ids and not all:
        click.secho('Please enter either the job IDs or `--all` to specify the jobs to delete.', fg = 'red')
        sys.exit(1)
    if job_ids and all:
        click.secho('Job IDs and `--all` should not be specified at the same time.', fg = 'red')
        sys.exit(1)
    execution.job_delete(job_ids, all, force)


@cli.command('logs', cls = _DocumentedCodeCommand)
@click.argument('job_ids',
                required = True,
                type = int,
                nargs = -1)
@click.option('--follow',
              flag_value = True,
              default = True,
              help = ('If set, follow and print the job logs. '
                      'Set `--follow` by default if no input.'))
@click.option('--download',
              is_flag = True,
              default = False,
              help = ('If set, download the job logs so far from the remote framework '
                      'and will not print the logs on the console. '))
def logs(
    job_ids: Tuple[int],
    follow: bool,
    download: bool,
):
    """Get the logs of the specific job(s)."""
    if len(job_ids) > 1 and not download:
        click.secho(f'Cannot stream logs of multiple jobs: {job_ids}.', fg = 'red')
        click.secho('Pass `--download` to get the logs of multiple jobs instead.', fg = 'yellow')
        sys.exit(1)
    if download:
        click.secho('Downloading the job logs ...', fg = 'yellow')
        not_found_job_ids = []
        for job_id in set(job_ids):
            try:
                job = jobs.Job(job_id)
                log_path = execution.download_job_logs(job)
            except IndexError:
                not_found_job_ids.append(job_id)
                continue
            except Exception as e:
                click.secho(f"Failed to download the logs of Job `{job_id}`. {e}", fg = 'red')
                continue
            else:
                click.secho(f"Job `{job_id}` logs downloaded to <{log_path}>.", fg = 'blue')
        if not_found_job_ids:
            click.secho(f'Not found the given job IDs: {tuple(not_found_job_ids)}.', fg = 'red')
    elif follow:
        try:
            job = jobs.Job(job_ids[0])
            _follow_job_logs(job)
            _echo_job_final_status(job)         
        except IndexError:
            click.secho(f'Not found the given job ID: {job_ids[0]}.', fg = 'red')
            sys.exit(1)
        except Exception as e:
            click.secho(f"Failed to stream the logs of Job `{job_ids[0]}`. {e}", fg = 'red')
            sys.exit(1)


@cli.group(cls = _NaturalOrderGroup)
def rayjob():
    """Managed rayjob commands."""
    pass


@rayjob.command('submit', cls = _DocumentedCodeCommand)
@click.argument('entrypoint',
                required = True,
                type = str)
@click.option('--cloud',
              required = True,
              type = str,
              help = 'Specify the cloud and group (separated with `:`), for example: `--cloud s-slurm:llmit`.')
@click.option('--name',
              '-n',
              required = False,
              type = str,
              help = 'The name is an optional and customizable name you can provide for your rayjob.')
@click.argument('run',
                required = False,
                type = str)
def rayjob_submit(
    entrypoint: str,
    cloud: str,
    name: str,
    run: str
):
    """Automatically launch a framework and submit the job when the framework is UP.
    The framework will be stopped once the job finished."""
    is_yaml, yaml_config = _check_yaml(entrypoint)
    if not is_yaml:
        click.secho(f'Invalid entrypoint. Please check: {entrypoint}', fg = 'red')
        sys.exit(1)
    
    name = name if name else yaml_config.get('name')
    rayjob = rayjobs.RayJob.save(name)
    click.secho(f'Received RayJob `{rayjob.rayjob_id}`.', fg = 'yellow')
    next_step_tips = ('\n------------------ Next step tips ------------------\n'
                      ' To list the rayjobs:\t>> opus rayjob list\n'
                      f' To delete the rayjob:\t>> opus rayjob delete {rayjob.rayjob_id}'
                      '\n----------------------------------------------------\n')
    click.secho(next_step_tips, fg = 'cyan')
    try:
        framework_config = yaml_config.pop('frameworkSpec')
        framework = _launch(framework_config, cloud)
        rayjob.framework_id = framework.framework_id
        rayjob.refresh_status(rayjobs.RayJobStatus.LAUNCHED)
        click.secho(f'Waiting for Framework `{rayjob.framework_id}` to be UP ...', fg = 'yellow')
        while True:
            if framework.get_status() == frameworks.FrameworkStatus.UP.value:
                click.secho(f'Framework `{rayjob.framework_id}` is UP! Preparing to submit the job ...', fg = 'yellow')
                break
            time.sleep(5)
        
        job_config = yaml_config.pop('jobSpec', {})
        job_config['run'] = run if run else job_config.get('run')
        job, error =_submit(job_config, rayjob.framework_id, autostop = True)
        rayjob.job_id = job.job_id
        if error:
            raise error
    except (Exception, KeyboardInterrupt) as e:
        rayjob.refresh_status(rayjobs.RayJobStatus.INTERRUPTED)
        click.secho(f'RayJob `{rayjob.rayjob_id}` workflow is interrupted by some reasons. {e}', fg = 'yellow')
        click.secho('The job has not been submitted to the ray framework yet.', fg = 'yellow')
    else:
        rayjob.refresh_status(rayjobs.RayJobStatus.SUBMITTED)
        _follow_job_logs(job)        


def format_rayjob_list(rows: List[Dict[str, Any]]) -> List[List[str]]:
    return [
        [
            row['id'], 
            '' if row['name'] is None else row['name'],
            '' if row['framework_id'] is None else row['framework_id'],
            '' if row['job_id'] is None else row['job_id'],
            rayjobs.RayJobStatus(row['status']).with_color(), 
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(row['submitted_at'] // 1000))
        ] for row in rows
    ]


@rayjob.command('list', cls = _DocumentedCodeCommand)
@click.option('--status',
              '-s',
              required = False,
              multiple = True,
              type = click.Choice(rayjobs.RayJobStatus._member_names_, case_sensitive = False),
              help = 'Filter rayjobs by the rayjob status(es).')
def rayjob_list(status: Tuple[str]):
    """List rayjobs' information."""
    table_head = [
        'ID',
        'NAME',
        'FRAMEWORK_ID',
        'JOB_ID',
        'STATUS',
        'SUBMITTED'
    ]
    rayjob_table = common_utils.create_table(table_head)
    list_result = execution.list_rayjob(set(status))
    if len(list_result) == 0:
        click.echo('No matching rayjobs.')
    else:
        rayjob_table.add_rows(format_rayjob_list(list_result))
        click.echo(rayjob_table)


@rayjob.command('delete', cls = _DocumentedCodeCommand)
@click.argument('rayjob_ids',
                required = True,
                type = int,
                nargs = -1)
def rayjob_delete(rayjob_ids: Tuple[int]):
    """Stop rayjob(s) by rayjob id(s) and delete the rayjob records."""
    for rayjob_id in rayjob_ids:
        try:
            rayjob = rayjobs.RayJob(rayjob_id)
            rayjob.delete()
        except Exception as e:
            click.secho(f"Failed to delete RayJob `{rayjob_id}`. {e}", fg = 'red')
            continue


def main():
    return cli()


if __name__ == "__main__":
    main()