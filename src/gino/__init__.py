from .api import Gino, enable_debug  # NOQA
from .engine import GinoEngine, GinoConnection, enable_debug  # NOQA
from .exceptions import *  # NOQA
from .strategies import GinoStrategy  # NOQA


def create_engine(*args, **kwargs):
    """Shortcut for :func:`sqlalchemy.create_engine` with ``strategy="gino"``."""

    from sqlalchemy import create_engine

    kwargs.setdefault("strategy", "gino")
    return create_engine(*args, **kwargs)


def get_version():
    """Get current GINO version."""

    try:
        from importlib.metadata import version
    except ImportError:
        from importlib_metadata import version
    return version("gino")


# noinspection PyBroadException
try:
    __version__ = get_version()
except Exception:
    pass
