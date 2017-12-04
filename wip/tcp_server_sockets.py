#!/usr/bin/python

from socket import *
myHost = ''
myPort = 5006

s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket
s.bind((myHost, myPort))            # bind it to the server port
s.listen(5)                         # allow 5 simultaneous
                                        # pending connections


while 1:
    # wait for next client to connect
    connection, address = s.accept() # connection is a new socket
    while 1:
        data = connection.recv(1024) # receive up to 1K bytes
        
        if data:
            print "\n\n\tdata was:  " + data
            connection.send('send attributes' )
        else:
            break
        data2 = connection.recv(1024) # receive up to 1K bytes
        print "\t\tdata2 is: " + data2
        break
    break

connection.close()              # close socket
