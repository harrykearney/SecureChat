try:
    from cryptography.fernet import Fernet
    import socket
    print('Imported Libraries.')
except ImportError:
    print('Error importing libraries')

with open('key.key', 'rb') as keyfile:
    key = keyfile.read()

server = socket.socket()

HOST = input(str('What is the hostname of the server? '))
PORT = 8080

ADDR = (HOST, PORT)

server.connect(ADDR)
print(f'Connected to: {HOST}')

running = True

while running:
    incoming_message = server.recv(1024)

    fernet = Fernet(key)
    incoming_message = fernet.decrypt(incoming_message).decode()

    print(f'Server: {incoming_message}')