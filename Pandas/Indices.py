import numpy as np
import pandas as pd

aleatorio = np.random.randint(low=20, high=100, size=[20, ])
nombre = np.random.choice(['Jaime', 'Sebastian', 'Maximo', 'Claudio'], 20)
numero = np.random.choice([10, 11, 13, 45, 8, 2], 20)
df = pd.DataFrame({'Aleatorio': aleatorio, 'Nombre': nombre, 'Numero': numero})

# Cambiar el indice de un dataframe
df = df.set_index('Numero')
# Recibe como parametro la columna a definir como indice
print(df.head(2))  # Tomo los primeros dos elementos
# 11             67  Sebastian
# 10             23     Maximo
# Los indices fueron modificados

# Inplace:
# Si quiero asignar el indice
# Sin reasignar la variable
df.set_index('Aleatorio', inplace=True)  # El indice fue reemplazado
print(df.head(2))  # Primeros dos indices
# 81          Jaime      11
# 57         Maximo      10

# Ordenar el indice de forma descendente
df.sort_index(axis=0, ascending=False, inplace=True)
# Imagen de los Ejes
print(df.head(4))  # Mostramos los 4 primeros valores
#     Aleatorio     Nombre  Numero
# 19         38     Maximo       8
# 18         76  Sebastian      45
# 17         84  Sebastian       2
# 16         71  Sebastian      10

# Ordenar el indice de forma ascendente
df.sort_index(axis=0, ascending=True, inplace=True)
print(df.head(4))  # Mostramos los 4 primeros valores
#    Aleatorio     Nombre  Numero
# 0         47      Jaime      45
# 1         74      Jaime      13
# 2         50  Sebastian       8
# 3         26      Jaime      13

# Sacar una columna
df.drop('Numero', axis=1, inplace=True)  # Sacamos la columna Numero
print(df.head(2))  # Mostramos los dos primeros valores de la columna
# 96         Jaime
# 38         Jaime
