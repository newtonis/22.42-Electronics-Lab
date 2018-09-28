import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import control
from scipy import signal
import sympy as sp
import matplotlib.patches as mpatches
from pylab import *
from mpldatacursor import datacursor
import numpy as np
import matplotlib.pyplot as plt
import pandas
import xlrd
#nombre del archivo


df = pandas.read_excel('Ejercicio1Capacitor.xlsx')
Freq = df['Freq'].values
font_size = 17;
Freq = Freq*1000;

graficode="Q"

bottom = 10
top = 10*10**6

f=np.logspace(log10(bottom),log10(top),1000)
w= 2*pi*f

R=0.894
L=0.956e-3
C=9.4e-12

Z1 = 1/(1j*w*C)
Z2 = R + 1j*w*L
Z = (Z1*Z2)/(Z1+Z2)

meas_data = df[graficode].values
#para poner latex => r'$\Omega$'

plt.xlabel('Frecuencia(Hz)', fontsize = font_size)
plt.ylabel('R'+'('+r'$\Omega$'+')', fontsize=font_size)
plt.xlim(bottom, top)
plt.title('Respuesta en frecuencia de '+graficode, fontsize = font_size)
plt.semilogx(Freq,meas_data)

CSTR = []
CSTR.append('Práctica')
for i in range(1,11):
    C=9e-12+i*0.1e-12;
    CSTR.append('C=9e-12+'+str(i)+'e-12')
    Z1 = 1. / (1j * w * C)
    Z = (Z1 * Z2) / (Z1 + Z2)
    plt.semilogx(f, abs(Z.imag /Z.real))
plt.legend(CSTR)
plt.show()
