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

## Creando el codigo para la automatización

```
touch newspaper_receipe.py
```
```
vim newspaper_receipe.py
```
```python
import argparse
import logging
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse
import pandas as pd

logger = logging.getLogger(__name__)


def main(filename):
    logger.info('Starting cleaning process')

    df = _read_data(filename) #<- Leer los datos
    newspaper_uid = _extract_newspaper_uid(filename) #<- Extraer
    df = _add_newspaper_uid_column(df, newspaper_uid) #<- Añadirlo a la columna
    df = _extract_host(df) # <- Extraer el host

    return df

def _read_data(filename):
    logger.info('Reading file {}'.format(filename))

    return pd.read_csv(filename)

def _extract_newspaper_uid(filename):
    logger.info('Extracting newspaper uid')
    newspaper_uid = filename.split('_')[0]

    logger.info('Newspaper uid detected: {}'.format(newspaper_uid))
    return newspaper_uid

def _add_newspaper_uid_column(df, newspaper_uid):
    logger.info('Filling newspaper_uid column with {}'.format(newspaper_uid))
    df['newspaper_uid'] = newspaper_uid

    return df

def _extract_host(df)
    logger.info('Extracting host from urls')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)

    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='The path to the dirty data', type=str)

    args = partser.parse_args()
    df = main(args.filename)
    print(df)
```
- Para ejecutarlo:
```
python3 newspaper_receipe.py *.csv
```

## ¿Cómo trabajar con datos faltantes?

Los **datos faltantes** representan un verdadero problema sobre todo cuando estamos realizando agregaciones. Imagina que tenemos datos faltantes y los llenamos con 0, pero eso haría que la distribución de datos se modificaría **radicalmente**. Podemos eliminar los registros, pero la **fuerza** de nuestras conclusiones se debilita.

Pandas nos otorga varias funcionalidades para identificarlas y para trabajar con ellas. Existe el concepto que se llama **NaN**, cuando existe un dato faltante simplemente se rellena con un NaN y en ese momento podemos preguntar cuáles son los datos faltantes con .isna().

- isna() para preguntar donde hay datos faltantes.
- notna() para preguntar dónde hay datos completos.
- dropna() para eliminar el registro.

Para reemplazar:

- fillna() donde le damos un dato centinela
- ffill() donde utiliza el último valor.

### 3. Rellenar datos faltantes

En nuestros datos aparecen varios NaN (de datos faltantes), en el caso de los titulos en algunas ocaciones se encuentran en el ultimo fragmento de la url, nos aprovecharemos de este hecho para en lugar de eliminar los registros completarlos.

```python
missing_titles_mask = el_universal['title'].isna()

missing_titles = (el_universal[missing_titles_mask]['url'].str.extract(r'(?P<missing_titles>[^/]+)$'))

missing_titles = ((missing_titles['missing_titles'].str.split('-')).str.join(' '))

missing_titles = missing_titles.to_frame()

missing_titles
```

### Integrar el codigo al programa

```
vim newspaper_receipe.py
```
```python
import argparse
import logging
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse
import pandas as pd

logger = logging.getLogger(__name__)


def main(filename):
    logger.info('Starting cleaning process')

    df = _read_data(filename) #<- Leer los datos
    newspaper_uid = _extract_newspaper_uid(filename) #<- Extraer
    df = _add_newspaper_uid_column(df, newspaper_uid) #<- Añadirlo a la columna
    df = _extract_host(df) # <- Extraer el host
    df = _fill_missing_titles(df)

    return df

def _read_data(filename):
    logger.info('Reading file {}'.format(filename))

    return pd.read_csv(filename)

def _extract_newspaper_uid(filename):
    logger.info('Extracting newspaper uid')
    newspaper_uid = filename.split('_')[0]

    logger.info('Newspaper uid detected: {}'.format(newspaper_uid))
    return newspaper_uid

def _add_newspaper_uid_column(df, newspaper_uid):
    logger.info('Filling newspaper_uid column with {}'.format(newspaper_uid))
    df['newspaper_uid'] = newspaper_uid

    return df

def _extract_host(df):
    logger.info('Extracting host from urls')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)

    return df

def _fill_missing_titles(df):
    logger.info('Filling missing titles')
    missing_titles_mask = df['title'].isna()

    missing_titles = (df[missing_titles_mask]['url'].str.extract(r'(?P<missing_titles>[^/]+)$'))
    missing_titles = ((missing_titles['missing_titles'].str.split('-')).str.join(' '))
    missing_titles = missing_titles.to_frame()

    df.loc[missing_titles_mask, 'title'] = missing_titles.loc[:, 'missing_titles']

    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='The path to the dirty data', type=str)

    args = parser.parse_args()
    df = main(args.filename)
    print(df)
```

