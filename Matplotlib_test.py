import matplotlib.pyplot as plt
import numpy as np

# Data Generation
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Plotting a graph
plt.plot(x, y, label='sin(x)')
plt.title('Sine graph')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.legend()
plt.grid(True)
plt.show()
