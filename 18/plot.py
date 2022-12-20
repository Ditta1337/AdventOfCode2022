import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

with open('/Users/ditta/Desktop/AGH/AdventOfCode2022/18/input.txt', 'r') as f:
    data = [tuple(map(int, line.split(','))) for line in f]


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xticks(range(min(x for x, _, _ in data), max(x for x, _, _ in data)+1))
ax.set_yticks(range(min(y for _, y, _ in data), max(y for _, y, _ in data)+1))
ax.set_zticks(range(min(z for _, _, z in data), max(z for _, _, z in data)+1))

for x, y, z in data:
    X, Y, Z = np.array([[x, x+1, x+1, x], [x, x+1, x+1, x]]), np.array([[y, y, y+1, y+1], [y, y, y+1, y+1]]), np.array([[z, z, z, z], [z+1, z+1, z+1, z+1]])
    ax.plot_surface(X, Y, Z, color='lightblue')
    X, Y, Z = np.array([[x, x+1, x+1, x], [x, x+1, x+1, x]]), np.array([[y, y, y+1, y+1], [y, y, y+1, y+1]]), np.array([[z, z, z, z], [z+1, z+1, z+1, z+1]])
    ax.plot_wireframe(X, Y, Z, color='black', linewidth=0.5)



# show the plot
plt.show()
f.close()