## Limpiando detalles adicionales

### 4. añadir uid a las filas
```python
import hashlib #Por lo usual se usa para operaciones criptograficas
# Usaremos hashlib para generar un hash de la url de tal manera que tengamos un numero unico que mapee siempre esa url
el_universal = pd.read_csv("web/web_scrapper_curso_data_eng/eluniversal_2019_06_07_articles.csv")

# axis=1 -> (eje 1)quiere decir que estamos hablando delas filas
# axis=0 -> (eje 0) estamos hablando de columnas
uids = (el_universal
                   .apply(lambda row: hashlib.md5(bytes(row['url'].encode())), axis=1)
                   .apply(lambda hash_object: hash_object.hexdigest())
       )
# Queremos que esta columna sea nuestro indice
el_universal['uid'] = uids
# inplace lo que significa es que queremos modificar directamente nuestra tabla
el_universal.set_index('uid', inplace=True)

el_universal
```
```python
stripped_body = (el_universal
                 .apply(lambda row: row['body'], axis=1)
                )
stripped_body = stripped_body.str.replace('\n','')
stripped_body = stripped_body.str.replace('\r','')
stripped_body = stripped_body.to_frame()
                                          
stripped_body
```

### Integrar el codigo al programa


```
vim newspaper_receipe.py
```
```python
import argparse
import hashlib
import logging
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse
import pandas as pd

logger = logging.getLogger(__name__)


def main(filename):
    logger.info('Starting cleaning process')

    df = _read_data(filename) #<- Leer los datos
    newspaper_uid = _extract_newspaper_uid(filename) #<- Extraer
    df = _add_newspaper_uid_column(df, newspaper_uid) #<- Añadirlo a la columna
    df = _extract_host(df) # <- Extraer el host
    df = _fill_missing_titles(df)
    df = _generate_uids_for_rows(df) # <- Genera los uids
    df = _remove_new_line_form_body(df)

    return df

def _read_data(filename):
    logger.info('Reading file {}'.format(filename))

    return pd.read_csv(filename)

def _extract_newspaper_uid(filename):
    logger.info('Extracting newspaper uid')
    newspaper_uid = filename.split('_')[0]

    logger.info('Newspaper uid detected: {}'.format(newspaper_uid))
    return newspaper_uid

def _add_newspaper_uid_column(df, newspaper_uid):
    logger.info('Filling newspaper_uid column with {}'.format(newspaper_uid))
    df['newspaper_uid'] = newspaper_uid

    return df

def _extract_host(df):
    logger.info('Extracting host from urls')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)

    return df

def _fill_missing_titles(df):
    logger.info('Filling missing titles')
    missing_titles_mask = df['title'].isna()

    missing_titles = (df[missing_titles_mask]['url'].str.extract(r'(?P<missing_titles>[^/]+)$'))
    missing_titles = ((missing_titles['missing_titles'].str.split('-')).str.join(' '))
    missing_titles = missing_titles.to_frame()

    df.loc[missing_titles_mask, 'title'] = missing_titles.loc[:, 'missing_titles']

    return df

def _generate_uids_for_rows(df):
    logger.info('Generating uids for each row')
    uids = (df
            .apply(lambda row: hashlib.md5(bytes(row['url'].encode())), axis=1)
            .apply(lambda hash_object: hash_object.hexdigest())
            )

    df['uid'] = uids

    return df.set_index('uid')

def _remove_new_line_form_body(df):
    logger.info('Remove new lines from body')

    stripped_body = (df.apply(lambda row: row['body'], axis=1))

    stripped_body = stripped_body.str.replace('\n','')
    stripped_body = stripped_body.str.replace('\r','')
    df['body'] = stripped_body.to_frame()

    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='The path to the dirty data', type=str)

    args = parser.parse_args()
    df = main(args.filename)
    print(df)
```

