from numpy import pi
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


vg = 1
r4 = 1e3 / 3.9
c3 = 3.9 * 1e-9
f = 1e4
w = 2 * pi * f
q_min = 0.25 * 50
q_max = 50
l_min = 1.9 * (10**(-3))
l_max = 8.1 * (10**(-3))


r1_min = l_min / (c3 * r4)
r1_max = l_max / (c3 * r4)
r3_min = 1 / (w * c3 * q_max)
r3_max = 1 / (w * c3 * q_min)

R1 = [r1_min, r1_max, 1]
R3 = [r3_min, r3_max, 1]

print("Rango: ")
print("R1 = [", R1[0], ",", R1[1], "]")
print("R3 = [", R3[0], ",", R3[1], "]")

s = [0, 5]

def calcular_delta_vd_z1(z1, z2, z3, z4):
    return abs(vg / (1 + z2/z4) * (1 + z3/z1))

def calcular_delta_vd_z3(z1, z2, z3, z4):
    return abs(vg / (1 + z4/z2) * (1 + z1/z3))

def calcular_delta_vd_z1_r1r3(r1, r3):
    l = c3 * r1 * r4
    rx = r1 * r4 / r3


    z1 = r1
    z2 = (rx * 1j * w * l) / (rx + 1j * w * l)
    z3 = 1 / (1j * w * c3) + r3
    z4 = r4

    return calcular_delta_vd_z1(z1, z2, z3, z4)

def calcular_delta_vd_z3_r1r3(r1, r3):
    l = c3 * r1 * r4
    rx = r1 * r4 / r3

    z1 = r1
    z2 = (rx * 1j * w * l) / (rx + 1j * w * l)
    z3 = 1 / (1j * w * c3) + r3
    z4 = r4

    return calcular_delta_vd_z3(z1, z2, z3, z4)


# grafico 1
fig = plt.figure(1)
ax = fig.gca(projection='3d')

r1 = np.arange(R1[0], R1[1], R1[2])
r3 = np.arange(R3[0], R3[1], R1[2])

r1, r3 = np.meshgrid(r1, r3)
delta_vd = calcular_delta_vd_z1_r1r3(r1, r3)

ax.set_title('Sensibilidad de Vd con respecto a Z_1')
ax.set_xlabel('R1')
ax.set_ylabel('R3')
ax.set_zlabel('$S_{Vd}^{Z_1}$')

surf = ax.plot_surface(r1, r3, delta_vd, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(s[0], s[1])

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

## grafico 2

fig = plt.figure(2)
ax = fig.gca(projection='3d')

r1 = np.arange(R1[0], R1[1], R1[2])
r3 = np.arange(R3[0], R3[1], R1[2])

r1, r3 = np.meshgrid(r1, r3)
delta_vd = calcular_delta_vd_z3_r1r3(r1, r3)

surf = ax.plot_surface(r1, r3, delta_vd, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

ax.set_zlim(s[0], s[1])

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

fig.colorbar(surf, shrink=0.5, aspect=5)

ax.set_title('Sensibilidad de Vd con respecto a Z_3')
ax.set_xlabel('R1')
ax.set_ylabel('R3')
ax.set_zlabel('$S_{Vd}^{Z_3}$')

plt.show()

