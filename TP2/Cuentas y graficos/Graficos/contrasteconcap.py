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
import cmath

df = pandas.read_excel('Ejercicio1Inductor.xlsx')
Freq = df['Freq'].values
font_size = 17;
Freq = Freq*1000;
L = df['L'].values
L = L*1e-3;
Q = df['Q'].values
Phi = df['Phi'].values
R = df['R'].values

graficode="L"

bottom = 10
top = 10*10**6
#
# bottomY = 0
# topY = 10000

f=np.linspace(bottom, top, 3000)
w= 2*pi*f

R=0.894
L=0.96e-3
C=9.28e-12

Z1 = 1/(1j*w*C)
Z2 = R + 1j*w*L
Z = (Z1*Z2)/(Z1+Z2)

if(graficode != "Z"):
    meas_data = df[graficode].values

#para poner latex => r'$\Omega$'



if graficode == "Q":
    plt.semilogx(f, abs(Z.imag/Z.real))
    plt.ylabel('Q' + '(adimensional)', fontsize=font_size)
    plt.title('Respuesta en frecuencia de '+graficode, fontsize = font_size)
elif graficode == "R":
    plt.ylabel('R' + '(' + r'$\Omega$' + ')', fontsize=font_size)
    plt.title('Respuesta en frecuencia de '+graficode, fontsize = font_size)
    plt.semilogx(f, Z.real)
elif graficode == "Phi":
    plt.ylabel(r'$\Phi$' + '(deg)', fontsize=font_size)
    plt.title('Respuesta en frecuencia de '+r'$\Phi$', fontsize = font_size)
    phaseZ = []
    for i in range(len(Z)):
        phaseZ.append(np.rad2deg(cmath.phase(Z[i])))
    plt.semilogx(f, phaseZ)
elif graficode == "L":
    meas_data=meas_data*1e-3
    plt.title('Respuesta en frecuencia de '+graficode, fontsize = font_size)
    plt.ylabel('L' + '(Hy)', fontsize=font_size)
    plt.semilogx(f, Z.imag/w)
elif graficode == "Z":
    Zmedida=R+1j*Freq*2*pi*L
    absz = []
    plt.title('Respuesta en frecuencia del modulo de ' + graficode, fontsize=font_size)
    plt.ylabel('|Z|' + '(' + r'$\Omega$' + ')', fontsize=font_size)
    for i in range(len(Z)):
        absz.append((abs(Z[i])))
    plt.semilogx(f, absz)
    plt.semilogx(Freq, abs(Zmedida))


CSTR = []

CSTR.append('Modelo')

plt.xlabel('Frecuencia(Hz)', fontsize = font_size)
# plt.xlim(bottom, top)
# plt.ylim(bottomY, topY)

if(graficode != "Z"):
    plt.semilogx(Freq,meas_data)

CSTR.append('Práctica')
plt.legend(CSTR)

plt.grid(True, which="both")
plt.show()
