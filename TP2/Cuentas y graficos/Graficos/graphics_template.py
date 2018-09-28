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
df = pandas.read_excel('Ejercicio1Inductor.xlsx')
#print the column names
print (df.columns)
#get the values for a given column
#k=1e3
Freq = df['Freq'].values
#Freq = Freq*k
# Q = df['Q'].values
# L = df['L'].values
# R = df['R'].values
# Phi = df['Phi'].values
#
# #get a data frame with selected columns
# FORMAT = ['Freq', 'L', 'Q']
# df_selected = df[FORMAT]

font_size = 17;

Freq = Freq*1000;

graficode="R"

meas_data = df[graficode].values
#para poner latex => r'$\Omega$'

plt.xlabel('Frecuencia(Hz)', fontsize = font_size)
plt.xlim(10,10e6)
plt.title('Respuesta en frecuencia de '+r'$\Phi$', fontsize = font_size)
plt.semilogx(Freq,meas_data)
plt.grid(True, which="both")
plt.show()

# colorTeo="cyan";
# colorPrac="magenta";

# plt.semilogx(f,mag,colorTeo, linewidth = 4)
# plt.semilogx(freq,amp,colorPrac,linewidth = 2.5)
# plt.ylabel('Módulo(dB)', fontsize=font_size)
# datacursor(display='multiple', tolerance=10, formatter="Frec: {x:.3e}  Hz \nAmp:{y:.1f} dB".format, draggable=True)
#
# plt.grid(True, which="both")
# blue_patch = mpatches.Patch(color=colorTeo, label='Teórico')
# green_patch = mpatches.Patch(color=colorPrac, label='Práctica')
# plt.legend(handles=[green_patch, blue_patch])
# plt.xlabel('Frecuencia(Hz)', fontsize = font_size)
# matplotlib.pyplot.subplots_adjust(left=0.180, bottom=0.110, right=0.835, top=0.880, wspace=0.200, hspace=0.200)

# plt.show()
