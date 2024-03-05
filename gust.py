import pyfiglet
import socket
import sys
import argparse
import gust
import textwrap
from datetime import datetime


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='GENERAL USE SOCKET TOOL',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            gust.py -ps 192.128.1.108 | gust.py --portscan 192.128.1.108
        '''))
    parser.add_argument('-ps', '--portscan', help='Scan ports of the target (can take 16 hours)')
    args = parser.parse_args()
    if args.portscan:
        try:
            ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
            print(ascii_banner)
            target = socket.gethostbyname(args.portscan)
            print("-" * 50)
            print("Scanning Target: " + target)
            print("Scanning started at:" + str(datetime.now()))
            print("-" * 50)
            gust.portscanner.gustpsr(target).scan()
        except KeyboardInterrupt:
            print("\n Exiting Program !!!!")
            sys.exit()
        except socket.gaierror:
            print("\n hostname Could Not Be Resolved !!!!")
            sys.exit()
        except socket.error:
            print("\ Server not responding !!!!")
            sys.exit()
    else:
        print("Invalid command!")

