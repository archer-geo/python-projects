import socket

name = 
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)
print('Welcome, ' + name)
conn, addr = s.accept()
print( 'Connection address:'+ str(addr))
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    input_msg = input("--> ")
    print(name + ": ", data.decode('utf-8'))
    conn.send(input_msg.encode('utf-8'))
