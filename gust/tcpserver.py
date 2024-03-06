import socket
import sys

class gusttcpserver:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

    def tcpserver(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((self.host, self.port))
            server_socket.listen()
            print(f"Server listening on {self.host}:{self.port}")
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(4096)
                    if not data:
                        break
                    print(f"Received data: {data.decode()}")
                    response = input("Enter response: ") + '\n'
                    conn.send(response.encode())


