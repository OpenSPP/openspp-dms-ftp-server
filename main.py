from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from authorizers import OpenSPPAuthorizer
from config import FTP_SERVER_HOSTNAME, OPENSPP_TOKEN, OPENSPP_USERNAME


def main():
    authorizer = OpenSPPAuthorizer()
    authorizer.add_user(
        username=OPENSPP_USERNAME, password=OPENSPP_TOKEN, perm="elradfmwMT"
    )

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.banner = "Welcome to OpenSPP DMS"

    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = (FTP_SERVER_HOSTNAME, 8002)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()


if __name__ == "__main__":
    main()
