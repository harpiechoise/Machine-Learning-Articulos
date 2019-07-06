import numpy as np  # Importamos numpy

a = np.arange(25).reshape(5, 5)  # Hacemos una matriz de 5 x 5
print(a > 10)
# [[False False False False False]
#  [False False False False False]
#  [False  True  True  True  True]
#  [ True  True  True  True  True]
#  [ True  True  True  True  True]]

# Pasando esta matriz de booleanos a numpy
print(a[a > 10])
# [11 12 13 14 15 16 17 18 19 20 21 22 23 24]
# Condiciones multiples
print(a[(a > 10) & (a < 20)])
# [11 12 13 14 15 16 17 18 19]

# Transpuesta de la Matriz
a = np.arange(15).reshape(5, 3)
print(a.T)
# [[ 0  3  6  9 12]
#  [ 1  4  7 10 13]
#  [ 2  5  8 11 14]]
print(a.T.shape)
# (3, 5)

# VStack
a = np.arange(1, 7).reshape(3, 2)
b = np.arange(7, 13).reshape(3, 2)
print(np.vstack((a, b)))  # Juntar las filas de A y B
# [[ 1  2]
#  [ 3  4]
#  [ 5  6]
#  [ 7  8]
#  [ 9 10]
#  [11 12]]

# HStack
print(np.hstack((a, b)))  # Juntar las columnas de A y B
# [[ 1  2  7  8]
#  [ 3  4  9 10]
#  [ 5  6 11 12]]

# Seno
print(np.sin(a))  # Sacar el seno de todos mis valores
# [[ 0.84147098  0.90929743]
#  [ 0.14112001 -0.7568025 ]
#  [-0.95892427 -0.2794155 ]]

# Coseno
print(np.cos(a))
# [[ 0.54030231 -0.41614684]
#  [-0.9899925  -0.65364362]
#  [ 0.28366219  0.96017029]]

# Tangente
print(np.tan(a))
# [[ 1.55740772 -2.18503986]
#  [-0.14254654  1.15782128]
#  [-3.38051501 -0.29100619]]

# Opreaciones Arco o Inverso igual estan
print(np.arctan(a))
# [[0.78539816 1.10714872]
# [1.24904577 1.32581766]
# [1.37340077 1.40564765]]

# Exponencial
print(np.exp(a))
# [[  2.71828183   7.3890561 ]
#  [ 20.08553692  54.59815003]
#  [148.4131591  403.42879349]]

# Sumatoria
print(np.sum(a))
# 21

# Media
print(np.mean(a))
# 3.5

# Desviacion Standar
print(np.std(a))
# 1.707825127659933

a = np.random.random((2, 2))

# Determinante
print(np.linalg.det(a))
# -0.024097224859192783

# Inversa de la matriz
print(np.linalg.inv(a))
# [[ -0.42041879  24.88464405]
#  [  2.29855941 -37.34437794]]

# Valor Propio de una Matriz
print(np.linalg.eig(a))
# array([ 0.93577781, -0.02575101]),
# array([[ 0.9982145 , -0.54370042],
#        [ 0.05973121,  0.83927937]])

# Producto Punto
a = np.random.random((3, 1))
b = a.T
print(np.dot(a, b))
# [[0.34587335 0.52728665 0.49425156]
# [0.52728665 0.80385265 0.7534904 ]
# [0.49425156 0.7534904  0.7062834 ]]

# Suma de columnas
a = np.random.random((2, 10)) * 5
print(a.sum(axis=1))
# [20.13862972 36.26166099]


a = np.random.random(10)

# Maximo
print(a.max())  # El valor maximo de la matriz
# 0.8133470649818069

# Posicion del numero mas grande
print(a.argmax())  # 4
print(a[4])  # 0.8133470649818069
