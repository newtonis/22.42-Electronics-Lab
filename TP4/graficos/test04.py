
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from numpy import pi
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
from numpy import sqrt
import seaborn as sns
import matplotlib.pyplot as plt

from numpy import exp,arange
from pylab import meshgrid,cm,imshow,contour,clabel,colorbar,axis,title,show


n = 1e-9
kilo = 1e3

c1 = c3 = c = 3.3 * n
r4 = 10 * kilo

R1 = [964, 9640, 10]
f = [5*kilo, 50*kilo, 10]

sv = [0, 0.5, 0.05]

def calcular_valor(r1 , f):
    s = 1j * f * 2 * pi
    r3 = r1
    r2 = 2 * r4
    w0 = 1 / (r1 * c)

    num = (s/w0)**2 + 1
    den = (s/w0)**2 + 3 * r1 * c3 * s + 1

    k = r4 / (r2 + r4)

    H = -k * num / den


    return abs(H)


r1 = np.arange(R1[0], R1[1], R1[2])
fr = np.arange(f[0], f[1], f[2])

r1, fr = np.meshgrid(r1, fr)

var = calcular_valor(r1, fr)


matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'



Z1 = mlab.bivariate_normal(r1, fr, 1.0, 1.0, 0.0, 0.0)
Z2 = mlab.bivariate_normal(r1, fr, 1.5, 0.5, 1, 1)
# difference of Gaussians



# Create a simple contour plot with labels using default colors.  The
# inline argument to clabel will control whether the labels are draw
# over the line segments of the contour, removing the lines beneath
# the label

CS = plt.contour(r1, fr, var)
plt.clabel(CS, inline=100, fontsize=10)
plt.title('Curvas de nivel')
plt.gca().set_ylabel("R1 (ohm)")
plt.gca().set_xlabel("Frecuencia (hz)")

plt.show()