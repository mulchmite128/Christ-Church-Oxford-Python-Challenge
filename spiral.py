import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 100000, 10000)
xpositive = ((t / 2) * np.cos(t))[::-1]
ypositive = ((t / 2) * np.sin(t))[::-1]
xnegative = - (t / 2) * np.cos(t)
ynegative = - (t / 2) * np.sin(t)
x = np.concatenate((xpositive, xnegative))
y = np.concatenate((ypositive, ynegative))
plt.plot(x, y)
plt.gca().set_aspect("equal")
plt.show()
