#!/usr/bin/python

# UDP client example
import socket
import  datetime, timeit

"""
    This is a ten second heart beat using the port
    number as the single word as the heartbeat
    
    28 Jan 2014                                       TEV
    
"""

port    = "5000"
target = '216.97.82.48'

while 1:
     while 1:
         then = datetime.datetime.now() + datetime.timedelta(seconds=10)
         while then > datetime.datetime.now():
             print 'sleeping'
             time.sleep(1)
             break
            
         client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
         client_socket.sendto(port, (target,port))
         client_socket.close()


