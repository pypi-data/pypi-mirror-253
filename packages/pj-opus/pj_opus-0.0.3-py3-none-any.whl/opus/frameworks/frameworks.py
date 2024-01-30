import os
import pathlib
import enum
import colorama
from typing import List, Tuple, Dict, Optional, Any
import time
from opus.utils import db_utils
from opus import clouds
from opus.common_types import CloudJobInfo
import json

_DB_PATH = os.path.expanduser('~/.opus/opus.db')
pathlib.Path(_DB_PATH).parents[0].mkdir(parents=True, exist_ok=True)
sqliteDB = db_utils.SQLiteDB(_DB_PATH)

# init framework db
sqliteDB.cursor.execute("""create table if not exists frameworks(
                        id integer primary key autoincrement,
                        name varchar(256),
                        cloud_job_info varchar(256),
                        head_external_ip varchar(256),
                        framework_type varchar(16),
                        launched_at integer,
                        status varchar(16),
                        cloud varchar(256)
                        )""")
sqliteDB.conn.commit()

framework_field_order = ('id',
                         'name',
                         'cloud_job_info',
                         'head_external_ip',
                         'framework_type',
                         'launched_at',
                         'status',
                         'cloud')

class FrameworkStatus(enum.Enum):
    # INIT: The `framework` has been launched, but the framework main process has not started yet.
    INIT = 'INIT'

    # UP: The `framework` is ready to use.
    UP = 'UP'

    # STOPPED: The `framework` has been shut down.
    STOPPED = 'STOPPED'

    # UNKNOWN: The `framework` has been disconnected for an unknown reason.
    UNKNOWN = 'UNKNOWN'

    @classmethod
    def unstopped(cls) -> List[str]:
        return [cls.INIT.value, 
                cls.UP.value]

    def with_color(self) -> str:
        return f'{framework_status_color_map[self]}{self.value}{colorama.Style.RESET_ALL}'


framework_status_color_map = {
    FrameworkStatus.INIT: colorama.Fore.CYAN,
    FrameworkStatus.UP: colorama.Fore.GREEN,
    FrameworkStatus.STOPPED: colorama.Fore.YELLOW,
    FrameworkStatus.UNKNOWN: colorama.Fore.MAGENTA,
}


