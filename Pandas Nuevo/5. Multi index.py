import pandas as pd
# Crear un multi index desde tuplas
indices = [('Santiago', 2000), ('Santiago', 2010), 
         ('California', 2000), ('California', 2010),
         ('NewYork', 2000), ('New York', 2010)]
m_indice = pd.MultiIndex.from_tuples(indices)
df = pd.DataFrame([33871648, 37253956, 18976457, 19378102, 20851820, 25145561], columns=['Poblacion'],index=m_indice)
print(df)
#                  Poblacion
# Santiago   2000   33871648
#            2010   37253956
# California 2000   18976457
#            2010   19378102
# NewYork    2000   20851820
# New York   2010   25145561

df['Santiago']
m_indice
