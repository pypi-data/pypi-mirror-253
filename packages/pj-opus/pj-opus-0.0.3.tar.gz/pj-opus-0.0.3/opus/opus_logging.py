"""Logging utils"""
import logging
import sys

_FORMAT = '%(levelname).1s | %(asctime)s | %(filename)s:%(lineno)d -- %(message)s'
_DATE_FORMAT = '%y-%m-%d %H:%M:%S'


class NewLineFormatter(logging.Formatter):
    """Adds logging prefix to newlines to align multi-line messages."""

    def __init__(self, fmt, datefmt=None):
        logging.Formatter.__init__(self, fmt, datefmt)

    def format(self, record):
        msg = logging.Formatter.format(self, record)
        if record.message != '':
            parts = msg.split(record.message)
            msg = msg.replace('\n', '\r\n' + parts[0])
        return msg
    

_root_logger = logging.getLogger('opus')
_default_handler = logging.StreamHandler(sys.stdout)


def _setup_logger():
    _root_logger.setLevel(logging.DEBUG)
    _default_handler.flush = sys.stdout.flush
    _default_handler.setLevel(logging.DEBUG)
    _root_logger.addHandler(_default_handler)
    fmt = NewLineFormatter(fmt=_FORMAT, datefmt=_DATE_FORMAT)
    _default_handler.setFormatter(fmt)
    # Setting this will avoid the message
    # being propagated to the parent logger.
    _root_logger.propagate = False


# The logger is initialized when the module is imported.
_setup_logger()


def init_logger(name: str):
    return logging.getLogger(name)