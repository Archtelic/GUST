import socket
import sys

class gusttcpclient:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

    def tcpclient(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            s.sendall(b' ')
            try:
                while True:
                    recv_len = 1
                    response = ''
                    while recv_len:
                        data = s.recv(4096)
                        response += data.decode()
                        recv_len = len(data)
                        if recv_len < 4096:
                            break
                    if response:
                        print('< ' + response)
                        buffer = input('> ')
                        buffer += '\n'
                        s.send(buffer.encode())
            except KeyboardInterrupt:
                print('\n Ending program')
                sys.exit()