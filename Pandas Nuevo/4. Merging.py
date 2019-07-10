import pandas as pd

# Concatenacion
a = pd.DataFrame({'Numero': [60, 30],
                  'Animal': ['Panda', 'Leon']})

b = pd.DataFrame({'Peso': [600, 120],
                  'Patas': [4, 4]})

# Concatenar en filas
c = pd.concat([a, b], axis=0)  # Concatenar en el eje de las filas
print(c)
# Ignorar indice
c = pd.concat([a, b], axis=0, ignore_index=True)
print(c)
# Concatenacion en columnas
c = pd.concat([a, b], axis=1)
print(c)

# Merging
a = pd.DataFrame({'Ciudad': ['Santiago', 'La serena', 'Temuco'],
                   'Viento KM': [30, 60, 20]})

b = pd.DataFrame({'Ciudad': ['Santiago', 'La serena', 'Temuco'],
                  'Humedad': [60, 20, 30], 
                  'Direcion Viento': ['E', 'S', 'O']})

c = pd.merge(a, b, on='Ciudad')
print(c)