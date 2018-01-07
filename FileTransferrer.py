import os
import paramiko

with open ("pass.txt", "r") as passwordFile:
    password = str(passwordFile.readline()).strip()

ssh = paramiko.SSHClient()
ssh.load_host_keys(os.path.expanduser(os.path.join("~", ".ssh", "known_hosts")))
#ssh.connect("89.160.197.240", username="server", password=password)
ssh.connect("192.168.1.35", username="server", password=password)
sftp = ssh.open_sftp()
#todo

filename = "testTrans.txt"

path = "public_html/" + filename

sftp.put(filename, "public_html/" + filename)
sftp.close()
ssh.close()