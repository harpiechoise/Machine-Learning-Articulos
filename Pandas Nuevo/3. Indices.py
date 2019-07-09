import numpy as np 
import pandas as pd  # Importamos pandas bajo el pseudonimo

dates = pd.date_range('27/2/2019', periods=8)
df = pd.DataFrame(np.random.random(8, 4), index=dates,
                  columns=['A', 'B', 'C', 'D'])
