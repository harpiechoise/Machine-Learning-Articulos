import pandas as pd
import numpy as np
# NaN como -Infinitos 
pd.options.mode.use_inf_as_na = True

# Creando un dataframe con nulos
df = pd.DataFrame(
                {
                    'Uno': np.random.choice([np.random.randint(low=1, high=20), np.nan], 5),
                    'Dos': np.random.choice([np.random.randint(low=1, high=20), np.nan], 5),
                    'Tres': np.random.choice([np.random.randint(low=1, high=20), np.nan], 5),
                    'Cuatro': np.random.choice([np.random.randint(low=1, high=20), np.nan], 5),
                    'Cinco': np.random.choice([np.random.randint(low=1, high=20), np.nan], 5)
                }
)

df
#     Uno   Dos  Tres  Cuatro  Cinco
# 0  12.0   NaN   5.0     NaN    NaN
# 1  12.0  16.0   NaN    10.0    NaN
# 2   NaN   NaN   NaN     NaN   13.0
# 3   NaN  16.0   NaN    10.0    NaN
# 4   NaN   NaN   5.0    10.0   13.0

# Filtrar nulos
pd.isna(df['Uno'])
# 0    False
# 1    False
# 2     True
# 3     True
# 4     True
# Name: Uno, dtype: bool

pd.notna(df['Dos'])
# 0    False
# 1     True
# 2    False
# 3     True
# 4    False
# Name: Dos, dtype: bool

df.isna()
#      Uno    Dos   Tres  Cuatro  Cinco
# 0  False   True  False    True   True
# 1  False  False   True   False   True
# 2   True   True   True    True  False
# 3   True  False   True   False   True
# 4   True   True  False   False  False

# Forma incorrecta de buscar nulos
print(None == None)
# True
print(np.nan == np.nan)
# False

# Forma incorrecta
df[df['Uno'] == np.nan]
# Empty DataFrame
# Columns: [Uno, Dos, Tres, Cuatro, Cinco]
# Index: []

# Forma correcta
df[df['Uno'].isna()]  # Filas donde la columna uno sea NaN
#    Uno   Dos  Tres  Cuatro  Cinco
# 2  NaN   NaN   NaN     NaN   13.0
# 3  NaN  16.0   NaN    10.0    NaN
# 4  NaN   NaN   5.0    10.0   13.0

# Los valores nulos no tienen valor
s = pd.Series([np.nan, np.nan])
s.sum()
# 0.0

df.sum(axis=1)
# 0    17.0
# 1    38.0
# 2    13.0
# 3    26.0
# 4    28.0
# dtype: float64

df.sum(axis=1, skipna=False)
# 0   NaN
# 1   NaN
# 2   NaN
# 3   NaN
# 4   NaN
# dtype: float64

