

# this script contains the server side script 
# this is to be run on the computer on the network which yu want to use as the hosting server.

# 789sk.gupta@gmail.com 

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
# both client and server scripts can be run on the same machine 
# just open 2 terminals and execute both scripts and provide the loopback ip address 
# finally yu can test the client and server connectivity on your local machine 
