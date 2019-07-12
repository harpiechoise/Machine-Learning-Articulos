import pandas as pd
from pandas.api.types import CategoricalDtype
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
