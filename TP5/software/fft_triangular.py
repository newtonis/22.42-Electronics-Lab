from numpy import fft


arr = []
n = 100

for i in range(n+1):
    if i < n/2:
        arr.append(i)
    else:
        arr.append(n-i)

print("Fft funcion cuadrada: ")
print(abs(fft.fft(arr, n+1)))



