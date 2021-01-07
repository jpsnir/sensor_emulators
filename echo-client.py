#!/usr/bin/env python3

import socket
import time

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    
    with open('gps-data.txt', 'r') as reader:
        line = reader.readline()
        while line != '':
            b = line.encode()
            s.sendall(b)
            time.sleep(1)
            line = reader.readline()
            data = s.recv(1024)
    
    #s.sendall(b'Hello, world')
    

#print('Received', repr(data))