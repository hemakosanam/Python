import socket
import subprocess
import sys
from datetime import datetime
subprocess.call('clear',shell=True)
remoteServer = input("enter a remote host to scan:")
remoteServerIP = socket.gethostbyname(remoteServer)
print(" " * 60)
print("please wait, scanning rmote host", remoteServerIP)
print(" " * 60)
t1 = datetime.now()
try:
    for port in range(1,5000):
        sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        result = socket.connect_ex((remoteServerIP, port))
        if result ==0:
            print("port ():   open".format(port))
            sock.close()
except KeyboardInterrupt:
    print("you pressed ctrl+c")
    sys.exit()
except socket.gaierror:
    print("hostname could not be resolved.exiting")
    sys.exit()
except socket.error:
    print("couldn't connect to server")
    sys.exit()