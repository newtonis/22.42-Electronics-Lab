from numpy import pi
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from numpy import sqrt

n = 1e-9
kilo = 1e3

c1 = c3 = c = 3.3 * n
r4 = 10 * kilo

R1 = [964, 9640, 10]
f = [5*kilo, 50*kilo, 10]

sv = [0, 0.5]

def calcular_valor(r1 , f):
    s = 1j * f * 2 * pi
    r3 = r1
    r2 = 2 * r4
    w0 = 1 / (r1 * c)
    num = (s/w0)**2 + 1
    den = (s/w0)**2 + 3 * r1 * c3 * s + 1

    k = r4 / (r2 + r4)

    H = -k * num / den

    print(abs(H))

    return abs(H)

fig = plt.figure(1)
ax = fig.gca(projection='3d')

r1 = np.arange(R1[0], R1[1], R1[2])
fr = np.arange(f[0], f[1], f[2])

r1, fr = np.meshgrid(r1, fr)



delta_vd = calcular_valor(r1, fr)

# ax.set_title('Sensibilidad de Vd con respecto a Z_1')
ax.set_xlabel('R')
ax.set_ylabel('f')
# ax.set_zlabel('$S_{Vd}^{Z_1}$')

surf = ax.plot_surface(r1, fr, delta_vd, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(sv[0], sv[1])

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()