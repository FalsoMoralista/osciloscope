import numpy as np
import matplotlib.pyplot as plt
 
# X values
time = np.arange(0, 10, 0.09)

# Y values
amplitude = np.sin(time)

# figure size to 16x9
plt.figure(figsize=(16,9))

#ploting wave
plt.plot(time, amplitude, linewidth=4, color='r')

# Graph Title
plt.title('Onda Senoidal')

# Label of X axis
plt.xlabel('Tempo')

# Label of Y axis
plt.ylabel('Amplitude = seno(tempo)')

plt.grid(True, which='both')
plt.axhline(y=0, color='k')
plt.show()

# Show graph
plt.show()