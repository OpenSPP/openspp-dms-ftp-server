import os

OPENSPP_URL = os.getenv("OPENSPP_URL", default="https://dev.newlogic-demo.com")
OPENSPP_DB_NAME = os.getenv("OPENSPP_DB_NAME", default="devel")
DEFAULT_PASSIVE_PORTS = os.getenv(
    "DEFAULT_PASSIVE_PORTS", default=[3000, 3001, 3002, 3003, 3004, 3005]
)
DEFAULT_SSL_CERTFILE = os.getenv(
    "DEFAULT_SSL_CERTFILE", default="/etc/ssl/certs/openspp/server.crt"
)
DEFAULT_SSL_KEYFILE = os.getenv(
    "DEFAULT_SSL_KEYFILE", default="/etc/ssl/certs/openspp/server.key"
)
FTP_HOSTNAME = os.getenv("FTP_HOSTNAME", default="0.0.0.0")
FTP_PORT = os.getenv("FTP_PORT", default=8002)
DEBUG = os.getenv("DEBUG", default=True)
