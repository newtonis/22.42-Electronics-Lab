from numpy import fft
from numpy import log10, sqrt

arr = []
n = 1000

for i in range(n):
    if i < n/2:
        arr.append(1)
    else:
        arr.append(0)
        
print("Fft funcion cuadrada: ")
xn = abs(fft.fft(arr, n))
print(xn)
print(10*log10(((((0.125/sqrt(2)*xn)**2)/50.0 * 1000))))

