import os

OPENSPP_URL = os.getenv("OPENSPP_URL", default="https://dev.newlogic-demo.com")
OPENSPP_DB_NAME = os.getenv("OPENSPP_DB_NAME", default="devel")
OPENSPP_USERNAME = os.getenv("OPENSPP_USERNAME", default="sampleusername")
OPENSPP_TOKEN = os.getenv("OPENSPP_TOKEN", default="samplejwt")
FTP_SERVER_HOSTNAME = os.getenv("FTP_SERVER_HOSTNAME", default="")
