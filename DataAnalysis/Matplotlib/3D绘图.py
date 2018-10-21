# coding:utf-8

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-4, 4, 100)
y = np.linspace(-4, 4, 100)
Z = 8*np.sin(x) - np.cos(y) + x
X, Y = np.meshgrid(x, y)
# 创建一个3D网格画布
fig = plt.figure()
axes = Axes3D(fig)
s = axes.plot_surface(X, Y, Z, cmap="rainbow")
plt.colorbar(s, shrink=0.5)
plt.show()