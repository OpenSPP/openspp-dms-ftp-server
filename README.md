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
_WIP_

## Configuration
Local values are already provided for quick setup of local environment.


## Development
_WIP_

#### Type checks


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