## Enriquecimiento de los datos

Podemos enriquecer nuestra tabla con información adicional, un poco de información numérica para realizar análisis posterior.

Usaremos **nltk** es una librería dentro del stack de Ciencia de Datos de Python que nos va a permitir tokenizar, separar palabras dentro del título y nos permitirá contar la frecuencia de cuántas palabras existen en nuestro título y body

### 6 tokenizar el titulo y el body
```python
import nltk 
#nltk.download() <- Para instalar nltk en jupyter 
from nltk.corpus import stopwords 
# Los stopwords son palabras que no nos a;aden ningun tipo de analisis ulterir (el,la), palabras que se usan mucho en el lenguaje pero que no sirven para determinar que esta sucediendo dentro de nuestro analisis de texto
# nltk es una libreria extensa con ella se puede trabajar con lenguaje natural de manera bastante facil


stop_words = set(stopwords.words('spanish'))

def tokenize_column(df, column_name):
    return (df
            .dropna()
            .apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1)
            .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)))
            .apply(lambda tokens: list(map(lambda token: token.lower(), tokens)))
            .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
            .apply(lambda valid_word_list: len(valid_word_list))
            )

el_universal['n_tokens_title'] = tokenize_column(el_universal, 'title')

el_universal
```

### Integrar el codigo al programa


```
vim newspaper_receipe.py
```
```python
import argparse
import hashlib
import logging
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse
import pandas as pd
import nltk
from nltk.corpus import stopwords 

logger = logging.getLogger(__name__)


def main(filename):
    logger.info('Starting cleaning process')

    df = _read_data(filename) #<- Leer los datos
    newspaper_uid = _extract_newspaper_uid(filename) #<- Extraer
    df = _add_newspaper_uid_column(df, newspaper_uid) #<- Añadirlo a la columna
    df = _extract_host(df) # <- Extraer el host
    df = _fill_missing_titles(df)
    df = _generate_uids_for_rows(df) # <- Genera los uids
    df = _remove_new_line_form_body(df)
    df = _tokenize_title(df, 'title')
    df = _tokenize_body(df, 'body')
    return df

def _read_data(filename):
    logger.info('Reading file {}'.format(filename))

    return pd.read_csv(filename)

def _extract_newspaper_uid(filename):
    logger.info('Extracting newspaper uid')
    newspaper_uid = filename.split('_')[0]

    logger.info('Newspaper uid detected: {}'.format(newspaper_uid))
    return newspaper_uid

def _add_newspaper_uid_column(df, newspaper_uid):
    logger.info('Filling newspaper_uid column with {}'.format(newspaper_uid))
    df['newspaper_uid'] = newspaper_uid

    return df

def _extract_host(df):
    logger.info('Extracting host from urls')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)

    return df

def _fill_missing_titles(df):
    logger.info('Filling missing titles')
    missing_titles_mask = df['title'].isna()

    missing_titles = (df[missing_titles_mask]['url'].str.extract(r'(?P<missing_titles>[^/]+)$'))
    missing_titles = ((missing_titles['missing_titles'].str.split('-')).str.join(' '))
    missing_titles = missing_titles.to_frame()

    df.loc[missing_titles_mask, 'title'] = missing_titles.loc[:, 'missing_titles']

    return df

def _generate_uids_for_rows(df):
    logger.info('Generating uids for each row')
    uids = (df
            .apply(lambda row: hashlib.md5(bytes(row['url'].encode())), axis=1)
            .apply(lambda hash_object: hash_object.hexdigest())
            )

    df['uid'] = uids

    return df.set_index('uid')

def _remove_new_line_form_body(df):
    logger.info('Remove new lines from body')

    stripped_body = (df.apply(lambda row: row['body'], axis=1))

    stripped_body = stripped_body.str.replace('\n','')
    stripped_body = stripped_body.str.replace('\r','')
    df['body'] = stripped_body.to_frame()

    return df

def _tokenize_title(df, column_name):
    stop_words = set(stopwords.words('spanish'))

    n_tokens_titles = (df
            .dropna()
            .apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1)
            .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)))
            .apply(lambda tokens: list(map(lambda token: token.lower(), tokens)))
            .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
            .apply(lambda valid_word_list: len(valid_word_list))
            )
    
    df['n_tokens_title'] = n_tokens_titles

    return df

def _tokenize_body(df, column_name):
    stop_words = set(stopwords.words('spanish'))

    n_tokens_bodys = (df
            .dropna()
            .apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1)
            .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)))
            .apply(lambda tokens: list(map(lambda token: token.lower(), tokens)))
            .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
            .apply(lambda valid_word_list: len(valid_word_list))
            )

    df['n_tokens_body'] = n_tokens_bodys

    return df

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='The path to the dirty data', type=str)

    args = parser.parse_args()
    df = main(args.filename)
    print(df)
```

