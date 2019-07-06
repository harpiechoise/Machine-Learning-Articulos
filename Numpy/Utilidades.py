import numpy as np
# 2 Útilidades

# Principio del Rango de numpy
print(np.arange(2, 13))  # [ 2  3  4  5  6  7  8  9 10 11 12]

# Pasos del rango
print(np.arange(2, 13, 2))  # [ 2  4  6  8 10 12]

# Matriz de zeros
print(np.zeros((3, 3)))  # 3 filas y 3 Columnas de ceros
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

# Matriz de unos
print(np.ones((3, 3)))
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

# Matriz identidad
print(np.eye(3))  # Matriz identidad de 3x3
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# Matriz de cualquier valor
print(np.full((3, 3), 6))  # Matriz de 3x3 con el numero 6
# [[6 6 6]
#  [6 6 6]
#  [6 6 6]]

# Matriz diagonal
print(np.diag([1, 2, 3, 4, 5]))  # Diagonal de 5x5
# [[1 0 0 0 0]
#  [0 2 0 0 0]
#  [0 0 3 0 0]
#  [0 0 0 4 0]
#  [0 0 0 0 5]]

# Repetir una Matriz determinada
v = np.array([1, 2, 3])
print(np.tile(v, (3, 1)))  # Repetir 3 veces en las filas y 1 en las columnas
# [[1 2 3]
#  [1 2 3]
#  [1 2 3]]

v = np.array([1, 2, 3])
print(np.tile(v, (3, 2)))  # Repetir 3 veces en las filas y 2 en las columnas

# [[1 2 3 1 2 3]
#  [1 2 3 1 2 3]
#  [1 2 3 1 2 3]]

# Aleatorio
print(np.random.random())  # 0.45667890913413645
print(50 * np.random.random() + 2)  # Aleatorio entre 2 y 52

# 35.96414339427922
