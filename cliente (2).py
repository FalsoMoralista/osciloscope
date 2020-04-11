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

    for i in range(1, 10):
        recebe = con.recv(1024).decode()
        xstr, ystr = recebe.split(",")
        x = int(xstr)
        y = int(ystr)

        xs.append(x)
        ys.append(y)

    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=1000)
serv_socket.close()
plt.show()


'''
while True:
    recebe = con.recv(1024).decode()
    xstr, ystr = recebe.split(",")
    xint = int(xstr)
    print (xint)
'''

#Sserv_socket.close()