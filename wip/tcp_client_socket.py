#!/usr/bin/python

import sys
from socket import *
serverHost = "127.0.0.1"            # servername is localhost
serverPort = 5006                  # use arbitrary port > 1024

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket


s.connect((serverHost, serverPort)) # connect to server on the port
s.send("ready")               # send the data
data = s.recv(1024)                 # receive up to 1K bytes
print data
s.send("some stuff")               # send the data
s.close()
