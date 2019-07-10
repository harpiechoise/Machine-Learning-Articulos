# Pandas
## 1. Introduccion
En el mundo del Datascience, siempre estamos lidando con datos que no tienen el formato que deseamos, y con ayuda de numpy podemos darle formato, pero no es suficiente, Numpy es mejor para numeros, para datos de cualquier tipo necesitamos de una herramienta mas poderosa, una herramienta mas preparada para trabajar con datos de cualquier tipo, y esta es Pandas.

Pandas tiene un set rico en funciones para trabajar con datos de varios tipos, Y trabajar con el es facil y si sabemos manejarlo podremos hacer esto de manera rapida. Ahora vamos con lo basico

# https://pandas.pydata.org/pandas-docs/version/0.25.0/user_guide/indexing.html#different-choices-for-indexing
Indexing Choices

Anot 3
The .loc attribute is the primary access method. The following are valid inputs:

A single label, e.g. 5 or 'a' (Note that 5 is interpreted as a label of the index. This use is not an integer position along the index.).
A list or array of labels ['a', 'b', 'c'].
A slice object with labels 'a':'f' (Note that contrary to usual python slices, both the start and the stop are included, when present in the index! See Slicing with labels.
A boolean array.
A callable, see Selection By Callable.