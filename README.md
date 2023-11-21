# OpenSPP DMS FTP Server

OpenSPP DMS FTP Server is a specialized FTP server project crafted with Python 3.10.
Its main objective is to support OpenSPP by facilitating easy and efficient upload of digital media content from your
local device directly to your OpenSPP account. With the emphasis on user convenience and system performance,
this platform stands as a bridge in accumulating digital assets on your OpenSPP account.

### How it works
OpenSPP DMS FTP Server: This server operates as an effective bridge between your device and your OpenSPP account,
enabling the secure transmission of digital media. Under the hood, it leverages the pyftpdlib - a mature,
robust Python library for implementing FTP server functionalities. The working mechanisms of the server are grounded
in the FTP protocol, a standard network protocol extensively utilized for reliable file transfers across a network.
Here's a general overview of how it works:

- Initiation: The FTP Server initiates the process by establishing a secure connection between your device and the
 OpenSPP server. In order to ensure maximum security and accurate authentication, the server requires the user's
 OpenSPP username and the associated scanner password. Please note that the scanner password is unique and different
 from the regular login password, and it is specifically required for this file transfer process.
- Uploading Process: After a successful connection has been established, you can kick-start the uploading process.
 Leveraging the strength of the FTP protocol and REST architecture, your digital media files are transferred from
 your device over this connection. FTP allows a stable transmission, while RESTful calls ensure the files are uploaded
 seamlessly to the OpenSPP server.
- Data Storage: Once the digital media files are successfully uploaded, they are directly stored into the designated
 DMS directory of your OpenSPP account. To ensure the privacy and security of your data, no files are retained or
 stored on the server-side system during this process
- Ending the Session: Once the file transfer is completed, the FTP Server safely ends the session, ensuring
 the overall security and integrity of the data.

[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


## Getting Started

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

## Configuration
Local values are already provided for quick setup of local environment.

- DEBUG: This setting enables or disables the debug mode. When it's on, the system will provide more detailed
 logs and messages to help troubleshoot any issues. Default: True
- TLS: This stands for Transport Layer Security. If set to True, it specifies that the FTP server should use a
 secure TLS connection. Default: False
- OPENSPP_URL: This denotes the URL of the OpenSPP server to which the FTP server will connect and transfer files.
 Default: http://example.org/
- DEFAULT_PASSIVE_PORTS: This setting defines the range of ports used in passive mode.
 Passive mode is an FTP mode to initiate data connections between the FTP server and client which helps to
 resolve issues related to network firewalls. Default: [3000, 3001, 3002, 3003, 3004, 3005]
- DEFAULT_SSL_CERTFILE: This is the path to the SSL certification file, utilized when establishing a
 secure TLS connection. Default: /etc/ssl/certs/openspp/server.crt
- DEFAULT_SSL_KEYFILE: This is the path to the SSL key file, required along with the certificate file to establish
 a TLS connection. Default: /etc/ssl/certs/openspp/server.key
- FTP_HOSTNAME: This indicates the hostname of the FTP server. Typically, this could be an IP address or
 a domain name. Default: 0.0.0.0 # Will cause errors if used this default in production
- FTP_PORT: Specifies the port at which the FTP server is running and listening for incoming connections. Default: 8002
- FTP_WORKER_COUNT: It determines the number of worker processes that the FTP server should use to handle
 incoming client requests concurrently. Default: 1
- FTP_UPLOAD_DIR: This designates the directory where uploaded files will be stored in the FTP server
 before they are transferred to the OpenSPP. Default: /uploads
- FTP_MAX_CONNECTIONS: This indicates the maximum number of simultaneous connections the FTP server will allow. Default: 256
- FTP_MAX_CONNECTIONS_PER_IP: This outlines the maximum number of connections that the FTP server will
 allow from a single IP address. Default: 0 # For unlimited


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

Clone the project repo at GitHub - OpenSPP/openspp-dms-ftp-server
```shell
git clone https://github.com/OpenSPP/openspp-dms-ftp-server.git
```
Go to the main project directory
```shell
cd openspp-dms-ftp-server
```
Create `production.yml`, the content should be similar to `local.yml`
```shell
cp local.yml production.yml
```
Edit the file similar to this sample
```text
version: "3.8"


services:
  ftp_server:
    image: prod_ftp_server
    build: .
    container_name: prod_ftp
    environment:
      - DEBUG=False
      - TLS=True
      - OPENSPP_URL=<IP or hostname of PDS-SPP e.g. https://spp.pds-mot.gov.iq>
      - FTP_HOSTNAME=<IP of the current VM or the hostname>
    tmpfs: ${FTP_UPLOAD_DIR:-/uploads}
    ports:
      - "8002:8002"
      - "3000-3005:3000-3005"
```
Run the server
```shell
docker compose -f production.yml up --build -d
```

## Testing with a Device
### Scanner Setup
- Setup FTP/FTPS profile
- This is specific to the scanner/printer
- Check the IP for scanner dashboard, usually found at the back of the machine or use the appropriate app provided by the scanner
- Use the following credentials
  - IP/hostname: IP address or hostname of the FTP server
  - Port: 8002
  - Username: your OpenSPP user
  - Password: scanner password of the user (this is different from the account password)
- Make sure to enable PASSIVE mode
- Verify that the scanner have network access to the FTP server on port 8002 and 3000-3005
### Trying it out
- Scan the document using the FTP/FTPS profile created above
- If its successful, go to OpenSPP web browser and check on the DMS directory of the user if the file is present

## License
[Apache 2.0](./LICENSE)
