import socket
from master import Master,Slave

IP_address = socket.gethostbyname(socket.gethostname())

# Creating the Master and Slave objects
slave = Slave("192.168.1.14",12345)
slave.start()

