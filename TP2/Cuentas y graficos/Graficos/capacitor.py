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

df = pandas.read_excel('Ejercicio1Capacitor.xlsx')
Freq = df['Freq'].values
font_size = 17;
Freq = Freq*1000;
C = df['C'].values
C= C*1e-9
D = df['D'].values
Phi = df['Phi'].values
G = df['G'].values
G=G*1e-6


graficode="Phi"

# if(graficode != "Z"):
#     meas_data = df[graficode].values
if graficode == "C":
    meas_data = C
elif graficode == "Phi":
    meas_data = Phi
elif graficode == "D":
    meas_data = D
elif graficode == "G":
    meas_data = G





bottom = 10
top = 10*10**6
#
# bottomY = 0
# topY = 10000

f=np.linspace(bottom, top, 3000)
w= 2*pi*f

R=1/0.03
C=10.4e-9

Z1 = 1/(1j*w*C)
Z2 = R
Z = Z1+Z2

#para poner latex => r'$\Omega$'



if graficode == "D":
#    plt.semilogx(f, abs(Z.real/Z.imag))
    plt.ylabel('D' + '(adimensional)', fontsize=font_size)
    plt.title('Respuesta en frecuencia de '+graficode, fontsize = font_size)
elif graficode == "G":
    plt.ylabel('G' + '(' + 'S' + ')', fontsize=font_size)
    plt.title('Respuesta en frecuencia de '+graficode, fontsize = font_size)
#    plt.semilogx(f, 1/Z.real)
elif graficode == "Phi":
    plt.ylabel(r'$\Phi$' + '(deg)', fontsize=font_size)
    plt.title('Respuesta en frecuencia de '+r'$\Phi$', fontsize = font_size)
    phaseZ = []
    for i in range(len(Z)):
        phaseZ.append(np.rad2deg(cmath.phase(Z[i])))
#    plt.semilogx(f, phaseZ)
elif graficode == "C":
    plt.title('Respuesta en frecuencia de '+graficode, fontsize = font_size)
    plt.ylabel('C' + '(f)', fontsize=font_size)
    Caux=[]
    for i in range(len(f)):
        Caux.append(C);
 #   plt.semilogx(f,Caux)
elif graficode == "Z":
    Zmedida=R+1j*Freq*2*pi*C
    absz = []
    plt.title('Respuesta en frecuencia del modulo de ' + graficode, fontsize=font_size)
    plt.ylabel('|Z|' + '(' + r'$\Omega$' + ')', fontsize=font_size)
    for i in range(len(Z)):
        absz.append((abs(Z[i])))
    plt.semilogx(f, absz)
    plt.semilogx(Freq, abs(Zmedida))


CSTR = []

#CSTR.append('Modelo')

plt.xlabel('Frecuencia(Hz)', fontsize = font_size)
# plt.xlim(bottom, top)
# plt.ylim(bottomY, topY)

if(graficode != "Z"):
    #plt.loglog(Freq, meas_data)
    plt.semilogx(Freq,meas_data)
#
# CSTR.append('Práctica')
# plt.legend(CSTR)

plt.grid(True, which="both")
plt.show()
