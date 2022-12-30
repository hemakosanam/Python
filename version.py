#import sys
  #print("version of python:",sys.version)


import socket
hostname=socket.gethostname()
print(hostname)

ipadd=socket.gethostbyname(hostname)
print(ipadd)


import os