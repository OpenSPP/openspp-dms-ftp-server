import os

OPENSPP_URL = os.getenv("OPENSPP_URL", default="https://dev.newlogic-demo.com")
OPENSPP_DB_NAME = os.getenv("OPENSPP_DB_NAME", default="devel")
DEFAULT_PASSIVE_PORTS = os.getenv(
    "DEFAULT_PASSIVE_PORTS", default=[3000, 3001, 3002, 3003, 3004, 3005]
)
