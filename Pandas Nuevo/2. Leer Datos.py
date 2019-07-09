import pandas as pd  # Importamos pandas bajo el seudonimo

# Leer datos en CSV
df = pd.read_csv('iris.csv')  # Abrir un CSV con headers
df.head(2)  # Primeros 2 valores del dataset
#    sepal length in cm   sepal width in cm ...
# 0                 5.1                 3.5
# 1                 4.9                 3.0

df.tail(2)  # Ultimos 2 valores del dataset
#      sepal length in cm   sepal width in cm ...
# 145                 6.7                 3.0
# 146                 6.3                 2.5

df = pd.read_csv('iris', encoding='utf-8')  # Leer un dataframe con encoding

pd.set_option('max_rows', 5, 'max_columns', 2)  # Opciones de print
print(df)
#      sepal length in cm   sepal width in cm   petal length in cm  ....
# 0                   5.1                 3.5                  1.4
# 1                   4.9                 3.0                  1.4
# ..                  ...                 ...                  ...
# 148                 6.2                 3.4                  5.4
# 149                 5.9                 3.0                  5.1

print(len(df))  # Cantidad de filas
# 150

# Leer un CSV sin headers
df = pd.read_csv("iris1.csv", header=None)
print(df)
#        0    1    2    3               4
# 0    5.1  3.5  1.4  0.2     Iris-setosa
# 1    4.9  3.0  1.4  0.2     Iris-setosa
# ..   ...  ...  ...  ...             ...
# 148  6.2  3.4  5.4  2.3  Iris-virginica
# 149  5.9  3.0  5.1  1.8  Iris-virginica

df = pd.read_json('Iris.json')
print(df)

#               class  ...  sepal width in cm 
# 0       Iris-setosa  ...                3.5
# 1       Iris-setosa  ...                3.0
# ..              ...  ...                ...
# 148  Iris-virginica  ...                3.4
# 149  Iris-virginica  ...                3.0

# [150 rows x 5 columns]

# Webscraping
# pip install lxml
url = pd.read_html('https://www.rexegg.com/regex-quickstart.html')
df = url[0]
df.head(2)
#   Character                                           Legend    Example  \
# 0        \d               Most engines: one digitfrom 0 to 9  file_\d\d
# 1        \d  .NET, Python 3: one Unicode digit in any script  file_\d\d
