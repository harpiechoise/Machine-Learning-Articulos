import numpy  # Importamos numpy para usarlo en nuestro codigo

import numpy as np  # Importamos con un alias

a = numpy.array([1, 2, 3])  # Creamos una array de numpy
print(a)  # [1 2 3]

# Bajo el alias
a = np.array([1, 2, 3])  # Creamos una array de numpy
print(a)  # [1 2 3]

a = np.array(['a', 1, 2, 'b'])  # Está mal

print(type(a))  # <class 'numpy.ndarray'>
