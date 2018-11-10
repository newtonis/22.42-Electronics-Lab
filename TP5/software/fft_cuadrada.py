from numpy import fft


arr = []
n = 1000

for i in range(n):
    if i < n/2:
        arr.append(1)
    else:
        arr.append(0)
        
print("Fft funcion cuadrada: ")
print(abs(fft.fft(arr, n)))

