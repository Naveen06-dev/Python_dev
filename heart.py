import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2 * np.pi, 1000)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

plt.figure(figsize=(6, 6))
plt.plot(x, y, color='red')
plt.fill(x, y, 'red', alpha=0.5)  
plt.gca().set_facecolor('white')  
plt.axis('equal')  
plt.axis('off')  
plt.show()
