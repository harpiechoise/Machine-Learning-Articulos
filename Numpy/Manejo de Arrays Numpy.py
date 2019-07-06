import numpy as np  # Importamos numpy

# Numpy Linspace
a = np.linspace(10, 50, 5)
# 5 Valores igualmente distribuidos, es decir, sus distancias son iguales
print(a)
# [10. 20. 30. 40. 50.]
print(a.itemsize)  # Tamaño en Bytes de cada elemento
# 8

# Reshape
print(np.arange(9))
# [0 1 2 3 4 5 6 7 8]

print(np.arange(9).reshape(3, 3))
# Distribuir 9 valores en 3 filas y 3 columnas

# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(np.arange(9).reshape(3, 3).shape)
# (3, 3)

# Indices
a = np.arange(9).reshape(3, 3)
print(a[1, 1])  # Valor de la segunda fila y la primera columna
# 4

# Tomar 1 fila
print(a[1, :])  # Tomo la segunda fila
# [3 4 5]

# Tomar 1 Columna
print(a[:, 1]) # Tomo la segunda columna
# [1 4 7]

# Memoria
m = np.arange(10)
x = m

np.shares_memory(m, x)
# Funcion para comprobar si dos valores comparten memoria
# True

# Solucion
m = np.arange(10)
x = m.copy()

np.shares_memory(m, x)
# False
