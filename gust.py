import pyfiglet
import socket
import sys
import argparse
import gust
import textwrap
from datetime import datetime

def print_banner(text):
    ascii_banner = pyfiglet.figlet_format(text)
    print(ascii_banner)

def handle_keyboard_interrupt():
    print('\n Exiting Program !!!!')
    sys.exit()

def handle_hostname_resolution_error():
    print('\n Hostname Could Not Be Resolved !!!!')
    sys.exit()

def handle_server_not_responding_error():
    print('\ Server not responding !!!!')
    sys.exit()

def perform_port_scan(target):
    try:
        print_banner('PORT SCANNER')
        print('-' * 50)
        print('Scanning Target: ' + target)
        print('Scanning started at:' + str(datetime.now()))
        print('-' * 50)
        gust.portscanner.gustpsr(target).scan()
    except KeyboardInterrupt:
        handle_keyboard_interrupt()
    except socket.gaierror:
        handle_hostname_resolution_error()
    except socket.error:
        handle_server_not_responding_error()

def perform_tcp_client(target, port):
    try:
        print_banner('TCP CLIENT')
        print('-' * 50)
        print(f'Connecting to: {target} on port: {port}')
        print('Connection time:' + str(datetime.now()))
        print('-' * 50)
        gust.tcpclient.gusttcpclient(target, port).tcpclient()
    except KeyboardInterrupt:
        handle_keyboard_interrupt()
    except socket.gaierror:
        handle_hostname_resolution_error()
    except socket.error:
        handle_server_not_responding_error()

def perform_tcp_server(target, port):
    try:
        print_banner('TCP SERVER')
        print('-' * 50)
        print(f'Starting server: {target} on port: {port}')
        print('Start time:' + str(datetime.now()))
        print('-' * 50)
        gust.tcpserver.gusttcpserver(target, port).tcpserver()
    except KeyboardInterrupt:
        handle_keyboard_interrupt()
    except socket.gaierror:
        handle_hostname_resolution_error()
    except socket.error:
        handle_server_not_responding_error()
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='GENERAL USE SOCKET TOOL',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=textwrap.dedent('''Example:
            gust.py -ps 192.128.1.108 | gust.py --portscan 192.128.1.108
            gust.py -tcpc 192.128.1.108 -p 80 | gust.py --tcpclient 192.128.1.108 --port 80
            gust.py -tcps 192.128.1.108 -p 80 | gust.py --tcpserver 192.128.1.108 --port 80
        '''))
    parser.add_argument('-ps', '--portscan', help='Scan ports of the target (can take 16 hours)')
    parser.add_argument('-tcpc', '--tcpclient', help='creates a TCP client to send bytes over a network')
    parser.add_argument('-tcps', '--tcpserver', help='creates a TCP server to recieve bytes over a network (use your public)')
    parser.add_argument('-p', '--port', type=int, help='Port for TCP client')
    args = parser.parse_args()

    if args.portscan:
        target = socket.gethostbyname(args.portscan)
        perform_port_scan(target)
    elif args.tcpclient and args.port:
        target = socket.gethostbyname(args.tcpclient)
        perform_tcp_client(target, args.port)
    elif args.tcpserver and args.port:
        target = socket.gethostbyname(args.tcpserver)
        perform_tcp_server(target, args.port)
    else:
        print('Invalid command!')
