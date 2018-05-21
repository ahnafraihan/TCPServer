# Socket Programming - ClientY

from socket import *

# set server IP and Port
serverName = '127.0.0.1' #remote: '128.226.180.169'
serverPort = 12000
# message to be sent for CLientY
message = 'Client Y: Ahnaf'
# create TCP socket for server, remote port 12000
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect to TCP Server
clientSocket.connect((serverName,serverPort))
# send message for ClientY
clientSocket.send(message)
# receive response from server, which should hold order of connections
response = clientSocket.recv(1024)

# receive response from server, which should hold order of connections
print message
print response

# close connection
clientSocket.close()