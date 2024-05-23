import paramiko

def create_ssh_client(hostname, username, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, username=username, password=password)
    return ssh

def sftp_to_remote(ssh, local_path, remote_path):
    try:
        sftp = ssh.open_sftp()
        sftp.put(local_path, remote_path)
        sftp.close()
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

def sftp_from_remote(ssh, local_path, remote_path):
    try:
        sftp = ssh.open_sftp()
        sftp.get(remote_path, local_path)
        sftp.close()
        return {"status": "success"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
