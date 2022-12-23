import os

from pyftpdlib.handlers import FTPHandler, TLS_FTPHandler

from config.base import (
    DEFAULT_PASSIVE_PORTS,
    DEFAULT_SSL_CERTFILE,
    DEFAULT_SSL_KEYFILE,
    FTP_HOSTNAME,
    TLS,
)

from .authorizers import OpenSPPAuthorizer
from .clients import OpenSPPClient
from .filesystems import OpenSPPFS


class OpenSPPFTPHandler(FTPHandler):
    """
    Custom OpenSPP handler that supports OpenSPP's authorizer and custom action for file received.
    """

    abstracted_fs = OpenSPPFS
    authorizer = OpenSPPAuthorizer()
    banner = "Welcome to OpenSPP DMS"
    permit_foreign_addresses = True
    passive_ports = DEFAULT_PASSIVE_PORTS
    masquerade_address = FTP_HOSTNAME

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
        """
        Command to change directory. Not really needed on our use case, so we just return the path.
        :param path: Path to new directory
        :return: Path to new directory
        """
        cwd = self.fs.cwd
        self.respond('250 "%s" is the current directory.' % cwd)
        return path


class OpenSPPTLSFTPHandler(TLS_FTPHandler, OpenSPPFTPHandler):
    """
    Custom handler with TLS enabled.
    """

    certfile = DEFAULT_SSL_CERTFILE
    keyfile = DEFAULT_SSL_KEYFILE
    # Force tls
    # tls_control_required = True
    # tls_data_required = True


OPENSPPHandler = OpenSPPTLSFTPHandler if TLS else OpenSPPFTPHandler
