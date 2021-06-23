import time
import socket

ADR  = socket.gethostbyname(socket.gethostname())
PORT = 4040
HEADER = 256
FORMAT = "utf-8"

DISCMSG = "DISCONNECT0"

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ADR,PORT))

def send(msg):
    msg_len = len(msg)
    sent_len = str(msg_len).encode(FORMAT)
    sent_len += b' ' * (HEADER-len(sent_len))
    print(sent_len)
    message = msg.encode(FORMAT)
    client.sendall(sent_len)
    client.sendall(message)

t =0;
while(True):
    send(str(t))
    t+=1
    time.sleep(1)
