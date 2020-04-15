try:
    from cryptography.fernet import Fernet
    print('Imported libraries successfully.')
except ImportError:
    print('Error occurred when importing libraries')

key = Fernet.generate_key()

file = open('key.key', 'wb')
file.write(key)
file.close()