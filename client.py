import sys
import socket


def main():
    message = 'hello world'
    message2 = 'hey'
    port = 18000
    host = "localhost"
    client_socket = socket.socket()
    print(f"Connexion au serveur sur le port {port} depuis la machine {host}")
    client_socket.connect((host, port))
    client_socket.send(message.encode())
    data = client_socket.recv(1024).decode()
    print(data)
    client_socket.send(message2.encode())
    data = client_socket.recv(1024).decode()
    print(data)
    if data == 'arretclient':
        client_socket.close()

if __name__ == '__main__':
    sys.exit(main())