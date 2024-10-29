import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi, 2*np.pi, 0.50)
y = np.sin(x)

plt.plot(x,y, "b--o", label = "$y = sin(x)$")
plt.grid()
plt.legend(loc=1)
plt.show()