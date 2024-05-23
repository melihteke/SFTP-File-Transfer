# SFTP-File-Transfer
This Python utility uses the paramiko library to establish an SSH connection and perform secure file transfers using SFTP.

## Functions
create_ssh_client(hostname, username, password)
This function creates and returns an SSH client connected to the specified host. It takes the following parameters:

- hostname: The hostname or IP address of the remote host.
- username: The username to use for authentication.
- password: The password to use for authentication.

sftp_to_remote(ssh, local_path, remote_path)

This function uploads a file from the local system to the remote system. It takes the following parameters:

- ssh: An active SSH client instance.
- local_path: The path to the file on the local system.
- remote_path: The path where the file should be stored on the remote system.

The function returns a dictionary with a status key. If the file transfer is successful, status will be "success". If an error occurs, status will be "error" and an additional message key will contain a description of the error.

sftp_from_remote(ssh, local_path, remote_path)

This function downloads a file from the remote system to the local system. It takes the following parameters:

ssh: An active SSH client instance.
local_path: The path where the file should be stored on the local system.
remote_path: The path to the file on the remote system.
The function returns a dictionary with a status key. If the file transfer is successful, status will be "success". If an error occurs, status will be "error" and an additional message key will contain a description of the error.


## Dependencies
This script requires the paramiko library. You can install it with pip:

```sh
pip install paramiko
```

## Usage
You can use these functions in your own Python scripts to perform secure file transfers over SSH. Here's an example:

```sh
ssh_session = create_ssh_client(hostname="192.168.178.153", username="root", password="password")
scp_from_remote(ssh_session, local_path="interfaces.xml", remote_path="/root/interfaces.xml")
```

