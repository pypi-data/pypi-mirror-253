import os
import enum
import pathlib
import time
import colorama
from typing import List, Tuple, Any, Dict
from opus import opus_logging
from opus.utils import db_utils
from opus.frameworks import Framework, FrameworkStatus, FrameworkType

logger = opus_logging.init_logger(__name__)

db_path = os.path.expanduser('~/.opus/opus.db')
os.makedirs(pathlib.Path(db_path).parents[0], exist_ok=True)
db = db_utils.SQLiteDB(db_path)
db.cursor.execute("""CREATE TABLE IF NOT EXISTS rayjobs (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name VARCHAR(256),
                            submitted_at INTEGER,
                            status VARCHAR(16),
                            framework_id INTEGER,
                            job_id INTEGER
                        )""")
db.conn.commit()

record_field_order = ('id', 
                      'name',
                      'submitted_at', 
                      'status',  
                      'framework_id', 
                      'job_id')


class RayJobStatus(enum.Enum):
    """RayJob status."""

    # INIT: The rayjob is received and the rayjob id has been generated.
    INIT = 'INIT'
    # LAUNCHED: The required ray framework has been launched.
    LAUNCHED = 'LAUNCHED'
    # SUBMITTED: The job has been submitted to the ray framework.
    SUBMITTED = 'SUBMITTED'
    # INTERRUPTED: The rayjob workflow is interrupted by some reasons, such as Ctrl-C, terminal exit, or ray job server connection failed.
    INTERRUPTED = 'INTERRUPTED'
    # COMPLETED: The rayjob workflow is completed.
    COMPLETED = 'COMPLETED'

    def with_color(self) -> str:
        return f'{rayjob_status_color_map[self]}{self.value}{colorama.Style.RESET_ALL}'


rayjob_status_color_map = {
    RayJobStatus.INIT: colorama.Fore.CYAN,
    RayJobStatus.LAUNCHED: colorama.Fore.CYAN,
    RayJobStatus.SUBMITTED: colorama.Fore.GREEN,
    RayJobStatus.COMPLETED: colorama.Fore.GREEN,
    RayJobStatus.INTERRUPTED: colorama.Fore.YELLOW,
}


class RayJob:
    """RayJob: automatically launch a Ray framework and submit the job when the framework is UP. 
    The Ray framework will be stopped once the job finished.
    """

    def __init__(self, rayjob_id: int) -> None:
        self.rayjob_id = rayjob_id
        record = self._get_records([[('id', rayjob_id)]])[0]
        self.name = record['name']
        self.submitted_at = record['submitted_at']
        self.status = record['status']
        self.framework_id = record['framework_id']
        self.job_id = record['job_id']
    
    @classmethod
    def save(cls, name: str) -> 'RayJob':
        submitted_at = int(round(time.time() * 1000))
        db.cursor.execute('INSERT INTO rayjobs (name, submitted_at, status) '
                          'VALUES (?, ?, ?)',
                          (name, submitted_at, RayJobStatus.INIT.value))
        db.conn.commit()
        return cls(db.cursor.lastrowid)

    def _update(self) -> None:
        db.cursor.execute('UPDATE rayjobs SET '
                          'status=(?), '
                          'framework_id=(?), '
                          'job_id=(?) '
                          'WHERE id=(?)',
                          (self.status,
                           self.framework_id,
                           self.job_id,
                           self.rayjob_id))
        db.conn.commit()

    @staticmethod
    def _get_records(filter_options: List[List[Tuple[str, Any]]] = []) -> List[Dict[str, Any]]:
        if len(filter_options) > 0:
            conditions = [' OR '.join([f"{o[0]}='{o[1]}'" for o in option]) 
                          for option in filter_options]
            conditions = ' AND '.join([f'({c})' for c in conditions])
            db.cursor.execute(f"SELECT {','.join(record_field_order)} FROM rayjobs "
                              f"WHERE {conditions} ORDER BY id DESC")
        else:
            db.cursor.execute(f"SELECT {','.join(record_field_order)} FROM rayjobs "
                              "ORDER BY id DESC")
        rows = db.cursor.fetchall()
        return [
            {
                record_field_order[i] : row[i] for i in range(len(record_field_order))
            } for row in rows
        ]
    
    def refresh_status(self, status: 'RayJobStatus') -> None:
        self.status = status.value
        self._update()
    
    @classmethod
    def list(cls, filter_options: List[List[Tuple[str, Any]]] = []) -> List[Dict[str, Any]]:
        submitted_rayjobs = cls._get_records([[('status', RayJobStatus.SUBMITTED.value)]])
        for rayjob in submitted_rayjobs:
            rayjob = cls(rayjob['id'])
            framework_record = Framework.get_frameworks([[('id', rayjob.framework_id)]])[0]
            framework = FrameworkType[framework_record['framework_type'].upper()].value
            framework = framework.create_from_record(framework_record)
            if framework.get_status() != FrameworkStatus.UP.value:
                rayjob.refresh_status(RayJobStatus.COMPLETED)
        return cls._get_records(filter_options)

    def delete(self) -> None:
        if self.status == RayJobStatus.INIT.value:
            pass
        else:
            framework_record = Framework.get_frameworks([[('id', self.framework_id)]])[0]
            framework = FrameworkType[framework_record['framework_type'].upper()].value
            framework = framework.create_from_record(framework_record)
            try:
                framework.stop()
            except Exception:
                pass
        db.cursor.execute(f'DELETE FROM rayjobs WHERE id={self.rayjob_id}')
        db.conn.commit()