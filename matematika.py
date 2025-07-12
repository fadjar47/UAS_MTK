import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Input fungsi aljabar dari pengguna
fungsi_input = input("Masukkan fungsi aljabar (misal: x**2 + 2*x + 1): ")
x = sp.symbols('x')
fungsi = sp.sympify(fungsi_input)

# Menghitung turunan dan integral
turunan = sp.diff(fungsi, x)
integral = sp.integrate(fungsi, x)

# Menampilkan hasil
print(f"Fungsi: {fungsi}")
print(f"Turunan: {turunan}")
print(f"Integral: {integral} + C")

# Menggambar grafik
x_vals = np.linspace(-10, 10, 400)
y_vals = [fungsi.subs(x, val) for val in x_vals]
y_turunan = [turunan.subs(x, val) for val in x_vals]

plt.figure(figsize=(12, 6))
plt.plot(x_vals, y_vals, label='Fungsi', color='blue')
plt.plot(x_vals, y_turunan, label='Turunan', color='red', linestyle='--')
plt.title('Grafik Fungsi dan Turunan')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5, ls='--')
plt.axvline(0, color='black',linewidth=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()