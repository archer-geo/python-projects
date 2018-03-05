#!/usr/bin/env python

import socket

name = x
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print('Welcome, ' + name)
while True:
        data = s.recv(BUFFER_SIZE)
        print(name + ": " + data.decode('utf-8'))
        msg_input = input("-->")
        s.send(msg_input.encode('utf-8'))
