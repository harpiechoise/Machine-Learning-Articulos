import numpy as np
import pandas as pd

aleatorio = np.random.randint(low=20, high=100, size=[20, ])
# Un vector de 20 valores aleatorios en una dimension
nombre = np.random.choice(['Jaime', 'Sebastian', 'Maximo', 'Claudio'], 20)
# Un vector de 20 valores aleatorios tomados entre los nombres de mi vista
numero = np.random.choice([10, 11, 13, 45, 8, 2], 20)
# Un vector de 20 valores aleatorios tomados entre los numeros de mi lista
# Todos deben tener la misma cantidad de valores
a = list(zip(aleatorio, nombre, numero))
# Pongo mis valores en una lista de tuplas
# Ejemplo
print(list(zip(['Hola', 'Adios'], [1, 2])))
# [('Hola', 1), ('Adios', 2)]

df = pd.DataFrame(data=a, columns=['Aleatorio', 'Nombre', 'Numero'])
print(df.head())  # Primeros 5 valores del Dataframe
#    Aleatorio     Nombre  Numero
# 0         67     Maximo      13
# 1         76    Claudio      13
# 2         62  Sebastian      10
# 3         80     Maximo       2
# 4         91    Claudio       8

print(type(df))  # <class 'pandas.core.frame.DataFrame'>
