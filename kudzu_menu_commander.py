import os
import socket
import time

HOST = "10.170.0.10"
PORT = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                time.sleep(310)
                continue
            conn.sendall(data)