import socket

class gustpsr:
    def __init__(self, host) -> None:
        self.host = host

    def scan(self):
        openedports = []
        closedports = []
        for port in range(1,65535):
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                socket.setdefaulttimeout(1)

                result = s.connect_ex((self.host, port))
                if result == 0:
                    print(f"port {port} is opened!")
                    openedports.append(port)
                else: 
                    closedports.append(port)
        print(f"""{self.host} has {len(openedports)} open!
                open ports = {openedports}""")
        print(f"{self.host} has {len(closedports)} open!")