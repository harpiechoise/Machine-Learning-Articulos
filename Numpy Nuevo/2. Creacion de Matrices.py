import numpy as np  # Importamos numpy bajo seudonimo

a = np.array(1, 2, 3)    # Esto está mal
a = np.array([1, 2, 3])  # Mi funcion recibe una lista como parámetro

a = np.array([1, 2, 3])
a.dtype     # dtype('int64')
a.itemsize  # 8

a = np.array([1., 2., 3.])  # Le pasaremos valores decimales
a.dtype     # dtype('float64')
a.itemsize  # 8

a = np.array([1, 'a', "Hola"])  # Esto no debemos hacer esto
a.dtype     # dtype('<U21')
a.itemsize  # 84

# Tipo de dato en la definicion
a = np.array([1, 2, 3], dtype='short')
a.dtype     # dtype('int16')
a.itemsize  # 2

# Tipo de dato luego de la definicion
a = a.astype('single')
a.dtype      # dtype('float32')
a.itemsize   # 4

a = a.astype('complex')
print(a)
# [1.+0.j 2.+0.j 3.+0.j]

a.dtype     # dtype('complex128')
a.itemsize  # 16
