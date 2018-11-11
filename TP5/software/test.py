# coding=utf-8
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy import Piecewise


def formula_cuadrada(n):
    if n % 2 == 0:
        return 0
    else:
        return 0.125 / (np.pi * n)


M = 1e6

data_dbm = [-11.4, 0, -21.4, 0, -26.6, 0, -30.2, 0, -33.3, 0, -35, 0, - 37, 0, -44]

calc_dbm = [formula_cuadrada(i) for i in range(1,len(data_dbm))]
print(data_dbm)
print(calc_dbm)
men_means, men_std = data_dbm, [1]*len(data_dbm)
women_means, women_std = calc_dbm, [1]*len(calc_dbm)

ind = np.arange(len(men_means))  # the x locations for the groups
width = 0.01  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men_means, width, yerr=men_std,
                color='SkyBlue', label='Teórico')
rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,
                color='IndianRed', label='Medido')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Potencia (dBm)')
ax.set_title('Potencias de cada armonico')
#ax.set_xticks(ind)
#ax.set_xticklabels(('1ro', '2do', '3ro', '4to', '5to', '6to', '7mo', '8vo','9np'))
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*offset[xpos], 1.01*height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")

plt.show()
