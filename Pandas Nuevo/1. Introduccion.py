import pandas as pd  # Seudonimo de pandas

#Series
a = pd.Series([1, 2, 3])  # Objeto Series

print(type(a)) # <class 'pandas.core.series.Series'>
print(a)
# 0    1
# 1    2
# 2    3
# dtype: int64

b = pd.Series([[1, 2, 3], [1,2,3]])  # No es como Numpy
print(b)
# 0    [1, 2, 3]
# 1    [1, 2, 3]
# dtype: object

# Cualquier Tupla puede ser convertida a una serie
b = ('AA', '2012', 100, 10.2)  # Definimos una Tupla
b = pd.Series(b)  # La convertimos en una serie
print(b)
# 0      AA
# 1    2012
# 2     100
# 3    10.2
# dtype: object

# Diccionario
b = {'A': 2, 'B': 6, 'C': 7}
b = pd.Series(b)
print(b)
# A    2
# B    6
# C    7
# dtype: int64

