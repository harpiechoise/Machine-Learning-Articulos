import pandas as pd  # Importamos pandas bajo el seudonimo

# Leer datos en CSV
df = pd.read_csv('iris.csv')  # Abrir un CSV con headers
df.head()  # Primeros 5 valores del dataset
#    sepal length in cm   sepal width in cm ...
# 0                 5.1                 3.5
# 1                 4.9                 3.0
# 2                 4.7                 3.2
# 3                 4.6                 3.1
# 4                 5.0                 3.6
df.tail()  # Ultimos 5 valores del dataset
#      sepal length in cm   sepal width in cm ...
# 145                 6.7                 3.0
# 146                 6.3                 2.5
# 147                 6.5                 3.0
# 148                 6.2                 3.4
# 149                 5.9                 3.0

df = pd.read_csv('iris', encoding='utf-8')  # Leer un dataframe con encoding

pd.set_option('max_rows', 5, 'max_columns', 5)  # Opciones de print
print(df)
#      sepal length in cm   sepal width in cm   petal length in cm  ....
# 0                   5.1                 3.5                  1.4
# 1                   4.9                 3.0                  1.4
# ..                  ...                 ...                  ...
# 148                 6.2                 3.4                  5.4
# 149                 5.9                 3.0                  5.1
