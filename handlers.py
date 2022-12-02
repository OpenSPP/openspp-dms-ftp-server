import os

from pyftpdlib.handlers import FTPHandler

from authorizers import OpenSPPAuthorizer
from clients import OpenSPPClient
from config import DEFAULT_PASSIVE_PORTS
from filesystems import OpenSPPFS


class OpenSPPFTPHandler(FTPHandler):
    abstracted_fs = OpenSPPFS
    authorizer = OpenSPPAuthorizer()
    banner = "Welcome to OpenSPP DMS"
    permit_foreign_addresses = True
    passive_ports = DEFAULT_PASSIVE_PORTS

    def on_file_received(self, file: str) -> None:
        """
        Call OpenSPP method for uploading a file
        :param file: Complete path of a file
        :return:
        """
        openspp_client = OpenSPPClient()
        openspp_client.upload_file(
            username=self.username, password=self.password, filename=file
        )
        os.remove(file)
