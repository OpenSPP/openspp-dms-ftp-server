import os

from pyftpdlib.handlers import TLS_FTPHandler

from authorizers import OpenSPPAuthorizer
from clients import OpenSPPClient
from config import (
    DEFAULT_PASSIVE_PORTS,
    DEFAULT_SSL_CERTFILE,
    DEFAULT_SSL_KEYFILE,
    FTP_HOSTNAME,
)
from filesystems import OpenSPPFS


class OpenSPPFTPHandler(TLS_FTPHandler):
    abstracted_fs = OpenSPPFS
    authorizer = OpenSPPAuthorizer()
    banner = "Welcome to OpenSPP DMS"
    permit_foreign_addresses = True
    passive_ports = DEFAULT_PASSIVE_PORTS
    masquerade_address = FTP_HOSTNAME

    # Force tls
    # tls_control_required = True
    # tls_data_required = True
    certfile = DEFAULT_SSL_CERTFILE
    keyfile = DEFAULT_SSL_KEYFILE

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

    def ftp_CWD(self, path: str) -> str:
        cwd = self.fs.cwd
        self.respond('250 "%s" is the current directory.' % cwd)
        return path
