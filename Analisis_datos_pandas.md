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