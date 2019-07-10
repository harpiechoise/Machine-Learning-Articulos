import pandas as pd

# Concatenacion
a = pd.DataFrame({'Numero': [60, 30],
                  'Animal': ['Panda', 'Leon']})

b = pd.DataFrame({'Peso': [600, 120],
                  'Patas': [4, 4]})

# Concatenar en filas
c = pd.concat([a, b], axis=0)  # Concatenar en el eje de las filas