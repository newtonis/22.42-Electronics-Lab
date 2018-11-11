import sympy as sp
from math import pi
from numpy import exp
import numpy as np

t, duty, wn, n, k, T = sp.symbols("t duty wn n k T")
wn = 2 * sp.pi * n/T

h = 2 * 1/T*(sp.integrate((t*(4/T) * sp.exp(-sp.I * wn * t)) , (t, 0, T/2))
    + sp.integrate( ((2-(t-T/2)*(4/T)) * sp.exp(-sp.I * wn * (t) )), (t, T/2, T)) )



print(sp.pretty(sp.simplify(h)))

# values = []

# for i in range(100):
#     v = f.subs(n, i).subs(pi, np.pi).subs(sp.I,1j).expand(complex=True)
#     print(v)
#     values.append(abs(v))
#
# print(values )