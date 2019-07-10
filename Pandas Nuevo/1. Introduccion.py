import pandas as pd  # Seudonimo de pandas

# Tipo de dato Serie
# Series
a = pd.Series([1, 2, 3])  # Objeto Series

print(type(a))  # <class 'pandas.core.series.Series'>
print(a)
# 0    1
# 1    2
# 2    3
# dtype: int64

b = pd.Series([[1, 2, 3], [1, 2, 3]])  # No es como Numpy
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
b = {'A': 2, 'B': 6, 'C': 7}  # Defino el Diccionario
b = pd.Series(b)  # Lo convierto a Serie
print(b)
# A    2
# B    6
# C    7
# dtype: int64

# Definir Indices Personalizados
b = [1, 10, 5]
b = pd.Series(b, index=['X', 'Y', 'Z'])  # Definir un Array con Indices

print(b)

print(b['X'])  # 1

# Utilidades de definir un Array con indices
# Hacer un Reporte
b = ['Tesla', 'Model S', 59100]
b = pd.Series(b, index=['Marca', 'Modelo', 'Precio'])
print(b)
# Marca       Tesla
# Modelo    Model S
# Precio      59100
# dtype: object

# Advertencia
b = {'I': 1, 'A': 2, 'C': 3}
b = pd.Series(b, index=['S', 'I', 'J'])  # Esto causa errores
print(b)
# S    NaN
# I    1.0
# J    NaN
# dtype: float64

# Indexacion de similar a numpy
b = {'Nombre': 'La nada', 'Fecha': 0, 'Valor': 0}
b = pd.Series(b)
print(b[['Nombre', 'Valor']])

# Estructura 2 Dataframe
# Desde un Diccionario
data = {'Nombre': ['Franco', 'Francisco', 'Lorena'],
        'Pedido': ['Panqueques', 'Bebida', 'Papas'],
        'Mesa': [5, 3, 4]}
df = pd.DataFrame(data)
print(type(df))  # <class 'pandas.core.frame.DataFrame'>

print(df)
#       Nombre      Pedido  Mesa
# 0     Franco  Panqueques     5
# 1  Francisco      Bebida     3
# 2     Lorena       Papas     4

# Crear una columna
df['Algo'] = 'Por Definir'
print(df)
#       Nombre      Pedido  Mesa         Algo
# 0     Franco  Panqueques     5  Por Definir
# 1  Francisco      Bebida     3  Por Definir
# 2     Lorena       Papas     4  Por Definir

# Modificar el indice
df.index = ['uno', 'dos', 'tres']
print(df)
#          Nombre      Pedido  Mesa         Algo
# uno      Franco  Panqueques     5  Por Definir
# dos   Francisco      Bebida     3  Por Definir
# tres     Lorena       Papas     4  Por Definir

# Selecionar una Columna
df['Nombre']
# 0       Franco
# 1    Francisco
# 2       Lorena
# Name: Nombre, dtype: object

# Seleccionar multiples Columnas
df[['Nombre', 'Mesa']]
#       Nombre  Mesa
# 0     Franco     5
# 1  Francisco     3
# 2     Lorena     4

# Seleccionar una fila con el nombre de las columnas
type(df.ix['uno'])
# Nombre        Franco
# Pedido    Panqueques
# Mesa               5
# Name: 0, dtype: object

# Acediendo a un elemento especifico de una fila del
# Dataframe
df.ix['uno', 'Pedido']
# 'Panqueques'

# Borrar una Columna
print(df.drop(['Mesa'], axis=1))
# Borrar instancia en memoria
del df['Mesa']

print(df)
#          Nombre      Pedido         Algo
# uno      Franco  Panqueques  Por Definir
# dos   Francisco      Bebida  Por Definir
# tres     Lorena       Papas  Por Definir

