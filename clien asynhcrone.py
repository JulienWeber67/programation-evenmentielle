import sys
import socket
def main():
    port = 18000
    host = "localhost"
    client_socket = socket.socket()
    print(f"Connexion au serveur sur le port {port} depuis la machine {host}")
    client_socket.connect((host, port))
    data = ''
    while data != 'bye' or 'arret':
        message = input('')
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

if __name__ == '__main__':
    sys.exit(main())