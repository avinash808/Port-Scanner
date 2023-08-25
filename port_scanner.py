import sys
import socket
import time
import pyfiglet
import threading


ASCII_art_1 = pyfiglet.figlet_format("Port Scanner by sudomosh")
print(ASCII_art_1)

usage = "python3 port_Scanner <TARGET IP> <START PORT> <END PORT>"


print("Scanning the IP:{}\n".format(sys.argv[1]))
print("->"*80)
if(len(sys.argv)!=4):
    print(usage)
    sys.exit()

try:
    target = socket.gethostbyname(sys.argv[1])
except socket.gaierror:
    print("Name Resolution error ")
    sys.exit()

start_port = int(sys.argv[2])
end_port =int(sys.argv[3])


def scan_port(port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(0.5)
    connection = s.connect_ex((target,port))
    if (not connection):
        print("Port Number {} is OPEN".format(port))
    s.close()

for port in range(start_port,end_port+1):
    thread = threading.Thread(target = scan_port, args = (port,))
    thread.start()
