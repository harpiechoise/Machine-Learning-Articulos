import numpy as np  # Importamos numpy con bajo el alias

a = np.arange(10)  # Creo un rango del 1 al 9
print(a + 10)  # [10 11 12 13 14 15 16 17 18 19]

a = np.eye(3)        # Creo una matriz diagonal de 3x3
b = np.eye(3, k=-1)  # Creo una matriz diagonal de 3x3
print(a + b)
# [[1. 0. 0.]
#  [1. 1. 0.]
#  [0. 1. 1.]]
print(a - b)
# [[ 1.  0.  0.]
#  [-1.  1.  0.]
#  [ 0. -1.  1.]]

a = np.full((3, 2), 5)  # Array de 3x2 de numeros 5
b = np.full((2, 3), 5)  # Array de 2x3 de numeros 5
print(a @ b)    # Producto punto de las dos Arrays
print(a.dot(b))  # Producto punto de las dos Arrays
# [[50 50 50]
#  [50 50 50]
#  [50 50 50]]

a = np.ones((3, 3))  # Array de unos de 3x3
a *= 5  # Operadores de asignacion
print(a)
# [[5. 5. 5.]
#  [5. 5. 5.]
#  [5. 5. 5.]]

a = np.random.random(200)  # Array de valores aleatoreos uniformes
print(a.sum())  # Sumatoria de los valores
print(a.min())  # Valor minimo de mi Array
print(a.max())  # Valor maximo de mi Array

a = np.array([[2, 5], [4, 7]])   # Array de valores aleatorios
print(np.sin(a))                # Seno
print(np.cos(a))                # Coseno
print(np.tan(a))                # Tangente
print(np.arccos(a))             # Arco Coseno
print(np.arcsin(a))             # Arco Seno
print(np.arctan(a))             # Arco Tangente
print(np.exp(a))                # Exponencial
print(np.tanh(a))               # Tangente Hiperbolica
print(np.arctanh(a))            # Arco Tangente Hiperbolica

# Operaciones Logicas
a = np.random.random((3, 2))
print(a > 0.5)
# [[False False]
#  [False  True]
#  [False  True]]

# Operaciones de Bits
a = np.array([3, 2])
print(~a)
# [-4 -3]

# Operaciones con numeros imaginarios
a = np.random.random((3, 2))
a = a * 1j
print(a.dtype)
print(a)
# complex128
# [[0.+0.95952142j 0.+0.84571813j]
#  [0.+0.98370541j 0.+0.65914453j]
#  [0.+0.92270371j 0.+0.60638011j]]

# Sumar Columnas
a = np.random.random((3, 2))
print(a.sum(axis=1))
# [0.56850895 0.51092    0.82053035]