## Valores duplicados en Jupyter

Estos valores duplicados es importantes identificarlos y removerlos de nuestro datasets para que esos valores no generen un peso no justificado dentro del análisis a realizar dentro de nuestro Pipelines.

Pandas nos otorga la función `drop_duplicates` para eliminar estos valores duplicados.

Lo primero que tenemos que hacer para ver duplicados es tratar de entender donde deberias tener valores duplicados y donde no.

```python
import pandas as pd

el_universal = pd.read_csv("web/web_scrapper_curso_data_eng/eluniversal_2019_06_07_articles.csv")
# si vamos a 'el_universal' y damos la funcion 'value_counts'
# Vamos a ver que en 'url' todas son diferentes lo mismo si fueramos a 'body'
el_universal['url'].value_counts()
```

Sin embargo cuado corremos el 'title' podremos ver que hay titulos que se repiten

```python
import pandas as pd

el_universal = pd.read_csv("web/web_scrapper_curso_data_eng/eluniversal_2019_06_07_articles.csv")
# si vamos a 'el_universal' y damos la funcion 'value_counts'
# Vamos a ver que en 'url' todas son diferentes lo mismo si fueramos a 'body'
el_universal['title'].value_counts()
```

Pandas nos da una facilidad para poder eliminar este tipo de valores duplicados con la funcion `drop_duplicates`
```python
# En keep se puede elegir entre el primero o el ultimo
el_universal.drop_duplicates(subset=['title'], keep='first', inplace=True)
```

### Integrar el codigo al programa


