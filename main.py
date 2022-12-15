import logging

from pyftpdlib.servers import FTPServer

from config import DEBUG, FTP_PORT, FTP_WORKER_COUNT
from handlers import OPENSPPHandler


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
    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever(handle_exit=True, worker_processes=FTP_WORKER_COUNT)


if __name__ == "__main__":
    main()
