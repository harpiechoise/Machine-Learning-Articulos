import pandas as pd
# Crear un multi index desde listas
datos = [['fiz', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],  
         ['uno', 'dos', 'uno', 'dos', 'tres', 'uno', 'dos', 'tres']]
indice = pd.MultiIndex.from_arrays(datos, names=['Primera', 'Segunda'])


# Desde tuplas
tuplas = list(zip(*datos))
indice = pd.MultiIndex.from_tuples(tuplas)

print(indice)
# MultiIndex(
#      levels=[['bar', 'baz', 'fiz', 'foo', 'qux'], ['dos', 'tres', 'uno']],
#      codes=[[2, 0, 1, 1, 3, 3, 4, 4], [2, 0, 2, 0, 1, 2, 0, 1]])
