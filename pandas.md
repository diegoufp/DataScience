# Pandas

**Pandas** nos otorga diversas facilidades para el ““domados de datos””. Nos otorga dos estructuras de datos:


- **Series**: Es un array unidimensional que representa una columna.
- **DataFrame**: Es un conjunto de series que forman una tabla. Se pueden acceder a través de indices como una etiqueta(label) o pueden ser posicionales es decir 0 o índice 100. También pueden ser rangos o slices

Estas estructuras de datos **no son** contenedores de datos. En Pandas las utilizamos para transformar y enriquecer nuestros datos, manipularlos, manejar los faltantes, realizar operaciones aritméticas, combinar diferentes dataframes en uno solo para obtener una nueva tabla. Leer datos de archivos y escribir a disco.

## Estructuras de datos

### Series

**Series** es un vector unidimensional, para poder acceder a esta lista podemos usar posiciones o labels, siendo este último el preferido para manipular las **series**. Una diferencia importante sobre las listas de Python es que los datos son homogéneos, es decir solo podemos tener un **tipo de dato** por cada **Serie**.

Las **Series** se pueden crear a partir de cualquier secuencia(listas, tuplas, arrays de numpy y diccionarios).

En Python tenemos la filosofía del Duck Typing, si se ve como un pato y hace cuac, a ese animal le llamamos pato, si una serie se comporta una lista, se accede como una lista en principio deberíamos llamarla lista, pero esto no es así.

Una mejor aproximación para inicializar Series es utilizar diccionarios.

```python
import pandas as pd

series_test = pd.Series([100, 200, 300])
series_test

series_test2 = pd.Series({1999: 48, 2000: 65, 2001:89})
series_test2
```

### DataFrames 

**DataFrames** son simplemente una tabla donde las filas y las columnas tienen etiquetas, se puede construir de diferentes formas pero siempre debemos considerar que la estructura que necesitamos construir para inicializarla tiene que ser bidimensional. Una matriz y puede ser una lista de listas, lista de tuplas, un diccionario de Python u otro **DataFrame**.

Si solo tenemos una dimensión a eso no le llamamos **DataFrame**, le llamamos **Serie**. Cuando utilizamos un diccionario las llaves se convierten en las llaves de la columna.

```python
import pandas as pd

frame_test = pd.DataFrame({1999: [74, 38, 39], 2000: [34, 32, 32], 2001: [23, 39, 23]})

frame_test

frame_test2 = pd.DataFrame([[74, 38, 39], [34, 32, 32], [23, 39, 23]], columns=[1999, 2000, 2001])

frame_test2
```