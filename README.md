# OpenSPP DMS FTP Server

This project allows FTP client to connect, login and upload files to OpenSPP servers.

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


### Getting Started

Clone this repo
```shell
git clone https://github.com/OpenSPP/openspp-dms-ftp-server.git
```

*Requirements*
- Docker engine or Docker Desktop
- Docker compose
  - It works with both v1 and v2
  - For the sake of uniformity, we are using v2 in our examples

###### Build
```shell
docker compose -f local.yml build
```

###### Run Services
```shell
docker compose -f local.yml up
```

## Documentation
### Quickstart
Run the server using [docker compose command](#run-services)

### Using a client to connect
#### Python Script
```python
import ftplib

HOSTNAME = "localhost"
USERNAME = "sample@user.com"
PASSWORD = "123456"

client = ftplib.FTP()
client.connect(host=HOSTNAME, port=8002)
client.login(user=USERNAME, passwd=PASSWORD)

with open("test.txt", "rb") as file:
    client.storbinary(f'STOR {file.name}', file)
client.close()
```

#### Other clients
This was also tested with Filezilla, Plustek and Brother document scanners (with FTP/SFTP.).
Please enable passive mode to avoid connection issues with your client and server.


## Configuration
Local values are already provided for quick setup of local environment.

```
DEBUG: bool - Enable debug mode for development. Default: True
TLS: bool - Enable to require/support SSL. Default: False
OPENSPP_URL: str - Target host for your OPENSPP instance. Default: https://dev.newlogic-demo.com
OPENSPP_DB_NAME: str - Target database of your OPENSPP instance. Default: devel
DEFAULT_PASSIVE_PORTS: list - List of passive ports to expose. Default: [3000, 3001, 3002, 3003, 3004, 3005]
DEFAULT_SSL_CERTFILE: str - Path to your SSL certfile. Default: /etc/ssl/certs/openspp/server.crt
DEFAULT_SSL_KEYFILE: str - Path to you SSL keyfile. Default: /etc/ssl/certs/openspp/server.key
FTP_HOSTNAME: str - Host name for the server
FTP_PORT: int - Exposed port for the server
FTP_WORKER_COUNT: int - Number of workers for the server to spawn
FTP_UPLOAD_DIR: str - Path to temporary storage of uploaded files while being uploaded to OPENSPP instance
```

## Development
_WIP_

#### Type checks
_WIP_

#### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

```shell
coverage run -m pytest
coverage html
open htmlcov/index.html
```

#### Running tests with pytest
```shell
pytest
```

## Deployment
_WIP_

## License
[Apache 2.0](./LICENSE)
