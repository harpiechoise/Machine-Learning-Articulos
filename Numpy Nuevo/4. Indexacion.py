import numpy as np  # Importamos numpy bajo el seudonimo

a = np.arange(10) + 50  # Creamos un rango y le sumamos 50
print(a[2])   # Si quiero acceder al tercer elemento

print(a[-2])  # Si quiero el penultimo valor de mi Array
# 58

# Seleccionar un rango de elementos
print(a[2:5])   # Seleccionar desde tercer elemento al sexto elemento
# [52 53 54]

# Con paso
print(a[0::2])  # [50 52 54 56 58]
# Ir del primer elemento al ultimo con una distancia de 2

print(a[:: -1])  # Invertir todos los elementos
# [59 58 57 56 55 54 53 52 51 50]


b = np.fromfunction(lambda x, y: x * y + 5, (3, 5), dtype=int)
# Matriz de 3x5 a partir de una funcion
print(b)
# [[ 5  5  5  5  5]
#  [ 5  6  7  8  9]
#  [ 5  7  9 11 13]]
print(b[1][3])  # Acceder al tercer elemento del segundo array
# 8
# Metodo Optimo
print(b[1, 3])  # Acceder al tercer elemento del segundo array
# 8

print(b[:5, 1])  # Cada valor de la columas de b
# [5 6 7]

# Version Optima
print(b[:, 1])
# [5 6 7]

print(b[1, ])  # Seleccionar una fila
# [5 6 7 8 9]

print(b[-1, ])  # Ultima fila

# Recorrer todos los valores de una Array multidimensional
for i in a.flat:
    print(i)
# 50
# 51
# 52
# 53
# 54
# 55
# 56
# 57
# 58
# 59

# Filtrar arrays
print(a[a > 55])  # Valores mayores a 55
# [56 57 58 59]

print(a[(a > 55) | (a == 50)])  # Operaciones de bits
# [50 56 57 58 59]

a = np.floor(10 * np.random.random((3, 4)))
# Array de 3x4 de numeros aleatorios
print(a)
# [[3. 5. 8. 9.]
#  [5. 5. 8. 0.]
#  [1. 0. 7. 6.]]
print(len(a.flat))
# 12
print(a.shape)  # (3, 4)

# Array aplanada
print(a.ravel())
# [3. 5. 8. 9. 5. 5. 8. 0. 1. 0. 7. 6.]

# Reshape
print(a.reshape(6, 2))
# [[3. 5.]
#  [8. 9.]
#  [5. 5.]
#  [8. 0.]
#  [1. 0.]
#  [7. 6.]]

print(a.T)  # Tranpuesta
# [[3. 5. 1.]
#  [5. 5. 0.]
#  [8. 8. 7.]
#  [9. 0. 6.]]
print(a.shape)  # (3, 4)
print(a.T.shape)  # (4, 3)

# Automatico
print(a.reshape(3, -1))
print(a.shape)
# (3, 4)

a = np.arange(60)
print(a[[10, 11, 12]])  # Buscamos 3 indices
# [10 11 12]
a[4] = 1  # Reasignamos el quinto elemento
print(a[:10])
# [0 1 2 3 1 5 6 7 8 9]
a[[1, 3, 7]] = 1  # Reasignamos un valor para el segundo cuarto y octavo valor
print(a[:10])  # [0 1 2 1 4 5 6 1 8 9]

# Argmax
a = np.array([1, 1, 1, 10])
print(a.argmax())  # Posicion de mi valor maximo
# 3
# Indice 3 de mi array
