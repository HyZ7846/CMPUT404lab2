
connected = True
while connected:
    msg = input(' :')
    if msg == '!quit':
        send(DISCONNECT_MESSAGE)
        break
    send(msg)