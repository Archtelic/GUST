import pyfiglet
import socket
import sys
import argparse
import gust
from datetime import datetime

if __name__ == "__main__":
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(ascii_banner)
    try:
        if len(sys.argv) == 2:
            target = socket.gethostbyname(sys.argv[1])
            print("-" * 50)
            print("Scanning Target: " + target)
            print("Scanning started at:" + str(datetime.now()))
            print("-" * 50)
            gust.portscanner.gustpsr(target).scan()
        else:
            print("Invalid number of arguments!")
    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
    except socket.gaierror:
            print("\n hostname Could Not Be Resolved !!!!")
            sys.exit()
    except socket.error:
            print("\ Server not responding !!!!")
            sys.exit()
