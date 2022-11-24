import sys
import socket
def main():
    port = 18000
    host = "localhost"
    server_socket = socket.socket()
    server_socket.bind((host, port))
    print(f"attente du client sur le port {port} depuis la machine {host}")
    server_socket.listen(1)
    data = ''
    while data != 'arret':
        conn, address = server_socket.accept()
        data = conn.recv(1024).decode()

        while data != 'bye' or 'arret':
            data = conn.recv(1024).decode()
            reply = input('')
            conn.send(reply.encode())

if __name__ == '__main__':
    sys.exit(main())