import numpy as np
import pandas as pd  # Importamos pandas bajo el pseudonimo

# Rango de fechas 8 dias
fechas = pd.date_range('27/2/2019', periods=8)
# Creo un dataframe
df = pd.DataFrame(np.random.random((8, 4)), index=fechas,
                  columns=['A', 'B', 'C', 'D'])

# Extraigo una Serie del dataframe
s = df['A']
# Selecciono una de las fechas de mi lista
# Que defini como indice
print(s[fechas[1]])
# 0.9948947196784879

# Si queremos intercambiar columnas
df[['B', 'A']] = df[['A', 'B']]  # No se debe hacer aunque funcione
# Forma correcta
df.loc[:, ['B', 'A']] = df[['A', 'B']].to_numpy()
print(df[['A', 'B']])
#                    A         B
# 2019-02-27  0.319319  0.671448
# 2019-02-28  0.405093  0.960463
# 2019-03-01  0.542734  0.261184
# 2019-03-02  0.172890  0.700732
# 2019-03-03  0.665918  0.585571
# 2019-03-04  0.459141  0.068089
# 2019-03-05  0.447317  0.493405
# 2019-03-06  0.661500  0.877922
# Anotacion Location Choices

# Series
sa = pd.Series([1, 2, 3], index=list('abc'))
# Seleccionar Indices Rapido
print(sa.b)
# 2

# Seleccionar columnas de un dataset rapido
print(df.A)
# 2019-02-27    0.319319
# 2019-02-28    0.405093
# 2019-03-01    0.542734
# 2019-03-02    0.172890
# 2019-03-03    0.665918
# 2019-03-04    0.459141
# 2019-03-05    0.447317
# 2019-03-06    0.661500
# Freq: D, Name: A, dtype: float64

# Reasignar un indice
sa.a = 5
print(sa)
# a    5
# b    2
# c    3
# dtype: int64

# Solo si existe
df.A = list(range(len(df)))
print(df)
#             A         B         C         D
# 2019-02-27  0  0.671448  0.161066  0.059666
# 2019-02-28  1  0.960463  0.822715  0.814657
# 2019-03-01  2  0.261184  0.885155  0.660747
# 2019-03-02  3  0.700732  0.935873  0.901624
# 2019-03-03  4  0.585571  0.983047  0.062070
# 2019-03-04  5  0.068089  0.737237  0.233875
# 2019-03-05  6  0.493405  0.226257  0.809233
# 2019-03-06  7  0.877922  0.786466  0.182065

# Si no existe
df.X = list(range(len(df)))  # Lanza Error
#  Pandas doesn't allow columns to be created via a new attribute name
df['X'] = list(range(len(df)))  # Forma correcta 
