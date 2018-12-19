# client script to be run on the client machine on the network 

# 789sk.gupta@gmail.com

impot os
import sys

import socket  # imported main socket library to perform networking operations 

client = socket.socket(socket.AF_NET , socket.SOCK_STREAM)

host = raw_input("enter the host ip address") # enter the host ip or is server ip to which it is to be connected 
port = input("enter the port number to connect with")

client.connect((host , port)) # making the connection from the server at this time 

data = client.recv(2048)  # initialised client object to hold the data recieved from the server.

print(data) # prints the recieved data from the server 

# program ends here.
