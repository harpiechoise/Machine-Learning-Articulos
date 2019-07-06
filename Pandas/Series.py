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

# Rango de fechas
a = pd.date_range(start='01-07-2019', end='20-07-2019')
print(a)
# DatetimeIndex(['2019-01-07', '2019-01-08', '2019-01-09', '2019-01-10',
#                '2019-01-11', '2019-01-12', '2019-01-13', '2019-01-14',
#                '2019-01-15', '2019-01-16',
#                ...
#                '2019-07-11', '2019-07-12', '2019-07-13', '2019-07-14',
#                '2019-07-15', '2019-07-16', '2019-07-17', '2019-07-18',
#                '2019-07-19', '2019-07-20'],
#               dtype='datetime64[ns]', length=195, freq='D')
# Length = Cuantos valores tengo en mi Serie
# Freq = Cada cuanto quiero mi valor, en este caso en dias
# https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases