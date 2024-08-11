import socket 
import threading
from pynput.keyboard import Listener,Key,Controller
import json

# This Main sys which sends the keyboard and mouse events to the slave
class Master:
    def __init__(self, IP_address, port):
        self.Ip_address = IP_address
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []   
    
    def on_press(self,key,client):
        print(key)
        if key == Key.esc:
            return False
        data = json.dumps(str(key))
        client.send(data.encode())
       
    def start(self):
        self.s.bind((self.Ip_address, self.port))
        self.s.listen(1)
        print(f"[*] Listening as {self.Ip_address}:{self.port}")
        
        while True:
            
            client, address = self.s.accept()
            print(f"[*] {address} connected")
            if client not in self.clients:
                self.clients.append(client)
            
            print(f"[*] {address} connected")
            client.send("You are connected".encode())
            with Listener(on_press=self.on_press) as listener:
                listener.join()

            
            

            
    def __del__(self):
        self.s.close()
        
        
        
class Slave:
    def __init__(self, IP_address, port):
        self.Ip_address = IP_address
        self.port = port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def start(self):
        self.s.connect((self.Ip_address, self.port))
        print(f"[*] Connected to {self.Ip_address}:{self.port}")
        
        while True:
            msg = self.s.recv(1024).decode()
            data = json.load(msg)
            print(data)
            print(f"[*] {msg}")

                
    def __del__(self):
        self.s.close()