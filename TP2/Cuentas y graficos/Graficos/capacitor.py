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

C = df['C'].values

Freq = Freq*1000;
C= C*1e-9
D = df['D'].values
Phi = df['Phi'].values
G = df['G'].values
G=G*1e-6


graficode="C"

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




Rz=8828
Cz=10.4e-9
w0=(4.950e6)*2*pi
Lz=1/(( Cz )*w0**2)

Z1 = (1/(1j*w*Cz))
Z2 = Rz
Z = (Z1*Z2)/(Z1+Z2)+1j*w*Lz
#Y = 1/Z;
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
    #plt.semilogx(f, phaseZ)
elif graficode == "C":
    plt.title('Respuesta en frecuencia de '+graficode, fontsize = font_size)
    plt.ylabel('C' + '(f)', fontsize=font_size)
    Caux=[]
    for i in range(len(f)):
        Caux.append(C)
 #   plt.semilogx(f,Caux)
elif graficode == "Z":
    Admmedida = G
    Sucmedido=(1j*Freq*2*pi*C)
    Ymedido = Admmedida+Sucmedido
    Zmedido=1/(Ymedido)

    absZmed = []
    plt.title('Respuesta en frecuencia del modulo de Y', fontsize=font_size)
    plt.ylabel('|Y|' + '(' + r'$\Omega$' + ')', fontsize=font_size)

    for i in range(len(Zmedido)):
        absZmed.append((abs(Zmedido[i])))

    plt.semilogx(Freq, absZmed)

    absZ = []
    for i in range(len(Z)):
        absZ.append((abs(Z[i])))

    plt.semilogx(f, absZ)
#    plt.loglog(f, absz)
#    plt.loglog(Freq, abs(Zmedida))
CSTR = []


plt.xlabel('Frecuencia(Hz)', fontsize = font_size)
# plt.xlim(bottom, top)
# plt.ylim(bottomY, topY)

if(graficode != "Z"):
    #plt.loglog(Freq, meas_data)
    plt.semilogx(Freq,meas_data)

CSTR.append('Práctica')
CSTR.append('Modelo')
plt.legend(CSTR)

plt.grid(True, which="both")
plt.show()
