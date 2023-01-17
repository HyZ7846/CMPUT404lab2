import socket

HEADER = 64
PORT = 5050
DISCONNECT_MESSAGE = "!DISCONNECTED"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

connected = True
while connected:
    msg = input(' :')
    if msg == '!quit':
        send(DISCONNECT_MESSAGE)
        break
    send(msg)