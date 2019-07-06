import numpy as np
import pandas as pd

aleatorio = np.random.randint(low=20, high=100, size=[20, ])
nombre = np.random.choice(['Jaime', 'Sebastian', 'Maximo', 'Claudio'], 20)
numero = np.random.choice([10, 11, 13, 45, 8, 2], 20)
df = pd.DataFrame({'Aleatorio': aleatorio, 'Nombre': nombre, 'Numero': numero})

# Head: 5 Primeros Valores del DataFrame
print(df.head())
#    Aleatorio     Nombre  Numero
# 0         67     Maximo      13
# 1         76    Claudio      13
# 2         62  Sebastian      10
# 3         80     Maximo       2
# 4         91    Claudio       8

# Como parametro recibe el numero de valores
print(df.head(2))  # 2 Primeros Valores del Dataframe
#    Aleatorio   Nombre  Numero
# 0         67   Maximo      13
# 1         76  Claudio      13

# Tail: Utimos 5 Valores del DataFrame
print(df.tail())
#    Aleatorio     Nombre  Numero
# 15         39    Claudio       2
# 16         90      Jaime      45
# 17         39     Maximo       8
# 18         48  Sebastian      45
# 19         92      Jaime      13

# Recibe como parametro el numero de valores a mostrar
print(df.tail(1))  # Ultimo valor del DataFrame
#     Aleatorio Nombre  Numero
# 19         92  Jaime      13

# Shape: Muestra la forma del dataframes (filas, columnas)
print(df.shape)
# (20, 3)

# Columns: Muestra el nombre de las columnas del DataFrame
print(df.columns)
# Index(['Aleatorio', 'Nombre', 'Numero'], dtype='object')

# Seleccionar Columnas
# Metodo 1
print(df.Nombre[:3])
# 0       Maximo
# 1      Claudio
# 2    Sebastian
# Name: Nombre, dtype: object

print(type(df.Nombre))  # <class 'pandas.core.series.Series'>

# Metodo 2
print(df['Nombre'][:3])
# 0       Maximo
# 1      Claudio
# 2    Sebastian
# Name: Nombre, dtype: object
print(df['Numero'].describe())
# Describe: Devuelve distintos calculos estadistcos sobre la columna
# Estos valores son count: El numero de valores
# mean: El promedio de estos valores
# std: Desviacion Standar de mis datos
# min: Valor Minimo
# Porcentaje de la suma de mis datos
# max: Valor Maximo
# Name: Nombre de la Columna
# dtype: Siempre sera float64.
# No se refiere al tipo de dato te la columna.
# Sino del Describe en si

# count    20.000000
# mean     16.750000
# std      14.824855
# min       2.000000
# 25%       9.500000
# 50%      11.000000
# 75%      13.000000
# max      45.000000
# Name: Numero, dtype: float64

# Info: Nos da informacion sobre el dataset
df.info()
# Range index: Cuantas filas tengo en mi DataFrame y en que rango estan 0 al x
# Data columns: Nos dice que cantidad de columnas tenemos
# Informacion de las columnas
#    Nombre de la columna: Numero
#     Cantidad de valores: 20
#     Si hay valores nulos: non-null
#     Tipo de datos: int64
# dtypes: Nos dice cuantos tipos de datos y
# que cantidad de cada uno tengo en cada columna
# Ejemplo: dtypes: int64(2) -> Hay dos columnas de Enteros de 64 bits
# Memory usage: Nos da el peso del dataframe en la memoria RAM

# RangeIndex: 20 entries, 0 to 19
# Data columns (total 3 columns):
# Aleatorio    20 non-null int64
# Nombre       20 non-null object
# Numero       20 non-null int64
# dtypes: int64(2), object(1)
# memory usage: 560.0+ bytes

# Pasar de un dataframe a una Matriz de Numpy
print(df.values[:2])
# [[67 'Maximo' 13]
# [76 'Claudio' 13]]
print(type(df.values))  # <class 'numpy.ndarray'>
