from typing import TextIO

from pyftpdlib.filesystems import AbstractedFS

from config.base import FTP_UPLOAD_DIR


class OpenSPPFS(AbstractedFS):
    def open(self, filename: str, mode: str) -> TextIO:
        dir_tree = filename.split("/")
        new_filename = "_".join(dir_tree)
        return open(f"{FTP_UPLOAD_DIR}/{new_filename}", mode)

    def listdir(self, path: str) -> list:
        """Don't return anything."""
        return []
