

# this script contains the server side script 
# this is to be run on the computer on the network which yu want to use as the hosting server.
# simple tcp listner code 

import os

import sys
import socket

server = socket.socket(socket.AF_STREAM, socket.SOCK_STREAM)
hostip = raw_input("enter the host ip") # enter the same ip which yu enteres the in the client script 

port = input("enter the port number ") # 
server.bind((hostip, port))
server.listen(5) # limit of clients to be connected with the server 

while True:
    connection, address = server.accept()
    print('Got connection from', address)
    connection.send('Welcome to the TCP listener')
    
    connection.close()  # closing the connection
    
# prigram ends :)