class Framework:

    def __init__(
        self,
        compute_framework_type: str = None,
        name: str = None,
        cloud_name: str = None,
        cloud_type: str = None,
        cloud_login_node: str = None,
        cloud_auth_config: str = None,
        cloud_job_info: CloudJobInfo = None,
        workdir: Optional[List[Tuple[str, str]]] = None,
        headCpu: int = None,
        headMem: str = None,
        headAccelerator: Optional[str] = None,
        headStartParams: Optional[Dict] = None,
        setupCommand: str = None,
        workerCpu: int = None,
        workerMem: str = None,
        workerAccelerator: Optional[str] = None,
        workerStartParams: Optional[Dict] = None,
        workerNum: int = None,
        envs: Optional[str] = None,
        launched_at: int = None,
        status: str = None,
        framework_id: int = None,
        head_external_ip: str = None,
    ) -> None:
       self.framework_id = framework_id
       self.compute_framework_type = compute_framework_type.lower()
       self.name = name
       self.cloud_type = cloud_type.lower()
       _cloud = clouds.CloudProviders[self.cloud_type.upper()].value
       self.cloud = _cloud(name=cloud_name, cloud_type=self.cloud_type, login_node=cloud_login_node, auth_config=cloud_auth_config)
       self.cloud_job_info = cloud_job_info
       self.workdir = workdir
       self.headCpu = headCpu
       self.headMem = headMem
       self.headAccelerator = headAccelerator
       self.headStartParams = headStartParams
       self.setupCommand = setupCommand
       self.workerNum = workerNum
       self.workerCpu = workerCpu
       self.workerMem = workerMem
       self.workerAccelerator = workerAccelerator
       self.workerStartParams = workerStartParams
       self.envs = envs
       self.launched_at = launched_at
       self.head_external_ip = head_external_ip
       self.status = status

    @classmethod
    def create_from_config(cls,
        config: Dict[str, Any],
    ) -> 'Framework':
        """Construct Framework instance from yaml config.
        """
        framework = cls(
            compute_framework_type = config.get('computeFramework').get('type'),
            name = config.get('computeFramework').get('name'),
            cloud_name = config.get('cloud').get('name'),
            cloud_type = config.get('cloud').get('type'),
            cloud_login_node = config.get('cloud').get('login_node'),
            cloud_auth_config = config.get('cloud').get('auth_config'),
            # TODO: name `group` may not reasonable
            cloud_job_info = CloudJobInfo(group=config.get('cloud').get('group'), job_id=""),
            workdir = config.get('workdir'),
            headCpu = config.get('head').get('resources').get('cpu'),
            headMem = config.get('head').get('resources').get('memory'),
            headAccelerator = config.get('head').get('resources').get('accelerators'),
            headStartParams = config.get('head').get('startParams', {}),
            setupCommand = config.get('setup'),
            workerNum = config.get('worker', {}).get('replicas', 0),
            workerCpu = config.get('worker', {}).get('resources', {}).get('cpu', 0),
            workerMem = config.get('worker', {}).get('resources', {}).get('memory', '0G'),
            workerAccelerator = config.get('worker', {}).get('resources', {}).get('accelerators'),
            workerStartParams = config.get('worker', {}).get('startParams', {}),
            launched_at = int(time.time()),
            status = FrameworkStatus.INIT.value,
            envs = config.get('envs')
        )
        framework.framework_id = framework._save()
        return framework
    
    def launch() -> None:
        """Launch Framework."""
        raise NotImplementedError
    
    def stop(self) -> None:
        """Stop Framework."""
        raise NotImplementedError
    
    def is_healthy(self) -> bool:
        """Not implement here"""
        pass
            
    def get_status(self) -> str:
        """Not implement here"""
        pass     
    
    def _update_db(self):
        """Update framework record.
        """
        sql = """
            update frameworks set
                name = ?,
                cloud_job_info = ?,
                head_external_ip = ?,
                framework_type = ?,
                launched_at = ?,
                status = ?,
                cloud = ?
            where id = ?
        """
        sqliteDB.cursor.execute(sql, 
                                (self.name, self.cloud_job_info.json(), self.head_external_ip, self.compute_framework_type, self.launched_at, self.status, self.cloud.to_json(), self.framework_id))
        sqliteDB.conn.commit()
    
    def _save(self) -> int:
        sql = """
            insert into frameworks(name, cloud_job_info, head_external_ip, framework_type, launched_at, status, cloud) values(?, ?, ?, ?, ?, ?, ?)
        """

        sqliteDB.cursor.execute(sql, 
                                (self.name, self.cloud_job_info.json(), self.head_external_ip, self.compute_framework_type, self.launched_at, self.status, self.cloud.to_json()))
        sqliteDB.conn.commit()
        return sqliteDB.cursor.lastrowid

    @classmethod
    def exists(cls, framework_id: int) -> bool:
        rows = sqliteDB.cursor.execute('SELECT EXISTS(SELECT 1 FROM frameworks WHERE id=(?))',
                                       (framework_id,))
        return rows.fetchone()[0]

    @staticmethod
    def get_frameworks(filter_options: List[List[Tuple[str, Any]]] = []) -> List[Dict[str, Any]]:
        if len(filter_options) > 0:
            conditions = [' OR '.join([f"{o[0]} LIKE '%{o[1]}%'" for o in option])
                          for option in filter_options]
            conditions = ' AND '.join([f'({c})' for c in conditions])
            sqliteDB.cursor.execute(f"SELECT {','.join(framework_field_order)} FROM frameworks "
                              f"WHERE {conditions} ORDER BY id DESC")
        else:
            sqliteDB.cursor.execute(f"SELECT {','.join(framework_field_order)} FROM frameworks "
                              "ORDER BY id DESC")
        rows = sqliteDB.cursor.fetchall()
        return [
            {
                framework_field_order[i] : row[i] for i in range(len(framework_field_order))
            } for row in rows
        ]
    
    @staticmethod
    def get_all_framework_ids() -> List[int]:
        rows = sqliteDB.cursor.execute('SELECT id FROM frameworks')
        return [row[0] for row in rows.fetchall()]
    
    @staticmethod
    def delete(framework_ids: Tuple[int]) -> None:
        if not framework_ids:
            return
        sql = "DELETE FROM frameworks WHERE id IN ({})".format(','.join([str(framework_id) for framework_id in framework_ids]))
        sqliteDB.cursor.execute(sql)
        sqliteDB.conn.commit()
    
    @classmethod
    def create_from_record(cls, record: Dict[str, Any]) -> 'Framework':
        """Construct Framework instance from db record.
        """
        cloud_attr = json.loads(record['cloud'])
        return cls(
            framework_id = record['id'],
            compute_framework_type = record['framework_type'],
            name = record['name'],
            cloud_name = cloud_attr.get('name'),
            cloud_type = cloud_attr.get('cloud_type'),
            cloud_login_node = cloud_attr.get('login_node'),
            cloud_auth_config = cloud_attr.get('auth_config'),
            # TODO: name `group` may not reasonable
            cloud_job_info = CloudJobInfo.parse_raw(record['cloud_job_info']),
            launched_at = record['launched_at'],
            head_external_ip = record['head_external_ip'],
            status = record['status']         
        )
    
    def run_job(self):
        """Run a job on a framework."""
        raise NotImplementedError
    
    def get_job_info(self):
        """Get a job's info on a framework."""
        raise NotImplementedError
    
    def stop_job(self):
        """Stop a job on a framework."""
        raise NotImplementedError
    
    def get_job_logs(self):
        """Get a job's logs on a framework."""
        raise NotImplementedError