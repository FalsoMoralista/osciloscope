import socket 
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

host = '127.0.0.1'
port = 7000

addr = (host, port) 

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

socket.bind(addr) 

print('Listening ...')

x = [0]
xs = []
ys = []

plt.style.use('fivethirtyeight')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def animate(i):
    ystr, address = socket.recvfrom(1)
    xs.append(x[0])
    ys.append(ystr)
    plt.cla()
    plt.plot(xs, ys, label='Channel 1')
    if x[0] % 10 == 0:
        ys.clear()
        xs.clear()
#    plt.grid(True)
#    ax.set_title('Osciloscope')
#    ax.set_ylabel('Voltage')
#    ax.set_xlabel('Time (ms)')
#    ax.set_ylim(-5,6)
    x[0] += 1
#    plt.legend(loc='upper left')
ani = FuncAnimation(plt.gcf(), animate, interval=0)
plt.tight_layout()
plt.show()
    
#Sserv_socket.close()
