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
#####END CONNECTION############

########GRAPH##################
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

def animate(i):
    xs = []
    ys = []
    y = 0
    while True:
        xstr = con.recv(1024).decode()
        x = int(xstr)
        xs.append(x)
        ys.append(y)
        ax1.plot(xs, ys)
        ani = animation.FuncAnimation(fig, animate, interval=1000)
        plt.show()
        y = y + 1
        plt.pause(0.0001)
#    ax1.clear()
#    ax1.plot(xs, ys)
serv_socket.close()
'''
while True:
    recebe = con.recv(1024).decode()
    xstr, ystr = recebe.split(",")
    xint = int(xstr)
    print (xint)
'''

#Sserv_socket.close()