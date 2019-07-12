import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np
# Tipo de dato categorico
s = pd.Series(['a', 'b', 'c', 'd'], dtype='category')
s
# dtype: category
# Categories (4, object): [a, b, c, d]

# Asignando la categoria luego
df = pd.DataFrame({'A': list('abcd')})
df['B'] = df['A'].astype('category')
df
#    A  B
# 0  a  a
# 1  b  b
# 2  c  c
# 3  d  d

df.dtypes
# A      object
# B    category
# dtype: object

# Categorias como tipo de datos
raw_cat = pd.Categorical(list('abca'), categories=list('bcd'))
# Si no pasamos la categoria especifica lo rellena con NaN
raw_cat

# Integrando una columna de tipo categorico
df = pd.DataFrame({'A': list('abcd')})
df['B'] = raw_cat
df
#    A    B
# 0  a  NaN
# 1  b    b
# 2  c    c
# 3  d  NaN

# Se puede asignar cada columna de un dataframe
df = df.astype('category')
df.dtypes
# A    category
# B    category
# dtype: object

categoria_tipo = CategoricalDtype(categories=list('abcd'), ordered=True)
s = s.astype(categoria_tipo)
s
# 0    a
# 1    b
# 2    c
# 3    d
# dtype: category
# Categories (4, object): [a < b < c < d]

s[s > 'c']
# 3    d
# dtype: category
# Categories (4, object): [a < b < c < d]

s[s < 'd']
# 0    a
# 1    b
# 2    c
# dtype: category
# Categories (4, object): [a < b < c < d]

s1 = pd.Series(list('abcd'))
df = pd.DataFrame({'cat': s, 's': s1})
df
#   cat  s
# 0   a  a
# 1   b  b
# 2   c  c
# 3   d  d

df.describe()
#        cat  s
# count    4  4
# unique   4  4
# top      d  c
# freq     1  1

df['cat'].describe()
# count     4
# unique    4
# top       d
# freq      1
# Name: cat, dtype: object

s = pd.Series(list('aaaaabbbbbbccccccddddeee'), dtype='category')
s1 = pd.Series(np.random.randint(low=1, high=20, size=24))
s.unique()
# [a, b, c, d, e]
# Categories (5, object): [a, b, c, d, e]

df = pd.DataFrame({'A': s1, 'c': s})

df.c.cat.categories = [f'Grupo: {g}' for g in df.c.cat.categories]
df.head(2)
#     A         c
# 0  18  Grupo: a
# 1   7  Grupo: a

df = df.set_index([df.c, df.index], drop=True)
df.loc['Grupo: d']
#      A         c
# 17  18  Grupo: d
# 18  15  Grupo: d
# 19   8  Grupo: d
# 20  17  Grupo: d

s.cat.categories = [1, 1, 1, 1, 1]
# ValueError: Categorical categories must be unique

s.cat.categories = [1, 2, 3, np.nan, 5]
# ValueError: Categorial categories cannot be null
