"""import socket
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 8001
addr = (host,port)

s.bind(addr)
s.listen(5)
while True:
    sock,address = s.accept()
    response = s.recv(1028)
    print(response.decode())"""
    
    
import socket

BYTES_TO_READ = 4096
HOST = "127.0.0.1"
PORT = 8080

def handle_connection(conn, addr):
    with conn:
        print(f"connected by : {addr}")
        while True:
            data = conn.recv(BYTES_TO_READ)
            if not data:
                print('hi')
                break
            print(data)
            conn.send(data)
    return

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.listen()
        
        conn, addr = s.accept()
        handle_connection(conn, addr)
    return

start_server()
    