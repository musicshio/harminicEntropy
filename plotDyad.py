import numpy as np
import matplotlib.pyplot as plt
from he import calcHE

C = 1200
x = np.linspace( 0, 1200, C)
y = calcHE(x)
plt.plot(x, y)
plt.show()
plt.savefig('fig.png')
