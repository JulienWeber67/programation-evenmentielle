import socket
import sys
def main():
    while True:

        reply = "message reçu"
        reply2 = "le serveur est actif"
        port = 18000
        host = "localhost"
        server_socket = socket.socket()
        server_socket.bind((host,port))
        print(f"attente du client sur le port {port} depuis la machine {host}")
        server_socket.listen(1)
        conn, address = server_socket.accept()
        data = conn.recv(1024).decode()
        conn.send(reply.encode())
        print(data)
        data = conn.recv(1024).decode()
        conn.send(reply2.encode())
        print(data)
        if data == "bye":
            reply3 = "arretclient"
            data = conn.recv(1024).decode()
            conn.send(reply3.encode())
            print("Le client s'est arrêté")
        if data == "arret":
            conn.close()
            print("Le client et le serveur se sont arrêté")


if __name__ == '__main__':
    sys.exit(main())