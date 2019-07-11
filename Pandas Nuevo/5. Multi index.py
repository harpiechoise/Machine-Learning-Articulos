import pandas as pd
import numpy as np
# Crear un multi index desde tuplas
indices = [('Santiago', 2000), ('Santiago', 2010),
           ('California', 2000), ('California', 2010),
           ('New York', 2000), ('New York', 2010)]
m_indice = pd.MultiIndex.from_tuples(indices)
df = pd.DataFrame([33871648, 37253956, 18976457, 19378102, 20851820, 25145561],
                  columns=['Poblacion'], index=m_indice)
print(df)
#                 Poblacion
# Santiago   2000   33871648
#            2010   37253956
# California 2000   18976457
#            2010   19378102
# New York   2000   20851820
#            2010   25145561
# Seleccionar mas facil multiples grupos
df.loc['Santiago']
#       Poblacion
# 2000   33871648
# 2010   37253956
df.loc['Santiago', 2010]
# Poblacion    37253956
# Name: (Santiago, 2010), dtype: int64
m_indice = pd.MultiIndex.from_tuples([('Categoria 1', 'Primer Valor'), 
                                      ('Categoria 1', 'Segundo Valor'), 
                                      ('Categoria 1', 'Tercer Valor'), 
                                      ('Categoria 2', 'Primer Valor'), 
                                      ('Categoria 2', 'Segundo Valor'), 
                                      ('Categoria 2', 'Tercer Valor'),])
df = pd.DataFrame(np.random.randint(1, high=5, size=(6,4)), columns=list('abcd'), index=m_indice)
df
#                            a  b  c  d
# Categoria 1 Primer Valor   4  1  3  3
#             Segundo Valor  3  3  4  1
#             Tercer Valor   4  4  4  2
# Categoria 2 Primer Valor   4  4  4  3
#             Segundo Valor  4  3  4  3
#             Tercer Valor   2  1  4  3

df.loc['Categoria 1', 'a']
# Primer Valor     4
# Segundo Valor    3
# Tercer Valor     4
# Name: a, dtype: int64

df.loc[('Categoria 1', 'Tercer Valor'):('Categoria 2', 'Sengundo Valor')]
#                            a  b  c  d
# Categoria 1 Tercer Valor   4  4  4  2
# Categoria 2 Primer Valor   4  4  4  3
#             Segundo Valor  4  3  4  3

df.loc[('Categoria 1', 'Tercer Valor'): 'Categoria 2']
#                            a  b  c  d
# Categoria 1 Tercer Valor   4  4  4  2
# Categoria 2 Primer Valor   4  4  4  3
#             Segundo Valor  4  3  4  3
#             Tercer Valor   2  1  4  3


