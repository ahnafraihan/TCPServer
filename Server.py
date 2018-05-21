#! /usr/bin/python

# Socket Programming - Server
# Must have this server running before you can run the socket programming Client code

from socket import *

# Create a TCP welcoming socket
serverSocket = socket(AF_INET,SOCK_STREAM)
serverPort = 12000
# Assign IP address and port number to socket
serverSocket.bind(('',serverPort))
# server begins listening for incoming TCP requests
serverSocket.listen(1)

print 'The server is ready to receive'

# loop indefinitely
while True:
          # wait for connections from ClientX and ClientY
          client1, addr1 = serverSocket.accept()
          client2, addr2 = serverSocket.accept()
          
          #receive messages in order of arrival/connection (s1 is first client to connect, s2 is second client to connect)
          res1 = client1.recv(1024)
          print "Message Received: " + res1
          res2 = client2.recv(1024)
          print "Message Received: " + res2

          # if clientX connects first
          if (res1 == 'Client X: Ahnaf'):
          	client1.send ('X: Ahnaf received before Y: Ahnaf')
          	client2.send ('X: Ahnaf received before Y: Ahnaf')
          	print "Sent acknowledgment to both X and Y"
          	break
          # if clientY connects first
          elif (res1 == 'Client Y: Ahnaf'):
          	client1.send ('Y: Ahnaf received before X: Ahnaf')
          	client2.send ('Y: Ahnaf received before X: Ahnaf')
          	print "Sent acknowledgment to both X and Y"
          	break
          else:
          	print "ERROR"

# close sockets
client1.close()
client2.close()
serverSocket.close()