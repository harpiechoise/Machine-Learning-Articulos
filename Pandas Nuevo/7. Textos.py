import pandas as pd
import numpy as np
# Series
s = pd.Series(['A', 'B', 'C', 'Casa', 'Vaca', np.nan, 'CABA', 'perro', 'gato'])
# Llevamos las cadenas a minusculas
s.str.lower()
# 0        a
# 1        b
# 2        c
# 3     casa
# 4     vaca
# 5      NaN
# 6     caba
# 7    perro
# 8     gato
# dtype: object

# Llevamos las cadenas a mayusculas
s.str.upper()
# 0        A
# 1        B
# 2        C
# 3     CASA
# 4     VACA
# 5      NaN
# 6     CABA
# 7    PERRO
# 8     GATO
# dtype: object

index = pd.Index(['    Jaime', 'Laura   ', '  Lorena  ', 'frank'])
# Eliminar espacios
index.str.strip()
# Index(['Jaime', 'Laura', 'Lorena', 'frank'], dtype='object')

# Eliminamos espacios a la derecha
index.str.rstrip()
# Index(['    Jaime', 'Laura', '  Lorena', 'frank'], dtype='object')

# Eliminamos espacios a la izquierda
index.str.lstrip()
# Index(['Jaime', 'Laura   ', 'Lorena  ', 'frank'], dtype='object')

# Arreglar las columnas
df = pd.DataFrame(np.random.rand(3, 2),
                  columns=['   Columna A', '  Columna B  '],
                  index=range(3))

df
#       Columna A    Columna B
# 0      0.467699       0.172059
# 1      0.405944       0.924535
# 2      0.607172       0.128199

# Eliminar los espacios
df.columns.strip()

# Formateando las columnas
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
df
#    columna_a  columna_b
# 0   0.467699   0.172059
# 1   0.405944   0.924535
# 2   0.607172   0.128199


# Split
s2 = pd.Series(['a_b_c', 'c_d_e', np.nan, 'f_g_h'])
s2.str.split('_')
# 0    [a, b, c]
# 1    [c, d, e]
# 2          NaN
# 3    [f, g, h]
# dtype: object

# Accediendo a los indices de las listas
s2.str.split('_').str.get(1)
# 0      b
# 1      d
# 2    NaN
# 3      g
# dtype: object

s2.str.split('_').str[1]
# 0      b
# 1      d
# 2    NaN
# 3      g
# dtype: object

# Expandir las listas
s2.str.split('_', expand=True)
#      0    1    2
# 0    a    b    c
# 1    c    d    e
# 2  NaN  NaN  NaN
# 3    f    g    h

# Replace con regex
# Reemplazar las cadenas que tengan una C al comienzo
# O sean vaca
s.str.replace('^c|vaca', 'XX-XX', case=False)
# 0           A
# 1           B
# 2       XX-XX
# 3    XX-XXasa
# 4       XX-XX
# 5         NaN
# 6    XX-XXABA
# 7       perro
# 8        gato
# dtype: object

# Datos mal formateados
pesos = pd.Series(['$1000', '50', '-$100'])
pesos.str.replace(r'-\$', '-').str.replace('$', '')
# 0    1000
# 1      50
# 2    -100
# dtype: object

# Juntar cadenas
s = pd.Series(['a', 'b', 'c', 'd'])
s.str.cat(sep=' ')
# 'a b c d'

s = pd.Series(['a', 'b', np.nan, 'd'])
s.str.cat(sep=', ', na_rep='-')
# 'a, b, -, d'
