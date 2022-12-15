from typing import TypeVar

from pyftpdlib.handlers import FTPHandler

TypeHandler = TypeVar("TypeHandler", bound=FTPHandler)
