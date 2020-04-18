try:
    from cryptography.fernet import Fernet
    import socket
    print('Imported Libraries.')
except ImportError:
    print('Error importing libraries')

with open('key.key', 'rb') as keyfile:
    key = keyfile.read()

server = socket.socket()

HOST = '127.0.0.1'
PORT = input('What port would you like to open the server on? ')
PORT = int(PORT)

ADDR = (HOST, PORT)

server.bind(ADDR)

print(f'Name: {HOST}')
print(f'PORT: {PORT}')

server.listen(1)

CONN, ADDR = server.accept()

print(f'{ADDR} has connected to the server! Say Hi!')

running = True

while running:
    # Send Message
    message = input(str('>> ')).encode()
    message = Fernet(key).encrypt(message)

    CONN.send(message)
    print('Message has been sent..')

    # Receive Message
    incoming_message = server.recv(1024)

    fernet = Fernet(key)
    incoming_message = fernet.decrypt(incoming_message).decode()

    print(f'Client: {incoming_message}')