import socket
from master import Master,Slave

IP_address = socket.gethostbyname(socket.gethostname())



if __name__ == "__main__":
    options = input("Enter 1 for Master and 2 for Slave: ")
    if options == "1":
        master = Master(IP_address,12345)
        master.start()
    elif options == "2":
        slave = Slave(" ",12345)    # IP address is not required for Slave              
        slave.start()
    else:
        print("Invalid option")