import socket
import random
import time

ip = "127.0.0.1" 
port = 7000

addr = ((ip,port))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(addr)

for i in range(1, 10):    
    n1 = random.randint(0, 10)
    n2 = random.randint(0, 10)
    x = str(n1)
    y = str(n2)
    string = x + ", " + y
    client_socket.send(string.encode())
    print(string)
    time.sleep(2)
    


client_socket.close()