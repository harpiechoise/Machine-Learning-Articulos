import pandas as pd
import numpy as np
# 24 Filas
data = {'A': 'uno uno dos tres'.split(' ') * 6,
        'B': 'A B C'.split(' ') * 8,
        'C': 'Hola adios Como Estas Adios Estas'.split(' ') * 4,
        'D': np.random.randint(0, 10, 24),
        'E': np.random.randn(24),
        'F': pd.date_range("10/11/2011", periods=24)}

pd.set_option('max_rows', 4, 'max_columns', 20)  # Opciones de print
df = pd.DataFrame(data)

df
#        A  B      C  D         E          F
# 0    uno  A   Hola  0  0.336044 2011-10-11
# 1    uno  B  adios  9  0.435507 2011-10-12
# ..   ... ..    ... ..       ...        ...
# 22   dos  B  Adios  6 -0.048364 2011-11-02
# 23  tres  C  Estas  2  1.792238 2011-11-03

# [24 rows x 6 columns]

# Crear tabla pivote
pt = pd.pivot_table(df, values='E', index=['A', 'B'], columns='C')
pt
# C        Adios      Como     Estas      Hola     adios
# A   B                                                 
# dos A      NaN       NaN       NaN -0.073279       NaN
#     B  0.22452       NaN       NaN       NaN       NaN
# ...        ...       ...       ...       ...       ...
# uno B -0.15360       NaN       NaN       NaN  0.563443
#     C      NaN -0.085424 -1.289704       NaN       NaN

pt = pd.pivot_table(df, values='E', index=['A', 'B'], columns='C', aggfunc=np.sum)
pt
# C         Adios      Como     Estas      Hola     adios
# A   B                                                  
# dos A       NaN       NaN       NaN -0.146557       NaN
#     B  0.449041       NaN       NaN       NaN       NaN
# ...         ...       ...       ...       ...       ...
# uno B -0.307201       NaN       NaN       NaN  1.126886
#     C       NaN -0.170849 -2.579407       NaN       NaN

print(pt.to_string())
# C          Adios      Como     Estas      Hola     adios
# A    B                                                  
# dos  A       NaN       NaN       NaN -0.146557       NaN
#      B  0.449041       NaN       NaN       NaN       NaN
#      C       NaN  2.108767       NaN       NaN       NaN
# tres A       NaN       NaN  0.042156       NaN       NaN
#      B       NaN       NaN       NaN       NaN  1.228165
#      C       NaN       NaN  1.147061       NaN       NaN
# uno  A       NaN       NaN -2.790387  0.549069       NaN
#      B -0.307201       NaN       NaN       NaN  1.126886
#      C       NaN -0.170849 -2.579407       NaN       NaN

pd.crosstab(df.A, df.B)
# B     A  B  C
# A            
# dos   2  2  2
# tres  2  2  2
# uno   4  4  4

pd.crosstab(df.A, df.B, normalize=True)
# B            A         B         C
# A                                 
# dos   0.083333  0.083333  0.083333
# tres  0.083333  0.083333  0.083333
# uno   0.166667  0.166667  0.166667