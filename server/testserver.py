import socket
import threading
import time
from queue import Queue


# socket closes after the code ends
# socket s is for listening to events

ADR  = socket.gethostbyname(socket.gethostname())
PORT = 4040
HEADER = 256
FORMAT = "utf-8"

DISCMSG = "DISCONNECT0"
'''
MSG PROTOCAL:
1: length of the msg - int
2: status : svr / cli
3: msg (time)
'''


print("[ADRESS] : ",ADR)

def handle_client(conn , addr):
    print(f"[NEW Connection] : { threading.activeCount()-1 } ")
    with conn:
        print(addr, "Connected.")
        while True:
            msg_len = conn.recv(HEADER).decode(FORMAT)
            if  msg_len:
                
                msg_len = int(msg_len)
                msg = conn.recv(msg_len).decode(FORMAT)
                print(msg)
                
                if(msg==DISCMSG):
                    break


        print("Disconnected.")


def handle_hostclient(conn , addr):
    print(f"[NEW Connection] : { threading.activeCount()-1 } ")

    with conn:
        print(addr, "Connected.")
        while True:
            data = conn.recv(1024).decode(FORMAT)
            if not data:
                break
            conn.sendall(data)
        print("Disconnected.")


def start():

    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("Starting...")
    s.bind((ADR, PORT))
# waits for a connection
    s.listen()

    while True:
        c, addr = s.accept()
        thread = threading.Thread(target=handle_client, args = (c,addr))
        thread.start()

start()