import numpy as np
import pandas as pd

aleatorio = np.random.randint(low=20, high=100, size=[20, ])
nombre = np.random.choice(['Jaime', 'Sebastian', 'Maximo', 'Claudio'], 20)
numero = np.random.choice([10, 11, 13, 45, 8, 2], 20)
df = pd.DataFrame({'Aleatorio': aleatorio, 'Nombre': nombre, 'Numero': numero})
