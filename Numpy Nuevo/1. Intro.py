import numpy  # Importamos numpy para usarlo en nuestro codigo

import numpy as np  # Importamos con un alias

a = numpy.array([1, 2, 3])  # Creamos una array de numpy
print(a)  # [1 2 3]

# Bajo el alias
a = np.array([1, 2, 3])  # Creamos una array de numpy
print(a)  # [1 2 3]

a = np.array(['a', 1, 2, 'b'])  # Está mal

# Tipo de dato
print(type(a))  # <class 'numpy.ndarray'>

# Array de dos dimensiones
a = np.array([[1, 2, 3], [1, 2, 3]])  # Array de dos dimensiones
print(a)
# [[1 2 3]
#  [1 2 3]]

print(a)
# [[1 2 3]
#  [1 2 3]]

a.shape     # (2, 3)
a.ndim      # 2
a.size      # 6
a.itemsize  # 8
a.dtype     # int64

# Calcular el tamaño en memoria de mi Array
print(f'Tamaño de mi array: {a.itemsize * a.size} bytes')
# Tamaño de mi array: 48 bytes
