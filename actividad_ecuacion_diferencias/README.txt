# Actividad - Ecuacion de diferencias

## Ejercicio

Dada la ecuacion:

y[n] = y[n-1] + x[n] + 0.5x[n-1]

con:

x[n] = (0.5)^n, para n >= 0

Condiciones iniciales:

- y[0] = 0
- y[-1] = 0
- x[-1] = 0

Se calculan y grafican los primeros 40 puntos de y[n] utilizando Python y Matplotlib.

## Como abrir el proyecto en Visual Studio Code

1. Descomprime el archivo ZIP.
2. Abre Visual Studio Code.
3. Selecciona **File > Open Folder**.
4. Selecciona la carpeta `actividad_ecuacion_diferencias`.
5. Abre el archivo `ejercicio1.py`.
6. Ejecuta el archivo con el boton **Run Python File**.

## Instalacion de librerias

Si Python ya esta instalado, abre la terminal de VS Code y ejecuta:

```bash
pip install numpy matplotlib
```

Despues ejecuta:

```bash
python ejercicio1.py
```

El programa mostrara los 40 valores de n, x[n] y y[n], y despues generara la grafica.

## Nota sobre y[0]

El problema establece directamente y[0] = 0. Por eso el programa asigna y[0] = 0 y empieza a aplicar la ecuacion de diferencias desde n = 1.
