try:
    from cryptography.fernet import Fernet
    import socket, os
    print('Imported Libraries.')
except ImportError:
    print('Error importing libraries')

server = socket.socket()

HOST = input(str('What is the hostname of the server? '))
PORT = input('On what port? ')
PORT = int(PORT)

ADDR = (HOST, PORT)

path = os.getcwd()
global KEY
for filename in os.listdir(f'{path}/keys'):
    if filename.endswith('.txt'):
        if filename[:-4] == HOST:
            filecontents = filename.read()
            KEY = file[1]
        else:
            with open(f'{path}/keys/{HOST}.txt', 'wb') as file:
                KEY = Fernet.generate_key()
                file.write(f'{HOST};{KEY}')

server.connect(ADDR)
print('-'*40)
print(f'Connected to: {HOST}')

running = True

while running:
    incoming_message = server.recv(1024)

    fernet = Fernet(key)
    incoming_message = fernet.decrypt(incoming_message).decode()

    print(f'Server: {incoming_message}')