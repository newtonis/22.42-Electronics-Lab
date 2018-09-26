import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from math import *
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pylab as pl
from random import *


def random_color():
    return '#%02x%02x%02x' % (randrange(256),randrange(256), randrange(256))


fig, ax1 = plt.subplots()
psi_values = [0.001, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
patches = []

for psi in psi_values:
    w_all = 10.0**np.arange(4, 9, 0.001)

    w0 = 10**6 * 2 * pi

    h = signal.lti([1, 0], [1/w0**2, 2 * psi / w0, 1])

    w, mag, phase = signal.bode(h, w_all)

    f = [i / 2 / pi for i in w]
    col = random_color()

    patches.append(mpatches.Patch(color=col, label="$\psi ="+str(psi)+"$"))


    # axes.figure()

    ax1.semilogx(f, mag, col, linewidth="2")


ax1.set_axisbelow(True)
ax1.minorticks_on()
ax1.grid(which='major', linestyle='-', linewidth='0.3', color='black')
ax1.grid(which='minor', linestyle=':', linewidth='0.1', color='black')

plt.legend(handles=patches)

plt.show()