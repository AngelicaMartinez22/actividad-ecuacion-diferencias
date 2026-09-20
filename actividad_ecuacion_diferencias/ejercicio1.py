import numpy as np
import matplotlib.pyplot as plt

# ============================================
# Ecuacion de diferencias:
# y[n] = y[n-1] + x[n] + 0.5*x[n-1]
#
# Entrada:
# x[n] = (0.5)^n, n >= 0
#
# Condiciones iniciales:
# y[0] = 0
# y[-1] = 0
# x[-1] = 0
# ============================================

N = 40
n = np.arange(N)

# Entrada x[n] = (0.5)^n
x = (0.5) ** n

# Salida y[n]
y = np.zeros(N)

# Condicion inicial indicada por el problema
y[0] = 0

# Calculo de la ecuacion de diferencias
# Se inicia en n=1 porque y[0] ya esta definido.
for i in range(1, N):
    y[i] = y[i - 1] + x[i] + 0.5 * x[i - 1]

# Mostrar resultados
print(" n        x[n]             y[n]")
print("-------------------------------------")
for i in range(N):
    print(f"{i:2d}     {x[i]:.10f}      {y[i]:.10f}")

# Grafica de los primeros 40 puntos de y[n]
plt.figure(figsize=(10, 6))
plt.stem(n, y)
plt.title("Respuesta y[n] - Primeros 40 puntos")
plt.xlabel("n")
plt.ylabel("y[n]")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
