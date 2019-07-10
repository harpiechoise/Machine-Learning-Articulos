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

# Asignar una fila
df.iloc[1] = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
print(df)
#             A          B         C          D
# 2019-02-27  0   0.671448  0.161066  0.0596664
# 2019-02-28  1          2         3          4
# 2019-03-01  2   0.261184  0.885155   0.660747
# 2019-03-02  3   0.700732  0.935873   0.901624
# 2019-03-03  4   0.585571  0.983047  0.0620701
# 2019-03-04  5  0.0680889  0.737237   0.233875
# 2019-03-05  6   0.493405  0.226257   0.809233
# 2019-03-06  7   0.877922  0.786466   0.182065

# Slices
# Series
s[:2]  # Primeros 2 Elementos
# 2019-02-27    0.686824
# 2019-02-28    0.868448
# Freq: D, Name: A, dtype: float64

s[::2]  # Todos los elementos con paso 2
# 2019-02-27    0.686824
# 2019-03-01    0.199276
# 2019-03-03    0.805328
# 2019-03-05    0.006065
# Freq: 2D, Name: A, dtype: float64

s[::-1]  # Reversa de indices
# 2019-03-06    0.764515
# 2019-03-05    0.006065
# 2019-03-04    0.120355
# 2019-03-03    0.805328
# 2019-03-02    0.966972
# 2019-03-01    0.199276
# 2019-02-28    0.868448
# 2019-02-27    0.686824
# Freq: -1D, Name: A, dtype: float64

s[5::-1]  # ultimos 6 elementos al revez
# 2019-03-04    0.120355
# 2019-03-03    0.805328
# 2019-03-02    0.966972
# 2019-03-01    0.199276
# 2019-02-28    0.868448
# 2019-02-27    0.686824
# Freq: -1D, Name: A, dtype: float64

s2 = s.copy()  # Pasa lo mismo que numpy con la memoria
s2[:5] = 0
print(s2)
# 2019-02-27    0.000000
# 2019-02-28    0.000000
# 2019-03-01    0.000000
# 2019-03-02    0.000000
# 2019-03-03    0.000000
# 2019-03-04    0.120355
# 2019-03-05    0.006065
# 2019-03-06    0.764515
# Freq: D, Name: A, dtype: float64

# Dataframe
df[:3]  # Primeros 3 elementos
#             A         B         C          D
# 2019-02-27  0  0.671448  0.161066  0.0596664
# 2019-02-28  1         2         3          4
# 2019-03-01  2  0.261184  0.885155   0.660747

df[2::-1]  # Ultimos 3 elementos al revez
#             A         B         C          D
# 2019-03-01  2  0.261184  0.885155   0.660747
# 2019-02-28  1         2         3          4
# 2019-02-27  0  0.671448  0.161066  0.0596664-

# Advertencia
df.loc[2:3]  # No se pueden usar Slice con loc
# TypeError: cannot do slice indexing on

# Anot3
s1 = pd.Series(np.random.randn(6), index=list('abcdef'))
print(s1[3:])
# d   -0.047107
# e   -0.180345
# f    0.334778
# dtype: float64

s1.loc['d':]
# d   -0.047107
# e   -0.180345
# f    0.334778
# dtype: float64

s1.loc['b']
# 0.8256215434880477

# Seleccionar filas del dataframe
df.index = list('abcedfgh')  # Reasignar indice
df.loc[['a', 'e', 'f'], :]  # Todas las columnas de los indices a e f
#    A          B         C          D
# a  0   0.671448  0.161066  0.0596664
# e  3   0.700732  0.935873   0.901624
# f  5  0.0680889  0.737237   0.233875

df.loc['a':'c', 'A':'B']  # Filas: a hasta c, columnas: 'A' hasta 'B'
#    A         B
# a  0  0.671448
# b  1         2
# c  2  0.261184

df.loc['a']
# A            0
# B     0.671448
# C     0.161066
# D    0.0596664
# Name: a, dtype: object

# Arrays de booleanos
df.loc['a'] > 0.1
# Selecciona todas las columnas donde a sea mayor a 0.1
# A    False
# B     True
# C     True
# D    False
# Name: a, dtype: bool

df.loc[:, df.loc['a'] > 0.5]  # Queries
# a  0.671448
# b         2

df.loc['a', 'A']  # Indice a de la columna A
# 0

# Con indices
s1 = pd.Series(np.random.randint(5), index=list(range(0, 10, 2)))
print(s1)
# 0    2
# 2    2
# 4    2
# 6    2
# 8    2
# dtype: int64

s1.iloc[:3]  # Primeros 3 elementos de una serie
# 0    2
# 2    2
# 4    2
# dtype: int64

df.iloc[:3]  # Primeros 3 elementos de un dataframe
#    A         B         C          D
# a  0  0.671448  0.161066  0.0596664
# b  1         2         3          4
# c  2  0.261184  0.885155   0.660747

df.iloc[:3, :2]  # Primeras 3 filas y primeras 2 columnas
#    A         B
# a  0  0.671448
# b  1         2
# c  2  0.261184

df.iloc[[1, 4, 5], [1, 2]]  # Segundo, Quito, Sexto elemento
# De segunda y tercera columna

#            B         C
# b          2         3
# d   0.585571  0.983047
# f  0.0680889  0.737237

df.iloc[1:3, :]  # Todas las columnas del segundo al cuarto indice
#    A         B         C         D
# b  1         2         3         4
# c  2  0.261184  0.885155  0.660747

df.head().iloc[:, 1:3]  # Todos los indices
# De la segunda a cuarta columna

#           B         C
# a  0.671448  0.161066
# b         2         3
# c  0.261184  0.885155
# e  0.700732  0.935873
# d  0.585571  0.983047

# Querys
# SQL
# SELECT FROM df WHERE B>1
df.loc[lambda df: df.B > 1, :]
#    A  B  C  D
# b  1  2  3  4

# SQL
# SELECT A, B FROM df
df.loc[:, lambda df: ['A', 'B']]
#    A          B
# a  0   0.671448
# b  1          2
# c  2   0.261184
# e  3   0.700732
# d  4   0.585571
# f  5  0.0680889
# g  6   0.493405
# h  7   0.877922

# SELECT A, B FROM df
df.iloc[:, lambda df: [0, 1]]
#    A          B
# a  0   0.671448
# b  1          2
# c  2   0.261184
# e  3   0.700732
# d  4   0.585571
# f  5  0.0680889
# g  6   0.493405
# h  7   0.877922

# SELECT A FROM df
df[lambda df: df.columns[0]]
# a    0
# b    1
# c    2
# e    3
# d    4
# f    5
# g    6
# h    7
