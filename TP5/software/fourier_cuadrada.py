import sympy as sp
from math import pi
from numpy import exp
import numpy as np

t, duty, pi, wn, n, T = sp.symbols("t duty pi wn n T")
wn = 2 * pi * n/T

h = 1/T*sp.integrate(1 * sp.exp(-sp.I * wn * t), (t, 0, T*duty))


f = sp.simplify(h.subs(duty, 0.5))


values = []

for i in range(100):
    v = f.subs(n, i).subs(pi, np.pi).subs(sp.I,1j).expand(complex=True)
    print(v)
    values.append(abs(v))

print(values )