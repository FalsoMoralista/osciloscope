import socket 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
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

plt.style.use('fivethirtyeight')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

x = [0]
xs = []
ys = []
def animate(i):
    ystr = con.recv(1).decode()
    y = int(ystr)
    xs.append(x[0])
    ys.append(y)
    plt.cla()
    plt.plot(xs, ys, label='Channel 1')
    plt.grid(True)
    ax.set_title('Osciloscope')
    ax.set_ylabel('Voltage')
    ax.set_xlabel('Time (ms)')
    ax.set_ylim(-5,6)
    x[0] += 1
    plt.legend(loc='upper left')
    
ani = FuncAnimation(plt.gcf(), animate, interval=0)
plt.tight_layout()
plt.show()
    
#Sserv_socket.close()
