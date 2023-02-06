import logging

from pyftpdlib.servers import FTPServer

from config.base import (
    DEBUG,
    FTP_MAX_CONNECTIONS,
    FTP_MAX_CONNECTIONS_PER_IP,
    FTP_PORT,
    FTP_WORKER_COUNT,
)
from openspp_dms_ftp_server.handlers import OPENSPPHandler


def main() -> None:
    """
    Main entrypoint to the server.
    :return:
    """
    address = ("0.0.0.0", FTP_PORT)
    server = FTPServer(address, OPENSPPHandler)
    log_level = logging.DEBUG if DEBUG else logging.INFO
    logging.basicConfig(level=log_level)

    # set a limit for connections
    server.max_cons = FTP_MAX_CONNECTIONS
    server.max_cons_per_ip = FTP_MAX_CONNECTIONS_PER_IP

    server.serve_forever(handle_exit=True, worker_processes=FTP_WORKER_COUNT)


if __name__ == "__main__":
    main()
