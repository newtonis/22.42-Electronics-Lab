import numpy as np
import visa

""" Aqui estan las configuraciones que son necesitadas por
todos los archivos.
"""


# Menu scales configuration
wait_time_scale = np.linspace(0.001, 10, 10000)
points_scale = np.linspace(10, 100, 100)
freq_scale = np.logspace(2, 7.3, 1000)
voltage_scale = np.linspace(0.1,20, 200)


# Resistor commercial values
com = [1, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]

# -1 implies we won't measure impedance so we don't need a resistor
res_scale = [-1]

# we generate all resistors values on all orders of magnitude
for i in range(1, 7):
    v = 10 ** i
    for j in com:
        res_scale.append(v * j)


# update rate for periodic event calls

TIME_UPDATE = 0.1

