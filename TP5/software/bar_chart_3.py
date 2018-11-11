import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, log10
from numpy import pi

def formula_cuadrada(n):
    if n % 2 == 0:
        xn = 0
    else:
        xn = 4*(0.125/2) / ((pi * n)**2)

    power = 2*xn**2/50
    return int(10*log10((power*1000.0))*10)/10


arr = [-15.8, -35.6, -44.2, -50.2, -54.0, -57.6, -59.2, -62.8]
calc_dbm = [formula_cuadrada(i) for i in [1,3,5,7,9,11,13,15]]
print(arr)
print(calc_dbm)

men_means, men_std = arr, [0]*len(arr)
women_means, women_std = calc_dbm, [0]*len(arr)

ind = np.arange(len(men_means))  # the x locations for the groups
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width/2, men_means, width, yerr=men_std,
                color='SkyBlue', label='Medido')
rects2 = ax.bar(ind + width/2, women_means, width, yerr=women_std,
                color='IndianRed', label='Teórico')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Potencia (dBm)')
ax.set_title('Señal Triangular Simetría 50%, potencia de cada armónico')
ax.set_xticks(ind)
ax.set_xticklabels(('1', '3', '5', '7', '9', '11', '13', '15'))
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