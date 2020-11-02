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