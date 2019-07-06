import pandas as pd  # Importamos pandas bajo el sudonimo pd

# Tipo basico de datos de Pandas: Series
a = pd.Series([1, 2, 3, 4, 5])  # Recibe como parámetro una lista de elementos
# Datos Deben Ser Homogeneos
print(a)
# 0    1
# 1    2
# 2    3
# 3    4
# 4    5
# dtype: int64

print(type(a))  # <class 'pandas.core.series.Series'>

print(a[3])  # Aceder al cuarto valor
# 4

print(a[1:3])  # Del indice 1 al 3
# 1    2
# 2    3
# dtype: int64

print(a[[4, 3, 1]])  # Seleccionar Varios indices
# 4    5
# 3    4
# 1    2
# dtype: int64

# Object Data Typeç
a = pd.Series(['a', 'b', 'c'])  # Le paso una lista de caracteres
print(a)
# 0    a
# 1    b
# 2    c
# dtype: object
