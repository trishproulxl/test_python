import matplotlib.pyplot as plt
import numpy as np

# Generating data
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plotting the sine and cosine functions
plt.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)

# Adding title and axis labels
plt.title('Sine and Cosine Functions')
plt.xlabel('x')
plt.ylabel('y')

# Adding legend
plt.legend()

# Adding grid
plt.grid(True)

# Displaying the plot
plt.show()
