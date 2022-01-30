import numpy as np
import matplotlib.pyplot as plt
from he import calcDyadHE

C = 1000
x = np.linspace( 0, 1500, C)
y = calcDyadHE(x)
plt.plot(x, y)
plt.show()
plt.savefig('fig.png')
