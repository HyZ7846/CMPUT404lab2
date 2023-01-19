"""import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("www.google.com", 80))
s.send(b"GET / HTTP/1.1\r\nHost:www.google.com\r\n\r\n")
response = s.recv(4096)
s.close()
print(response.decode())"""

import socket

BYTES_TO_READ = 4096

def get(host, port):
    # Created our request
    request_data = b"GET / HTTP/1.1\nHost:" + host.encode('utf-8') + b"\n\n"
    
    # Created our socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # we have sent some data on our socket
    s.connect((host,port))
    s.send(request_data)
    s.shutdown(socket.SHUT_WR)
    
    # listen for response
    response = s.recv(BYTES_TO_READ)
    while(len(response) > 0):
        print(response)
        response = s.recv(BYTES_TO_READ)
    
    s.close()
    
    
get("www.google.com",80)