import numpy as np  # Importamos numpy bajo el seudonimo

a = np.arange(10) + 50  # Creamos un rango y le sumamos 50
print(a[2])  # Si quiero acceder al tercer elemento

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
