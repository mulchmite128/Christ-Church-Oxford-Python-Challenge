import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 12*np.pi, 10000)
func = np.exp(np.cos(t)) - 2 * np.cos(4 * t) - (np.sin(t / 12)) ** 5
x = np.sin(t) * func
y = np.cos(t) * func
plt.plot(x, y)
plt.gca().set_aspect('equal')
plt.show()
