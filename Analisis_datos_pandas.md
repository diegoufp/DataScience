# Manipulación y Análisis de Datos con Pandas y Python

## Qué es pandas?

En Computación y Ciencia de datos, **pandas** es una biblioteca de software escrita como extensión de Numpy para manipulación y análisis de datos para el lenguaje de programación Python. En particular, ofrece estructuras de datos y operaciones para manipular tablas numéricas y series temporales.

Las **características** de la biblioteca son:

El tipo de datos son DataFrame para manipulación de datos con indexación integrada. Tiene herramientas para leer y escribir datos entre estructuras de dato en memoria y formatos de archivos variados
Permite la alineación de dato y manejo integrado de datos fallantes, la reestructuración y segmentación de conjuntos de datos, la segmentación vertical basada en etiquetas, indexación elegante, y segmentación horizontal de grandes conjuntos de datos, la inserción y eliminación de columnas en estructuras de datos.
Puedes realizar cadenas de operaciones, dividir, aplicar y combinar sobre conjuntos de datos, la mezcla y unión de datos.
Permite realizar indexación jerárquica de ejes para trabajar con datos de altas dimensiones en estructuras de datos de menor dimensión, la funcionalidad de series de tiempo: generación de rangos de fechas y conversión de frecuencias, desplazamiento de ventanas estadísticas y de regresiones lineales, desplazamiento de fechas y retrasos.
Como podemos ver, se trata de una herramienta realmente eficaz con multiplicidad de usos, lo que la convierte en excelente para el tratamiento de datos, y dada su sencillez, también es apta para usuarios poco expertos en la programación, lo que ha convertido a Python en un lenguaje de programación muy usado y muy demandado.

## Series e Indexación y selección de datos

