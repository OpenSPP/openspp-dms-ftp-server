import tempfile
from typing import TextIO

from pyftpdlib.filesystems import AbstractedFS


class OpenSPPFS(AbstractedFS):
    def open(self, filename: str, mode: str) -> TextIO:
        filename = filename.split("/")[-1]
        # Use mkdtemp, so it persist and should be removed on
        # OpenSPPFTPHandler.on_file_received after uploading to OpenSPP
        temp_dir = tempfile.mkdtemp()
        return open(f"{temp_dir}/{filename}", mode)

    def listdir(self, path: str) -> list:
        """Don't return anything."""
        return []
