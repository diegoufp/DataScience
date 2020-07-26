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

## Índices y selección

Existen muchas formas de manipular los DataFrames y de seleccionar los elementos que queremos transformar.

- **Dictionary like**:
```
df[`col1`] # Regresa un DataSeries
df[['col1', 'col3']] # Regresa un DataFrame
```

- **Numpy like**:
iloc = index location
```
df.iloc[:] # fila
df.iloc[:,:] # fila, columna
```

- **Label based**:
loc = location
```
df.loc[:] # fila
df.loc[:,:] # fila, columna
```

Existe una gran diferencia en la forma en la que utilizamos estos slices porque varia de la forma tradicional de Python. `loc` va a incluir el final del que necesitamos.

### Read data
```python
import pandas as pd

#pd.options.display.max_rows = 10 <- Muestra cierta cantidad de datos en este caso 10 

el_universal = pd.read_csv("web/web_scrapper_curso_data_eng/eluniversal_2019_06_07_articles.csv")

type(el_universal)

el_universal.head() # <- muestra las primeras 5 lineas
#el_universal.tail() <- muestra las ultimas 5 lineas
```

### Index and selection

#### dictionary like

```python
el_universal['title']
```
```python
el_universal[['title', 'url']]
```

#### Numpy like

```python
el_universal.iloc[10:15]
```
```
el_universal.iloc[66]['title']
```
```
el_universal.iloc[:5, 0]
```

#### Label based (Forma recomendada)

```
el_universal.loc[:, 'body': 'title']
```

## Data wrangling

**Data wrangling** es una de las actividades más importantes de todos los profesionales de datos. Simplemente es limpiar, transformar y enriquecer el dataset para objetivos posteriores.

Pandas es una de las herramientas más poderosas para realizar este ““domado”” de datos. Recordemos que Pandas trae muchas de sus abstracciones del lenguaje R, pero nos otorga lo mejor de ambos mundos, por eso es tan popular.

Nos permite:

- generar transformaciones con gran facilidad.
- trabajar rápidamente con datasets grandes
- detectar y reemplazar faltantes
- agrupar y resumir nuestros datos
- visualizar nuestros resultados.

### 1. añadir newspaper_uid al DataFrame
```python
import pandas as pd

el_universal = pd.read_csv("web/web_scrapper_curso_data_eng/eluniversal_2019_06_07_articles.csv")

el_universal['newspaper_uid'] = 'eluniversal'
el_universal
```

### # 2. Obtener el host
```python
from urllib.parse import urlparse #<- Permite parsear la url
    #apply Lo que nos permit ees generar transformaciones custom que notros requeramos 
el_universal['host'] = el_universal['url'].apply(lambda url: urlparse(url).netloc)

el_universal
```
- Contar los sitios que se repiten
```
#value_counts (Es una funcion de pandas) Lo que nos permite es contar cuantos valores se repiten y sus frecuencias
el_universal['host'].value_counts()
```