```
vim newspaper_receipe.py
```
```python
import argparse
import hashlib
import logging
logging.basicConfig(level=logging.INFO)
from urllib.parse import urlparse
import pandas as pd
import nltk
from nltk.corpus import stopwords 

logger = logging.getLogger(__name__)


def main(filename):
    logger.info('Starting cleaning process')

    df = _read_data(filename) #<- Leer los datos
    newspaper_uid = _extract_newspaper_uid(filename) #<- Extraer
    df = _add_newspaper_uid_column(df, newspaper_uid) #<- Añadirlo a la columna
    df = _extract_host(df) # <- Extraer el host
    df = _fill_missing_titles(df)
    df = _generate_uids_for_rows(df) # <- Genera los uids
    df = _remove_new_line_form_body(df)
    df = _tokenize_column(df, 'title')
    df = _tokenize_column(df, 'body')
    df = _remove_duplicate_entries(df, 'title')
    df = _drop_rows_with_missing_values(df)
    _save_data(df, filename)

    return df

def _read_data(filename):
    logger.info('Reading file {}'.format(filename))

    return pd.read_csv(filename)

def _extract_newspaper_uid(filename):
    logger.info('Extracting newspaper uid')
    newspaper_uid = filename.split('_')[0]

    logger.info('Newspaper uid detected: {}'.format(newspaper_uid))
    return newspaper_uid

def _add_newspaper_uid_column(df, newspaper_uid):
    logger.info('Filling newspaper_uid column with {}'.format(newspaper_uid))
    df['newspaper_uid'] = newspaper_uid

    return df

def _extract_host(df):
    logger.info('Extracting host from urls')
    df['host'] = df['url'].apply(lambda url: urlparse(url).netloc)

    return df

def _fill_missing_titles(df):
    logger.info('Filling missing titles')
    missing_titles_mask = df['title'].isna()

    missing_titles = (df[missing_titles_mask]['url'].str.extract(r'(?P<missing_titles>[^/]+)$'))
    missing_titles = ((missing_titles['missing_titles'].str.split('-')).str.join(' '))
    missing_titles = missing_titles.to_frame()

    df.loc[missing_titles_mask, 'title'] = missing_titles.loc[:, 'missing_titles']

    return df

def _generate_uids_for_rows(df):
    logger.info('Generating uids for each row')
    uids = (df
            .apply(lambda row: hashlib.md5(bytes(row['url'].encode())), axis=1)
            .apply(lambda hash_object: hash_object.hexdigest())
            )

    df['uid'] = uids

    return df.set_index('uid')

def _remove_new_line_form_body(df):
    logger.info('Remove new lines from body')

    stripped_body = (df.apply(lambda row: row['body'], axis=1))

    stripped_body = stripped_body.str.replace('\n','')
    stripped_body = stripped_body.str.replace('\r','')
    df['body'] = stripped_body.to_frame()

    return df

def _tokenize_column(df, column_name):
    logger.info('Calculating the number of unique tokes in {}'.format(column_name))
    stop_words = set(stopwords.words('spanish'))

    n_tokens = (df
            .dropna()
            .apply(lambda row: nltk.word_tokenize(row[column_name]), axis=1)
            .apply(lambda tokens: list(filter(lambda token: token.isalpha(), tokens)))
            .apply(lambda tokens: list(map(lambda token: token.lower(), tokens)))
            .apply(lambda word_list: list(filter(lambda word: word not in stop_words, word_list)))
            .apply(lambda valid_word_list: len(valid_word_list))
            )

    df['n_tokens_' + column_name] = n_tokens

    return df

def _remove_duplicate_entries(df, column_name):
    logger.info('Removing duplicate entries')
    df.drop_duplicates(subset=[column_name], keep='first', inplace=True)

    return df

def _drop_rows_with_missing_values(df):
    logger.info('Dropping rows with missing values')
    # dropna() -> Elimina las filas que no tiene valores
    return df.dropna()

def _save_data(df, filename):
    clean_filename = 'clean_{}'.format(filename)
    logger.info('Saving data at location: {}'.format(clean_filename))
    df.to_csv(clean_filename, encoding = 'utf-8-sig')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='The path to the dirty data', type=str)

    args = parser.parse_args()
    df = main(args.filename)
    print(df)
```

## Visualización de datos

Pandas tambien es un gran aliado a la hora de hacer analisis descriptivo de nuestros datos, es decir, poder entender y visualizar como se componen nuestros datos. Para eso lo mejor es entrar en nuestro `jupyter notebook` y comenzar a ejecutar los metodos descriptivo que nos ofrece pandas.

### Descriptive analysis en jupyter

LO primero que tenemos que hacer es leer nuestros archivos csv que contienen nuestros datos limpios.
```python
import pandas as pd
clean_eluniversal = pd.read_csv('web_scrapper_curso_data_eng/clean_eluniversal_2020_02_23_articles.csv')
clean_elpais = pd.read_csv('web_scrapper_curso_data_eng/clean_elpais.csv')
```
- Metodo describe:

El metodo describe lo que nos otroga es una serie de **valores estadisticos** que nos permiten entender las distribuciones de nuestros datos.
```python
clean_eluniversal.describe()
```

- Visualización de la información donde el token de una columna es mínimo
Mascara booleana:
```python
clean_eluniversal.loc[clean_eluniversal['n_tokens_title'] == 1]
```

- Gráficas por distinción en puntos de diferentes colores para diferentes variables o diferentes Data Frame:
```python
# %matplotlib inline <- Nos permite generar graficos directamente en jupyter notebook
%matplotlib inline
clean_eluniversal['n_tokens_title'].plot(style = 'k.')
clean_eluniversal['n_tokens_body'].plot(style = 'r.')
```

- Elaboración de histogramas para dos o más variable o dos o mas Data Sets:
```python
# .concat nos permite juntar dos diferentes dataframes
all_newspaper =pd.concat([clean_eluniversal])
# Los agruparemos por su newspaper_uid
grouped = all_newspaper.groupby('newspaper_uid')
# Comparar atraves de un histograma
grouped.hist()
# Grafica de lineas
grouped.plot()
```

- Visualización de valores mínimos, medios y maximos de uno o mas Data Sets:
```python
# .agg <- agregacion
grouped['n_tokens_body'].agg(['min', 'mean', 'max'])
```
