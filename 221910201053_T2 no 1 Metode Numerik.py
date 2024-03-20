import math as mt
import numpy as np
import matplotlib.pyplot as plt

# Inisialisasi
n = 3
x = 0.5
eksak = mt.exp(x)
tollapprox = 0.5 * 10 ** (2 - n)
epsT = np.zeros(25, dtype=float)
epsA = np.zeros(25, dtype=float)
hasil = np.zeros(25, dtype=float)

# Perkiraan nilai dan iterasi
for i in range(25):
    hasil[i] = sum((x ** j) / mt.factorial(j) for j in range(i + 1))
    epsA[i] = abs((hasil[i] - hasil[i - 1]) / hasil[i]) * 100 if i != 0 else 0
    epsT[i] = abs((eksak - hasil[i]) / eksak) * 100

    # Tampilkan hasil setiap iterasi
    print("Iterasi ke:", i + 1)
    print("Estimasi Nilai:", hasil[i])
    print("Epsilon t:", epsT[i])
    print("Epsilon a:", epsA[i])
    print("--------------------")

    # Cek konvergensi dan hentikan iterasi jika memenuhi kriteria
    if i > 1 and epsA[i] < tollapprox:
        break

# Plot hasil
plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.plot(range(i + 1), hasil[:i + 1], marker='o', color='b')
plt.xlabel('Iterasi')
plt.ylabel('Nilai Estimasi')
plt.title('Nilai Estimasi vs Iterasi')

plt.subplot(1, 3, 2)
plt.plot(range(i + 1), epsA[:i + 1], marker='o', color='r')
plt.xlabel('Iterasi')
plt.ylabel('Epsilon a (%)')
plt.title('Epsilon a vs Iterasi')

plt.subplot(1, 3, 3)
plt.plot(range(i + 1), epsT[:i + 1], marker='o', color='g')
plt.xlabel('Iterasi')
plt.ylabel('Epsilon t (%)')
plt.title('Epsilon t vs Iterasi')

plt.tight_layout()
plt.show()