[Google colab](https://colab.research.google.com/notebooks/intro.ipynb#recent=true "Google colab")

```py
import pandas as pd

# SERIES

sr = pd.Series([10,9,8,7,6])
# Ver los valores de la variable que contiene un vector
sr.values

# Ver el indice de nuestra serie(muestra informacion como rango y principio)
sr.index

# Ver la dimencionalidad del objeto
sr.shape

# fromar de buscar los valores de la variable
sr[:]
sr[[0,4,2]]
sr[0]

# Definir un nuevo indice(en esta ocacion cabiamos a in index basado en letras y no numeros)
sr = pd.Series([10,9,8,7,6], index=['a','b','c','d','e'])

# y para llamarlos 
sr['c']
sr[['d', 'c']]
sr['b':'e']
sr[:]

# DICCIONARIOS

dic_data = {'CO':100, 'MX':200, 'AR':300}

# Ver los valores de la variable que contiene un vector
dic_data.keys()

# Estraer la informacion de los diccionarios
dic_data['MX']

# Transformar un diccionario en una serie de pandas
pd.Series(dic_data)

# Definir un nuevo indice(en esta ocacion cabiamos a in index basado en letras y no numeros)
pd.Series(dic_data, index=['CO','MX','PE'])

# En esta ocacion el valor de 'PE' sera 'NaN', el cual es uns variable nula, cualquier operacion que se haga con una variable nula sera igual a nula, 'Nan' + 10 = 'Nan'

# Identificar los objetos que son nulo
sr = pd.Series(dic_data, index=['CO','MX','PE'])
sr.isnull()

# Identificar los objetos que no son nulos
sr.notnull()
```

## DataFrame

Una **DataFrame** es una estructura bidimencional en donde las columnas tienen varias categorias de datos.

```py
import pandas as pd
import numpy as np

# ver la version de pandas
pd.__version__

# actualizar la version de pandas(codigo funcional en google colab)
!pip install --upgrade pandas

dict_data = {'CH':[100,800,200], 'CO':[100,200,300],'MX':[300,500,400]}
dict_data

# Transformar diccionario en dataframe
df = pd.DataFrame(dict_data)
df

dict_data = {
    'edad': [10,9,13,14,12,11,12],
    'cm': [115,110,130,155,125,120,125],
    'pais':['co','mx','co','mx','mx','ch','ch'],
    'genero':['M','F','F','M','M','M','F'],
    'Q1':[5,10,8,np.nan,7,8,3],
    'Q2':[7,9,9,8,8,8,9]
}

df = pd.DataFrame(dict_data)
df

# definir los indices
df = pd.DataFrame(dict_data, index = ['ana','benito','camilo','daniel','erika','fabian','gabriela'])
df

# ver el index del dataframe
df.index

# ver las columnas del dataframe
df.columns

# valores que componen el dataframe
df.values

# buscar un subconjunto de datos
df['edad']
df[['edad','cm','Q1']]

# Buscando un valor guandose por las filas y columnas
df.loc['ana',['edad','cm','Q1']]
df.loc[['ana','erika'],['edad','cm','Q1']]
df.loc['daniel']['Q1']
df.loc['daniel','Q1']

# buscando valores por posiciones
df.iloc[2,1]
df.iloc[2][1]
df.iloc[2,[1,3]]
df.iloc[2][[1,3]]

# filtro por condiciones
df['edad'] >= 12
df['Q2']>= df['Q1']

# usar el filtro para obtener el subconjunto de datos
df[df['edad'] >= 12]
df[df['Q2']>= df['Q1']]

# usar varios filtros
df[(df['edad']>=12)&(df['pais']=='mx')]

# Otra forma de hacer consultas
df.query('edad>12')
```

## Indexado y manejo de archivos CSV

```py
# acceder a las carpertas de google drive
from google.colab import drive
drive.mount('/content/drive')

# al ejecutar el codigo en google colab no va arroja run link despues de una intruccion 'Go to this URL in a browser', le tenemos que dar click al link e inciamos con cuenta gmail para permitir el acceso, depsues arrojara un codigo que tenemos que poner en la instruccion 'Enter your authorization code:' y pegamos la clave de acceso
# ahora ya tenemos acceso a las carpetas dentro del google drive

# cambiar directorios y posicionar dentro de la carpeta colab notebooks
%cd '/content/drive/My Drive/Colab Notebooks'
# 'ls' me permite ver lo que estra dentro de esta carpeta 
!ls
# ahora nuestro colab esta conectado a nuestro google drive

# crear una carpeta dentro de google drive
!mkdir /content/drive/My\ Drive/Colab\ Notebooks/db

dir_pandas = '/content/drive/My Drive/Colab Notebooks/db/{}'.format('test.csv')
dir_pandas

import pandas as pd
import numpy as np

dict_data = {
    'edad': [10,9,13,14,12,11,12],
    'cm': [115,110,130,155,125,120,125],
    'pais':['co','mx','co','mx','mx','ch','ch'],
    'genero':['M','F','F','M','M','M','F'],
    'Q1':[5,10,8,np.nan,7,8,3],
    'Q2':[7,9,9,8,8,8,9]
}
df = pd.DataFrame(dict_data)
df
dir_pandas = '/content/drive/My Drive/Colab Notebooks/db/{}'.format('test.csv')

# guardar un dataframe en un archivo csv en google drive
df.to_csv(dir_pandas)
# si no que remos guardar el index
df.to_csv(dir_pandas, index=False)
# verificar que se haya creado el archivo
!ls /content/drive/My\ Drive/Colab\ Notebooks/db

# leer el archivo que esta en google drive
df_read = pd.read_csv('/content/drive/My Drive/Colab Notebooks/db/test.csv')
df_read

# definir otro formato para separar la informacion(los formatos csv esta separados por ';')
df.to_csv(dir_pandas,sep='|', index=False)
# para leer este archivo separado por '|' en lugar de ';'
df_read = pd.read_csv('/content/drive/My Drive/Colab Notebooks/db/test.csv', sep='|')
df_read
```

## Cómo usar Pandas y Python para conectar con tu base de datos SQL

Pandas cuenta con una funcionalidad que facilita el acceso a tus bases de datos tipo SQL, para ello te mostrare algunos ejemplos:

- **PostgreSQL**:

Valida que tengas la librería `psycopg2` usando el comando `import`. Si no está instalada en tu ambiente, usa el comando `!pip install psycopg2` en la terminal de python para instalarlo.

Comenzamos cargando las librerías:
```py
import pandas as pd
import psycopg2
```

Luego creamos el elemento de conexión con el siguieente código:
```py
Conn_sql = psycopg2.connect(user = "user_name",
                            password = "password",
                            host = "xxx.xxx.xxx.xxx",
                            port = "5432",
                            database = "postgres_db_name")
```

Seguido simplemente definimos nuestra query en SQL:
```py
query_sql = '''
select *
from table_name
limit 10
'''
```

Y creamos nuestro dataframe:
```
df = pd.read_sql(query_sql, sql_conn)
df.head(5)
```

- **SQL Server:**

Valida que tengas la librería `pyodbc` usando el comando `import`, si no está instalada en tu ambiente, usa el comando `!pip install pyodbc` en la terminal python para instalarlo.

Comenzamos cargando las librerías:
```py
import pandas as pd
import pyodbc
```

Luego creamos el elemento de conexión con el siguiente código:
```py
driver = '{SQL Server}'
server_name = 'server_name'
db_name = 'database_name'
user = 'user'
password = 'password'
sql_conn = pyodbc.connect('''
DRIVER={};SERVER={};DATABASE={};UID={};PWD={};
Trusted_Connection=yes
'''.format(driver, server_name, db_name, user, password))
```

O si tienes el DSN:

```py
dsn = 'odbc_datasource_name'
sql_conn = pyodbc.connect('''
DSN={};UID={};PWD={};Trusted_Connection=yes;
'''.format(dsn, user, password))
Seguido simplemente definimos nuestra query en SQL:	
query_sql = 'select * from table_name limit 10'
```

Y creamos nuestro dataframe con:

```py
df = pd.read_sql(query_sql, sql_conn)
df.head(5)
```

- **MySQL / Oracle / Otras**:

Valida que tengas la librería `sqlalchemy` usando el comando `import`, si no está instalada en tu ambiente, usa el comando `!pip install sqlalchemy` en la terminal de python para instalarlo.

Comenzamos cargando las librerías:

```py
import pandas as pd
import sqlalchemy as sql
Escogemos nuestra base de datos, Oracle, MySql o la de tu preferencia:
database_type = 'mysql'
database_type = 'oracle'
```

Luego creamos el elemento de conexión con el siguiente código:
```py
user = 'user_name'
password = 'password'
host = 'xxx.xxx.xxx.xxx:port'
database = 'database_name'

conn_string = '{}://{}:{}@{}/{}'.format(
database_type, user, password, host, database)

sql_conn = sql.create_engine(conn_string)
```

Seguido simplemente definimos nuestra query en SQL:
```py
query_sql = '''
select *
from table_name
limit 10
'''
```

Y creamos nuestro dataframe con:
```py
df = pd.read_sql(query_sql, sql_conn)
df.head(5)
```

La libreria `sqlalchemy` también soporta PostgreSQL y otras fuentes de datos.

## Ventajas y desventajas de los formatos

**CSV, json y formatos String** : Son simples, requieren alto costo computacional y algo lentos.

**HDF** : Gran soporte, adecuado para grandes cantidades de datos, rápido a costo de alto costo computacional.

**Parquet**: Puede igualar a hdf e inclusive trabajar por chunks y en paralelo.

**Pickle** : Es práctico pero lento con grandes cantidades de datos.

```py
import pandas as pd
import numpy as np
# acceder a las carpertas de google drive
from google.colab import drive
drive.mount('/content/drive')

# al ejecutar el codigo en google colab no va arroja run link despues de una intruccion 'Go to this URL in a browser', le tenemos que dar click al link e inciamos con cuenta gmail para permitir el acceso, depsues arrojara un codigo que tenemos que poner en la instruccion 'Enter your authorization code:' y pegamos la clave de acceso
# ahora ya tenemos acceso a las carpetas dentro del google drive

# cambiar directorios y posicionar dentro de la carpeta colab notebooks
%cd '/content/drive/My Drive/Colab Notebooks/db'
# 'ls' me permite ver lo que estra dentro de esta carpeta 
!ls
# ahora nuestro colab esta conectado a nuestro google drive

dir_pandas = '/content/drive/My Drive/Colab Notebooks/db/{}'
dir_pandas

dict_data = {
    'edad': [10,9,13,14,12,11,12],
    'cm': [115,110,130,155,125,120,125],
    'pais':['co','mx','co','mx','mx','ch','ch'],
    'genero':['M','F','F','M','M','M','F'],
    'Q1':[5,10,8,np.nan,7,8,3],
    'Q2':[7,9,9,8,8,8,9]
}
df = pd.DataFrame(dict_data)

# Guardar un archivo en formato excel
df.to_excel(dir_pandas.format('test.xlsx'))
# Guardar un archivo en formato excel y eliminar el index
#df.to_excel(dir_pandas.format('test.xlsx').index=False)
# Guardar un archivo en formato excel y poder nombre a la hoja
#df.to_excel(dir_pandas.format('test.xlsx').index=False, sheet_name='hoja_uno')

# Leer un archivo en formato excel
pd.read_excel(dir_pandas.format('test.xlsx'))

# Guardar documentos en formato json
df.to_json(dir_pandas.format('test.json'))
# Pra leer un archivo en formato json, si no especificamos el archivo sea creara el archivo en blanco
pd.read_json(dir_pandas.format('test.json'))

# Guardar docuemtno en formato ico
# ico es una formato binario que se usa cuando una base de datos tiene un tama;o mediano
df.to_pickle(dir_pandas.format('test.pkl'))
# leer un archivo en formato ico, el objeto 'Dataframe' no tiene atributos pickle por lo cual lo tenemos que leer con un 'pd'
pd.read_pickle(dir_pandas.format('test.pkl'))

# Otro formato muy utilizado cuando hablamos de bigdata y estas bases pertenecen a apache es el formato parquet
df.to_parquet(dir_pandas.format('test.parquet'))
# para leer el formato parquet
pd.read_parquet(dir_pandas.format('test.parquet'))
# tambien esta el fromato hdf que es muy utilizado con hadoop
df.to_hdf(dir_pandas.format('test.hdf'), key='data',format='table')
# para leer el archivo hdf
pd.read_hdf(dir_pandas.format('test.hdf'))
```

## Tipos de Variables que componen un data frame

La base de datos que usaremos para esta practica la encontraremos en [Google Data Search](https://datasetsearch.research.google.com/ "Google Data Search").

Siendo ams especifico usaremos una [base de datos de metioritos](https://data.nasa.gov/Space-Science/Meteorite-Landings/gh4g-9sfh "base de datos de metioritos") en el cual le daremos en la opcion de `import` para descargar el la data en un archivo csv.

```py
import pandas as pd
import numpy as np
# acceder a las carpertas de google drive
from google.colab import drive
drive.mount('/content/drive')

# al ejecutar el codigo en google colab no va arroja run link despues de una intruccion 'Go to this URL in a browser', le tenemos que dar click al link e inciamos con cuenta gmail para permitir el acceso, depsues arrojara un codigo que tenemos que poner en la instruccion 'Enter your authorization code:' y pegamos la clave de acceso
# ahora ya tenemos acceso a las carpetas dentro del google drive

# cambiar directorios y posicionar dentro de la carpeta colab notebooks
%cd '/content/drive/My Drive/Colab Notebooks/db'
# 'ls' me permite ver lo que estra dentro de esta carpeta 
!ls
# ahora nuestro colab esta conectado a nuestro google drive

# este es el bd que descargamos :
df_meteorites = pd.read_csv('Meteorite_Landings.csv')
# si la base de datos es muy grande podemos usar la funcion 'head' para ver los primeros datos.
# por defecto nos mostrara los primeros 5 datos pero si queremos mas datos tenemos que especificar el numero entre parentesis
df_meteorites.head()
# asi mismo existe la funcion 'tail' que nos muestra los ultimos 5 datos que podemos especificar ams de igual forma
df_meteorites.tail()
# Si queremos tomar una muestar de datos aleatorios usamos 'sample', por defecto nos muetsra uno pero podemos especificar mas
df_meteorites.sample()

# para examinar el tam;o de la base de datos usamos 'shape', la cual muestra el numero de filas y columnas que lo conforman 
df_meteorites.shape
# si queremos ver el total de los datos que componen la base de datos usamos 'size' y esto es solamente el producto de las filas por las columnas
df_meteorites.size
# si queremos saber la informacion de las variables numericas que componen mi base de datos usamos 'describe'
# la funcion 'describe' nos muestra cualidades estaditica de la base de datos
df_meteorites.describe()
# para quitar las notaciones cientificas
pd.options.display.float_format = '{:,.1f}'.format
# y corretemos de neuvo la linea anterior
df_meteorites.describe()
# tambien podemos usar 'describe' para tener informacion de tipo texto y variable numericas
df_meteorites.describe(include='all')
# para ver de que esta compuesta las variables de la base de datos
df_meteorites.info()
# solo ver el tipo de las variables
df_meteorites.dtypes

# Hay una funcionalidad en las nuevas versiones de pandas que nos permite convertir y encontrar el formato mas adecuado para las variables
# un ejemplo de esto es que convierte en estas variables 'int64' a 'Int64' que esto es un nuevo tipo de entero tambien puede entender como funcionan las variables no definidas.
df_meteorites.convert_dtypes().dtypes
```

## Estructuras de dataframes en detalle

```py
# ver la variedad de los datos que componen el dataframe
df_meteorites.nunique()
# Definir(agregar) una nueva variable en el dataframe
df_meteorites[['fall','nametype']] = df_meteorites[['fall','nametype']].astype('category')
# y si ahora vemos de que estan compuestas la variables de nuestro dataframe vemos que ahora tienemos un nuevo tiempo de categoria
df_meteorites.dtypes
# tambien podemos usar 'unique' para saber las categorias que componen esta variable
df_meteorites['fall'].unique()
# para saber la frecuencia de las categoria en una variable usamos:
df_meteorites['fall'].value_counts()

# Para crear una variable dummies usamos:
# Convertir nuestra variables tipo texto a variables tipo dummies es de gran importancia a la hora de hacer analisis de datos puesto que nuestra vriable deja de tener un formato texto y ahora pasa a tener un formato numerico
pd.get_dummies(df_meteorites['fall'])

# Crear una nueva variable(columna), en este caso ponemos el nombre de la columna que queremos crear y lo que contendra
df_meteorites['ones'] = 1 # con esto logramos crear un columna de puros numero unos
# AHora si queremos crear dos nuevas columnas con valores dommies:
df_meteorites[['fell','found']] = pd.get_dummies(df_meteorites['fall'])

# para variable de tiempo:
df_meteorites['year']
# para convertir a variable tipo tiempo:
# el format 'errors' permite que cada vez que encuentre un formato que no corresponde al tiempo siemplente genere un variable no numerica 
# 'format' compone le formato en el que se vera al fecha 
pd.to_datetime(
    df_meteorites['year'],
    errors = 'coerce',
    format = '%m/%d/%Y%H:%M:%S%p'
) 
# y asi convertimos y sobreescribimos el formato tipo texto a un formato de tiempo:
df_meteorites['year'] = pd.to_datetime(
    df_meteorites['year'],
    errors = 'coerce',
    format = '%m/%d/%Y%H:%M:%S%p'
)
# y si vemos ahora los tipos de vairable que componen el df vemos el cambio
df_meteorites.convert_dtypes().dtypes

# Para renombrar alguna de las columnas
# el parametro 'inplace' lo que hace es que los combios que hagamos sobre el dataframe van a quedar guardados directamente
df_meteorites.rename(columns={'mass (g)':'mass'}, inplace=True)
# Una forma practica de obtener los nombres de las columnas es usar 'list'
list(df_meteorites)

# Una gran ventaja de trabajar con variable 'categoricas' es que reduce el uso de memoria ram y tambien el espacio que ocupan los archivos
```

## Borrar filas, columnas y copiar información

```py
df_meteorites

# Borrar una columna
# En el parametro 'axis' debemos indicar '0'(index) o '1'(columns)
# 'inplace' nos permite registrar el cambio en el df
df_meteorites.drop(['ones'], axis=1 , inplace=True)

# Para borrar filas(index)
# por defecto cuando se hace drop de una lista pandas reconoce que se esta borrando en el eje de las filas pero de igual froma se puede especificar
df_meteorites.drop[[0,2,4,6]]

# si nosotros queremos modificar un df pero no queremos guardar los cambios directamente sobre el sino mas bien trabar sobre una copia.
# 'deep' es una especificacion de que la copia es profunda, esto es por que cuando una df se copia en una variabla, la variable no copia directamente el df, lo que copia es la referencia a la memoria donde se estan guardando los datos.
# Es decir que si no especificamos con 'deep' entonces los cambios que hagos sobre 'df' tambien se haran sobre 'df_meteorites'
df = df_meteorites.copy(deep=True)
df.drop(['id'], axis=1, inplace=True) # de esta forma mi copia es alterada y la original no
```

## Funciones matemáticas

Para esta practica usaremos una fuente de informacion diferente, esta la tomaremos de la pagian de [kaggle](https://www.kaggle.com/ "kaggle"), el cual es una [base de datos de bicicletas compartidas](https://www.kaggle.com/hmavrodiev/london-bike-sharing-dataset "base de datos de bicicletas compartidas"). Hacemos click a la pesta;a de `Data` hasta encontrar la opcion de `Download`.

```py
import pandas as pd
import numpy as np
# acceder a las carpertas de google drive
from google.colab import drive
drive.mount('/content/drive')

# al ejecutar el codigo en google colab no va arroja run link despues de una intruccion 'Go to this URL in a browser', le tenemos que dar click al link e inciamos con cuenta gmail para permitir el acceso, depsues arrojara un codigo que tenemos que poner en la instruccion 'Enter your authorization code:' y pegamos la clave de acceso
# ahora ya tenemos acceso a las carpetas dentro del google drive

# cambiar directorios y posicionar dentro de la carpeta colab notebooks
%cd '/content/drive/My Drive/Colab Notebooks/db'
# 'ls' me permite ver lo que estra dentro de esta carpeta 
!ls
# ahora nuestro colab esta conectado a nuestro google drive

# esta es la base de datos que decargamos
df_lmerged = pd.read_csv('london_merged.csv')
# Primero reconoceremos los tipos de variables que tenemos en el df
df_lmerged.dtypes

# En esta ocacion hay una columna que trabaja sobre un tipo texto cuando debria set tipo tiempo, asi que lo cambiaremos:
# avece ssi el formato no es muy complejo panda sen capaz de reconocerlo y transformarlo correctamente en el formato deseado
df_lmerged['timestamp'] = pd.to_datetime(df_lmerged['timestamp'])
df_lmerged['timestamp']

# crearemos una nueva columna llamada hora
# una de las funcion que se pueden hacer con columnas tipo timepo es:
df_lmerged['hour'] = df_lmerged['timestamp'].dt.hour
df_lmerged['hour']

# localizaremos los datos numericos
df = df_lmerged.iloc[:,1:]
df
# sabre un DataFrame podemos usar operaciones directamente y tambien podemos hacer operaciones entre las misma columnas

# atraves de iloc podemos seleccionar solo los datos que coresponde a index pares
df['t1'].iloc[::2]
# si hacemos uan resta con otra variable 
df['t1'].iloc[::3] - df['t2'] # en esta ocacion apareceran datos con 'NaN' por que en esos campos no habian datos y se autocompletaron con datos nulos
# Para completar las varaibles nulas podemos usar una funcionalidad de pandas
# la duncion 'sub' nos da la versatilidad de llenar los campos 'NaN' con un valor determinado
df['t1'].iloc[::3].sub(df['t2'], fill_value=1000)

# Asi mismo pandas cuenta con otras funcionalidades de algebra lineal como es el 'producto punto'
# Producto punto es el producto escalar entre dos vectores.
# La norma de un vector es la raíz cuadrada de la suma de cada componente al cuadrado.
df['t1'].dot(df['t1'])

```

## Funciones más complejas y lambdas

```py
import pandas as pd
import numpy as np
from google.colab import drive
drive.mount('/content/drive')

%cd '/content/drive/My Drive/Colab Notebooks/db'
!ls

df_meteorites = pd.read_csv('Meteorite_Landings.csv')
df_lmerged['timestamp'] = pd.to_datetime(df_lmerged['timestamp'])
df_lmerged['hour'] = df_lmerged['timestamp'].dt.hour
df = df_lmerged.iloc[:,1:]
df

def fun_1(x):
  y = x**2 + 1
  return y

np.arange(-5,6).shape

fun_1(np.arange(-5,6))

# Usar una funcion en un dataframe
df['hour'].apply(fun_1)

# Tambien podemos usar funciones mas complejas
def fun_2(x, a=0, b=0):
  y = x**2 + a*x + b
  return y

fun_2(10,a=20,b=-100)

# Usar una funcion mas compleja en un dataframe
df['hour'].apply(fun_2, args=(20,-100))
# tambien podemos especificar los argumentos
df['hour'].apply(fun_2,a=20,b=-100)

# Usar funcion lambda
# lambda es un forma de definir una funcion en una sola linea
df['t1'].apply(lambda x: x+273)

# lambas mas complejos 
# eso sacara la media de cada una de las columnas
df.apply(lambda x:x.mean())
# tambien se puede hacer a las filas
df.apply(lambda x:x.mean(), axis=1)
# operaciones esta las columnas con lambdas
df.apply(lambda x:x['t1']-x['t2'], axis=1)

# aplicar un mismo cambio a todo el dataframe
df.applymap(lambda x:x/1000)
```

## Múltiples índices

En esta practica usaremos una base de datos de [The World Bank](https://data.worldbank.org/ "The World Bank") la cual es esta [base de datos](https://data.worldbank.org/indicator/SP.POP.TOTL "base de datos"), simplemente buscamos l opcion de `Download` en `csv` y la subimos a nuestro google drive.

```py
import pandas as pd
import numpy as np
from google.colab import drive
drive.mount('/content/drive')

%cd '/content/drive/My Drive/Colab Notebooks/db/'
!ls

df_pob = pd.read_csv('poblacion.csv')
df_pob

# para quitar la notacion cientifica
pd.options.display.float_format = '{:,.1f}'.format

# cambiar de variable numerica a variable categorica en formato str
df_pob['year'] = pd.Categorical(df_pob['year'].apply(str))

df_pob.dtypes

# La funcion llamada isin crea un vector de variables booleanas (falso, verdadero), que me permitira filtrar ambos paises
idx_filtro = df_pob['Country'].isin(['Aruba', 'Colombia']) # hacemos que los demas paises sean falsos y ['Aruba', 'Colombia'] sean verdaderos
idx_filtro
# df.le devuelve un filtro (True, False) si en esa columna es menor a un valor (less) coloca True.
# idx_filtro_pop = df_pob['pop'].le(1000000)

# usamos el filtro para solo tener informacion de los dos paises
df_sample = df_pob[idx_filtro]
df_sample

# Crear multiples indices
# soret_index nos ayuda a tener una mejor vista
df_sample = df_sample.set_index(['Country', 'year']).sort_index()
df_sample

# ahora si solo queremos eleccionar de indicie a colombia
df_sample.loc['Colombia',:]
# si queremos buscar ademas un a;o en especifico
df_sample.loc['Colombia',:].loc['2016',:]

# atraves de la funcion xs tambien podemos seleccionar multiples indices
df_sample.xs(['Aruba', '2018'])

# si solo queremos seleccionar los a;os ne el segundo indice podemos especificar la busqueda a bajo nivel
df_sample.xs('2018',level='year')

# aplicarlo a toda la base de datos
df_contries = df_pob.set_index(['Country', 'year']).sort_index()
# tambien podemos organizar nuestros datos mediante la funcion 'ascending'
# en el cual establecemos el orden(en esta ocacion establecemos orden alfabetico inverso)
#df_contries = df_pob.set_index(['Country', 'year']).sort_index(ascending=[False,True])
df_contries

# IndexSlice
ids = pd.IndexSlice
df_contries.loc[ids['Aruba':'Austria', '2015':'2017'],:].sort_index()

# si queremos tener todos los indices del primer nivel podemos usar:
df_contries.index.get_level_values(0)
# si queremos tener todos los indices del segundo nivel podemos usar:
df_contries.index.get_level_values(1)

# Cuando trabajamos con un df con multiples indices tenemos que da multiples intrucciones para encontrar un dato en especifico
df_contries['pop']['Colombia']['2018']

# la ventaja de tener dos indices es a la hora de usar funciones matematicas sobre el
# podemos definir que nos calcule la suma de la poblacion, pero en el nivel de indice 'year'
df_contries.sum(level='year')

# cambiar el formato de los indices
# unstack lo que va a ser es convertir los indices en columnas
df_sample.unstack('year')
```

## Cómo trabajar con variables tipo texto en Pandas 

Pandas cuenta con una gran funcionalidad a la hora de interactuar con texto, es super versatil si estas interesado en crear modelos de análisis de lenguaje natural.

Comencemos cargando nuestra librería y creando un diccionario con nombres de personas.
```py
import pandas as pd
data = {'names':['Sara Moreno 34',
                 'jUAn GOMez 23',
                 'CArlos mArtinez 89',
                 'Alfredo VelaZques 3',
                 'luis Mora 56',
                 '@freddier #platzi 10',pd.NA]}
```

Usemos los datos del diccionario para crear nuestro DataFrame. Nuestro DataFrame contiene una columna tipo texto, con variedades de caracteres especiales, números, mayúsculas e inclusive variables nulas.

```py
df = pd.DataFrame(data)
df
```

Para usar las funciones asociadas a texto usamos str en nuestro DataFrame, por ejemplo, si se quiere colocar el texto en minúscula, basta con escribir:

```py
df['names'].str.lower()
```

Para mayúsculas igualmente:
```py
df['names'].str.upper()
```

O si queremos solo la primera letra en mayúscula:
```py
df['names'].str.capitalize()
```

Para contar la longitud de nuestro texto usamos:
```py
df['names'].str.len()
```

Para dividir el texto por espacios usamos split y definimos el carácter por
el que queremos dividir, en este caso, un espacio vacío ' ' o '#':
```py
df['names'].str.split(' ')
df['names'].str.split('#')
```

Para seleccionar los primeros o últimos 5 caracteres usamos:
```py
df['names'].str[:5]
df['names'].str[-5:]
```
Podemos reemplazar una secuencia de caracteres por otra mediante:
```py
df['names'].str.replace('Alfredo','Antonio')
```

También podemos buscar una secuencia de texto en específico, en este caso,
'ara':

```py
df['names'].str.findall('ara')
```

También podemos crear un filtro basándonos en una secuencia de texto en
específico, en este caso, las filas que tengan 'or':
```py
df['names'].str.contains('or')
```
Así mismo, podemos contar el número de ocurrencias de un caracter en específico,
por ejemplo, cuántas veces aparece la letra 'a':
```py
df['names'].str.lower().str.count('a')
```

Existen comandos más avanzados usando Regex, por ejemplo, si quiero extraer los
caracteres numéricos:
```py
df['names'].str.extract('([0-9]+)', expand=False)
```

O, por ejemplo, si quiero extraer las menciones '@xxxx' del texto:
```py
df['names'].str.replace('@[^\s]+','')
```

## Concatenación de DataFrames: concat y append

```py
import pandas as pd
import numpy as np

# para que las cantidades sean mas legibles en pandas y en numpy
pd.options.display.float_format =  '{:.2f}'.format
np.set_printoptions(precision=1)

# CONCATENACION CON NUMPY

# crear numero aleatorio con numpy
# 'rand' crear un numero aleatorio entre 0 y 1
np.random.rand
# 'randn' crea un numero aleatorio -1 y 1

# en este caso crearemos una matris de 2 x 5  en numeros aleatorios
x1 = np.random.rand(2,5)*10
x2 = np.random.rand(2,5)*-1

# numpy puede concadenar matrices con la funcion 'concatenate'
np.concatenate([x1,x2])

# si vemos las dimenciones del objeto que hemos creado podemos ver que ahora crecio a uno de 4 x 5
np.concatenate([x1,x2]).shape

# podemos concadenar a lo largo del eje de las columnas y esto lo hacemos especificando su eje
np.concatenate([x1,x2], axis= 1)

# si vemos las dimenciones del objeto que hemos creado podemos ver que ahora crecio a uno de 2 x 10
np.concatenate([x1,x2], axis= 1).shape

# CONCATENACION CON PANDAS

s1 = pd.Series(x1[0], index=['a', 'b', 'c', 'd', 'e'])
s2 = pd.Series(x2[0], index=['c', 'd', 'e', 'f', 'g'])

# para hacer una concatenacion en pandas usamos la funcion de 'concat'
pd.concat([s1,s2])
# para concatenar a lo largo de las columnas
pd.concat([s1,s2], axis=1)
# para concatenar a lo largo de las columnas sin respetar el indice
# para hacer esto simplemente vamos resetear su indice
# 'reset_index' borra el indice previamente decinido y para que no siga apareciendo como una columna usamos 'drop=True'
# ahora optenemos ua serie con indice nuevos
s1.reset_index(drop=True)

# Y lo remplazamos en la concatenacion 
pd.concat([s1.reset_index(drop=True),s2.reset_index(drop=True)], axis=1)

# CONCATENACION DE DATAFRAMES

df1 = pd.DataFrame(np.random.rand(3,2)*10, columns=['a','b'])
df2 = pd.DataFrame(np.random.rand(3,2)*-1, columns=['a','b'], index=[2,3,4])

pd.concat([df1,df2])

# si queremos concatenar a lo largo de las columnas
pd.concat([df1,df2], axis=1)

# si estamos concadenan dos df y queremos hacer enfacis en una columna donde se comparten los elementos lo podemos hacer atravez del argumento 'join'
pd.concat([df1,df2], axis=1, join='inner')

# si queremos concadenar sin respetar sus indices tambin podemos resetear los indices
pd.concat([df1.reset_index(drop=True),df2.reset_index(drop=True)], axis=1)

# hay una forma mas simple de concadenar dos dataframes y es con 'append'
df1.append(df2)

# siq uermeos hacer un append a lo largo del eje de las columas 
# primero invertimos las filas y las columnas con 'T'
df1.T
# ya hora lo aplicamos para unir atraves del eje de las columnas
df1.T.append(df2.T).T
```

## Merge de DataFrames

**Marge** es un tipo de concatenacion que se da cuando los dos dataframes contienen una columna en comun, estoy es muy util cuando tienes fuentes de datos diferentes y quieres unirficarlos atravez de un parametro que se comparte entre ellas.

```py
import pandas as pd
import numpy as np
from google.colab import drive
drive.mount('/content/drive')

%cd '/content/drive/My Drive/Colab Notebooks/db/'
!ls

df_left = pd.DataFrame(
    {'X':['x0','x1','x2','x3'],
    'W':['w0','w1','w2','w3'],
    'Y':['y0','y1','y2','y3'],
    'Mix':['y2','y3','a2','a3']},
    index = ['y2','y3','a2','a3'])

df_right = pd.DataFrame(
    {'Z':['z2','z3','z4','z5'],
     'A':['a2','a3','a4','a5'],
     'Y':['y2','y3','y4','y5']},
    index = [2,3,4,5])

# ahora las dos columnas se an unificado atravez de una columna en comun
pd.merge(df_left, df_right)

# en general siempre es bueno especificar el tipo de union  que se esta presentando 
pd.merge(df_left, df_right, how='inner', on='Y')

# puedpd.merge(df_left, df_right, how='inner', on='Y')e que queramos unir la columna 'Y' con la columna 'mix' para ello:
pd.merge(df_left, df_right, how='inner', left_on='Mix', right_on='Y')
# tambien podemos hacerlo atraves de la columna 'A' por que esta tiene parametros de 'y' y 'a'
pd.merge(df_left, df_right, how='inner', left_on='Mix', right_on='A')

# Merge posibles:
# 'inner'(natural join): que funciona trayendo los parametros que tienen en comun los dataframe 
# 'left'(left outer join): que siemplemente se a;aden los parametros que tiene a la derecha 
# 'right'(right outer join): que siemplemente se a;aden los parametros que tiene a la izquierda
# 'outer'(full outer join): En donde se juntar todos los parametros

df_left = pd.DataFrame(
    {'X':['x0','x1','x2','x3'],
    'W':['w0','w1','w2','w3'],
    'Y':['y0','y1','y2','y3']},
    index = ['y2','y3','a2','a3'])

df_right = pd.DataFrame(
    {'Z':['z2','z3','z4','z5'],
     'A':['a2','a3','a4','a5'],
     'Y':['y2','y3','y4','y5']},
    index = [2,3,4,5])

# 'inner'(natural join): que funciona trayendo los parametros que tienen en comun los dataframe 
pd.merge(df_left, df_right, how='inner', on='Y')

# 'left'(left outer join): que siemplemente se a;aden los parametros que tiene a la derecha 
pd.merge(df_left, df_right, how='left', on='Y')

# 'right'(right outer join): que siemplemente se a;aden los parametros que tiene a la izquierda
pd.merge(df_left, df_right, how='right', on='Y')

# 'outer'(full outer join): En donde se juntar todos los parametros
pd.merge(df_left, df_right, how='outer', on='Y')

# Hay otros tipo de merge que se pueden hacer cuando se comparte mas de un solo parametro
df_left = pd.DataFrame(
    {'X':['x0','x1','x2','x3'],
    'W':['w0','w1','w2','w3'],
    'Y':['y0','y1','y2','y3'],
     'A':['a0','a1','a2','a3']}
    )

df_right = pd.DataFrame(
    {'Z':['z2','z3','z4','z5'],
     'A':['a2','a3','a4','a5'],
     'Y':['y2','y3','y4','y5']},
    index = [2,3,4,5])

pd.merge(df_left, df_right, how='outer', on=['Y','A'])
# Es importante el definir las columnas a las cuales vamos a ahcer el merge
# si especificamos solamente la columna 'A' entonces las columnas con mismo valores que no especificames apareceran con un sufijo para diferenciarlas
pd.merge(df_left, df_right, how='outer', on='A')
# Estos sufijos se pueden cambiar con 'suffixes'
pd.merge(df_left, df_right, how='outer', on='A', suffixes=['_left', '_right'])
```

## ¿Cómo lidiar con datos faltantes en tus DataFrames? 

Es muy común que nuestros DataFrames presenten datos faltantes, antes de empezar a procesar nuestros DataFrames veamos un poco en qué consisten los objetos NaN (Not a Number).

Importemos las librerias Pandas y Numpy para esto:

```py
import numpy as np
import pandas as pd
```

Un número que no está definido usualmente se representa con el siguiente objeto:
```
np.nan
> nan
```

¡Este objeto tiene propiedades matemáticas! Al sumar un número, obtenemos como
respuesta el mismo NaN.
```py
np.nan + 0
> nan

np.nan > 0
> False
```

La versión 1.0 de pandas incluye un nuevo objeto NA, que es mucho más
general pues, ademas de interactuar con números, tambien puede hacerlo con
cadenas de texto u otras varaibles como las de tipo booleano. Si quieres que
esta nueva definición este incluida entre tus cálculos usa:

```py
pd.options.mode.use_inf_as_na = True
```

Al sumar NA a una cadena de texto, obtengo el mismo NA:
```
pd.NA +'Hola mundo'
> <NA>

pd.NA | False
> <NA>
```

A continuación, vamos a crear un DataFrame
```py
df = pd.DataFrame(np.arange(0, 15).reshape(5, 3), columns=['a', 'b', 'c'])
df
```

Y vamos a añadir algunas variables no definidas:
```py
df['d'] = np.nan
df['e'] = np.arange(15, 20)
df.loc[5,:] = pd.NA
df.loc[4,'a'] = pd.NA
df.loc[0,'d'] = 1
df.loc[5,'d'] = 10
df
```

Para reconocer cuando un objeto es nulo simplmente usamos:
```
df.isnull()
```

En dónde todas nuestras variables no definidas fueron marcadas con `TRUE`,
`df.isna()` tambien cumple esta función.



Conocer el número de variables nulas por columna puede hacerse juntando el
comando anterior con la funcion de suma:

```
df.isnull().sum()
```

Si lo que nos interesa es conocer el número de filas con elementos nulos, basta
con usar `axis=1`:
```
df.notnull().sum(axis=1)
```

O todos los elementos nulos de nuestro DataFrame:
```
df.size-df.isnull().sum().sum()
```

Reconocer estos elementos nos puede ayudar a filtrar en nuestro DataFrame, en
este caso, me gustaría filtrar por las variables no nulas de la columna ‘a’:
```py
df[df['a'].notnull()]
```

`dropna` es perfecto para elimnar rapidamente las filas con registros faltantes:
```py
df.dropna()
df[['a']].dropna()
```

Ya que hemos visto cómo funcionan las variable nulas, veamos cómo lidiar con
ellas. Usando la función fillna podremos reemplazarlas por el valor que
querramos, en este caso 0.
```
df.fillna(0)
```

Si quisieramos remplazar con el valor siguiente usamos `method="ffill"`:
```py
df.fillna(method="ffill")
```

Si quisieramos remplazar con el valor previo usamos `method="bfill"`, eso es lo contrario a `method="ffill"`:
```
df.fillna(method="bfill")
```

El mismo ejercicio anterior se puede aplicar con las filas usando `axis=1`:
```py
df.fillna(method="bfill",axis=1)
```

Podemos usar también una serie para reemplazar los valores de una columna en especifico, es importante que haya emparejamiento entre los índices:
```
fill = pd.Series([100, 101, 102])
fill
```
```py
df['d'] = df['d'].fillna(fill)
df['d']
df
```

Una de las **formas más usadas** para reemplazar datos es usar el promedio de las columnas, esto se hace con la función `mean`. O si se quiere un mejor estimador, usamos median.
```
df.fillna(df.median())
```

Por último, Pandas también puede **interporlar** los valores faltanes calculando el valor que puede haber existido en el medio.
```py
df_d = pd.concat([df[['d']], df[['d']].interpolate()],axis=1)
df_d.columns = ['d_antes','d_interpolado']
df_d
```

## Group by

La funcion `Group by` permite agrupar atravez de una serie de elemetos y sobre este aplicar diversas funciones.

```py
import pandas as pd
import numpy as np
# seaborn es una base de datos que esta dentro de una importante herramienta de visualizacion
import seaborn as sns

df = sns.load_dataset('diamonds')
df

# con gruupby agruparemos los datos de acuerdo a una variable 
df.groupby('cut').mean()
# tambien podemos usar otros estimadores estadisticos como median que no esta sesgado y es mucho las preciso cuando tienes distribuciones con colas muy largas
df.groupby('cut').median()

# podemos hacer uso de este tipo de funciones a niveld e columnas como 'count' que contara los datos
df.groupby('cut')['carat'].count()
# pero tambien podemos extraer el valor maximo
df.groupby('cut')['carat'].max()
# y tambien podemos extraer el valor minimo
df.groupby('cut')['carat'].min()

# funcion para agrupar sobre un parametro
for key_group, group in df.groupby('cut'):
  grouped_price = group['price'].mean()

  print(f'cut: {key_group}, Price: {grouped_price} \n')

# funcion para agrupar sobre varios parametros
# to_frame es para convertir en un dataframe
df.groupby(['cut','color'])['price'].mean().to_frame()
# EStos se convirtio en un dataframe con multiples indices

# Con 'aggregate' podemos definir una lista de las funciones que queremos aplicar 
df.groupby(['cut','color'])['price'].aggregate(['min', np.mean,max])
# con esto obtenemos que por las dos vaiables(indices) por las cuales estamos agrupando y cada una de las funciones que le emos pedido en el agrupamiento son columnas

# nosotros podemos definir nuestras propias funciones para hacer este mismo proceso
# para ello primero crearemos una funcion de ejemplo
def mean_kilo(x):
  return np.mean(x)/1000

# y ahora la agregamos al elemento
df.groupby(['cut','color'])['price'].aggregate(['min', np.mean,max, mean_kilo]).head(10) #pondremos un head para no mostrar todo los elementos

# podemos hacer un diccionario de instrucciones que podemos colocar sobre 'aggregate'
dict_agg = {'carat': [min,max], 'price':[np.mean,mean_kilo]}
df.groupby(['cut','color']).aggregate(dict_agg)
# y con esto logramos tener multiples indices en filas y columnas

# podemos definir una funcion de filtro 
def f_filter(x):
  return mean_kilo(x['price'])>4

df.groupby('cut').filter(f_filter)
# para entender lo que esta sucediendo vamos a utilizar 'unique'
df.groupby('cut').filter(f_filter)['cut'].unique()
# En esta ocacion se filtraron 2 categorias : ['Premium', 'Fair']
# que son los tipos de corte que mas coste elevado tienen en los cortes
```