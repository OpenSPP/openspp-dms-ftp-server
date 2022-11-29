import logging

from pyftpdlib.servers import FTPServer

from handlers import OpenSPPFTPHandler


def main():
    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = ("", 2121)
    server = FTPServer(address, OpenSPPFTPHandler)
    logging.basicConfig(level=logging.INFO)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == "__main__":
    main()
