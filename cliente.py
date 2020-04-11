import socket 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

#####CONNECTION#####
host = '127.0.0.1'
port = 7000

addr = (host, port) 

serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) 

serv_socket.bind(addr) 

serv_socket.listen(10) 

print ('aguardando conexao')

con, cliente = serv_socket.accept()

print ('conectado') 
print ("aguardando mensagem")

y = 0
while True:
    xstr = con.recv(1024).decode()
    x = int(xstr)
    print (x, y)
    y = y + 1
    
serv_socket.close()