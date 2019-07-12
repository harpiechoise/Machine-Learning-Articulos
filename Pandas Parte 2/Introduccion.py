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
# 0  12.0   NaN   5.0     NaN    NaN
# 1  12.0  16.0   NaN    10.0    NaN
# 2   NaN   NaN   NaN     NaN   13.0
# 3   NaN  16.0   NaN    10.0    NaN
# 4   NaN   NaN   5.0    10.0   13.0

