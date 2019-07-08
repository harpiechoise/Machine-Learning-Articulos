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

a = np.zeros((3, 3)) # Array 3x3
print(a)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

a = np.ones((3, 3), dtype='single') # Array 3x3 
print(a) 
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

a = np.empty((2, 5))  # Array 2x5
print(a)
# [[ 4.68083815e-310  8.12555790e-096  9.45869060e-154  3.32231745e+257
#    4.70106013e+180]
#  [ 2.14102784e+161  3.09100413e+169 -8.27789406e+016  1.45121267e-308
#    0.00000000e+000]

b = np.zeros_like(a)  # Copiar las dimensiones
print(b) 
# [[0. 0. 0. 0. 0.]
# [0. 0. 0. 0. 0.]]

b = np.ones_like(a)  # Copiar las dimensiones
print(b)
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

fn = lambda x, y: x ** y  # Defino mi funcion
a = np.fromfunction(fn, (5, 5), dtype='single')  # Llamo a mi funcion 
print(a)
# [[  1.   0.   0.   0.   0.]
#  [  1.   1.   1.   1.   1.]
#  [  1.   2.   4.   8.  16.]
#  [  1.   3.   9.  27.  81.]
#  [  1.   4.  16.  64. 256.]]

a = np.arange(10, 21)  # Rango del 1 al 20
print(a)  # [10 11 12 13 14 15 16 17 18 19 20]

a = np.arange(10, 21, 2)  # Rango del 1 al 20 con distancia 2
print(a)  # [10 12 14 16 18 20]

# Array Gigante
print(np.arange(100000))
# [    0     1     2 ... 99997 99998 99999]

#Cambiar las opciones de el metodo print 
np.set_printoptions(threshold=10)
print(np.arange(10))  # [0 1 2 3 4 5 6 7 8 9]
print(np.arange(11))  # [ 0  1  2 ...  8  9 10]
np.set_printoptions(threshold=1000) # Volver a la normalidad

# Matriz identidad
a = np.identity(3)  # Matriz de identidad de 3x3
print(a)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

#K-eye
a = np.eye(3, k=1)   # La muevo hacia arriba
print(a)
# [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

a = np.eye(3, k=-1)  # La muevo hacia abajo
print(a)
# [[0. 0. 0.]
#  [1. 0. 0.]
#  [0. 1. 0.]]


def pow(x, y):  # Creo una funcion
    "Elevar mi Array a un exponente"
    return x ** y


pow_vec = np.vectorize(pow)  # Vectorizo mi funcion
pow_vec(np.arange(10), 2)  # Le paso los dos argumentos a mi funcion
# array([ 0,  1,  4,  9, 16, 25, 36, 49, 64, 81])

