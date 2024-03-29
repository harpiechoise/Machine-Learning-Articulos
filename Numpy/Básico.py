# Importamos Numpy
import numpy
from timeit import timeit  # Utilidad para hacer pruebas de rendimiento
import numpy as np
# Crear una array de numpy
numpy.array([1, 2, 3])  # array([1, 2, 3])

# Reduccion de la importacion
# Linea: 4
np.array([1, 2, 3])  # array([1, 2, 3])

# Array de Numpy Anidada
b = np.array([[1, 2, 3], [1, 2, 3]])  # Matriz
# array([[1, 2, 3],
#        [1, 2, 3]])

# Forma de la matriz
print(b.shape)
# (2, 3) 2 Filas y 3 Columnas

# Datos Homogeneos (Del mismo tipo de dato
print(b.dtype)  # int64

# Numero de dimensiones
print(b.ndim)  # 2

# Tipo de dato Numpy Array
print(type(b))  # <class 'numpy.ndarray'>

# Rango de numpy
print(np.arange(10))  # [0 1 2 3 4 5 6 7 8 9]

# Prueba de rendimiento
# Python
n = 10000
timeP = timeit(lambda: [i ** 3 for i in range(n)], number=10000)

# Numpy
n_range = np.arange(n)
timeN = timeit(lambda: n_range**3, number=10000)

print(f'Tiempo que le tomó a Python: {timeP} segundos')
print(f'Tiempo que le tomó a Numpy: {timeN} segundos')

# Tiempo que le tomó a Python: 23.39795723399584 \
# segundos en hacer 10000 iteraciones

# Tiempo que le tomó a Numpy: 0.19095460099924821 \
# segundos en hacer 10000 iteraciones
