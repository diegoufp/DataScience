# Estadistica y Analisis de Datos con Python

## Introduccion

### Python y la estadística
¿Porqué usar pythony no R para estadística?.

R es un lenguaje dedicado a la estadística, python es un lenguaje de propósito general con módulos estadísticos.
R está especializado para estadística y tiene más features que python. Pero cuando se trata de construir complejos piplines para el análisis que mezcla estadística con análisis de imágenes, minería de texto la riqueza de python es invaluable.

La estadística actual requiere una gran cantidad de procesamiento y almacenamiento de información.
Aquí entran los ambientes virtuales.

Los ambientes virtuales como Collabs, Jupyter, facilitan el trabajo en estas variables de volumen y procesamiento, así como el uso de librerías.

libreria [OS](https://docs.python.org/3/library/os.html "OS")

En el ambiente de anaconda se inicia `jupyter notebook`.
```python
# Datos de fuentes locales
import os # Operating Sistem

# El nombre del sistema operativo que estamos usando
os.name

# Directorio activo con el cual estamos trabajando
os.getcwd()

# Listador los documentos del directorio
os.listdir('.')

# Con el metodo chdir podemos modificar la ruta para que sea la nueva ruta de trabajo
path = '/home/sann/Documents/Data Science'
os.chdir(path)
os.getcwd()

import pandas as pd
# Permite cargar una base de datos csv
df = pd.read_csv('elnombre_del_archivo.csv')

# funcion implicita para vear algunos datos de data frame
df.head()
# para ver solo las columnas
df.columns
# para ver cuantos datos y columnas
df.shape

import tensorflow as tf # Es utilizada para procesamiento de igamenes principalmente
# Para instalar tensorflow en conda:
# conda install tensorflow

fashon = tf.keras.datasets.fashion_mnist
(imagenes, categorias) = fashon.load_data()[0]
# Tendra un conjunto de 60000 imagenes de 28 x 28 (en este caso el valor de las columnas es igual a un pixel)
imagenes.shape

# Ver el arreglo de los colores de cada pixel
imagenes[0]

# Estoy viendo el tamaño de mi arreglo y llamo a categoráis o tags para poder generar patrones.
imagenes[0].shape, categorias[0]

```

## Conceptos clave estadistica

### Tipos de datos
- Numericos
continuos, porcentajes y enteros

- Categorios 
Categoricas ordinales(fechas) y clases sin sentido ordinal.

### Medidas de terncencia central
- Media o primedio geometrico y aritmetico
- Mediana
- Moda

### Mediada de dispersion
- Desviacion estandar
Que tanto se alejan uno de los valores x y de su valor promedio.

### Variables

- Deterministico
Asume un valor puntual

- Aleatorio 
Puede tomar una serie de valores que cambian en un rango determinado 

### Probabilidad

- Formula:
```
Casos favorables
---------------- = Probabilidad de Laplace
Casos totales
```

El calculo de probabilidad siempre debe estar dentro del rango de 0 o 1 nunca mayor, nunca menor `0 < P(B) < 1`

```python
import numpy as np
import datetime
from datetime import date
import scipy
import scipy.stats
from scipy.stats import bernoulli
from scipy.stats import binom
import pandas as pd

universo = ['cara', 'sello']
p_cara = 1/2
# La variable bernoulli solo puede tener valor binario 0 y 1
bernoulli.rvs(p=p_cara)
universo[bernoulli.rvs(p=p_cara)]
# Repetir el experimento
bernoulli.rvs(p=p_cara, size = 10)
# Distribucion binomial que es una suma de n experimento independientes de bernoulli
sum(bernoulli.rvs(p=p_cara, size = 10))
# La Dsitribucion binomial tambien se puede hacer con la libreria scipy.stats modulo binom
binom.rvs(p=p_cara, n = 10)
# Y se puede repetir n veces el experimento
binom.rvs(p=p_cara, n = 10, size= 100)
# Creamos un df con pandas
pd.Series(binom.rvs(p=p_cara, n = 10, size= 100))
# Para buscar la frecuencia de repeticion de valorte sen pandas usamos value_counts()
pd.Series(binom.rvs(p=p_cara, n = 10, size= 100)).value_counts()
# Y si los queremos convertirlos a probabilidad simplemente los tenemos que dividir sobre el total de casos 
pd.Series(binom.rvs(p=p_cara, n = 10, size= 100)).value_counts()/100

# Medidas de tendencia central

df = pd.read_csv('nombre_del_archivo.csv')
df.columns
y = df['una_de_las_columnas'].values
# Limpiar los valores de 0
y = np.where(y == 0, 1, y)
# El minimo
np.min(y)
# El maximo
np.mx(y)
# promedio: sum(yi)/n
np.mean(y)
# o
np.sum(y)/len(y)
# La medio geometrica
scipy.stats.mstats.hmean(y)
# La mediana
np.median(y)
# la moda no viene no esta tendro de numpy asi que debemos declararla 
# moda = valor de 'y' con la maxima freciencia 
moda = np.nan
valores, conteo_valores = np.unique(y, return_counts = True)
pos = np.argmax(conteo_valores)
moda = valores[pos]

# desviacion estantar
np.std(y)

# Revisiones
# Lo que se quiere ver es que tanto cambian las medidas de tendecia central cuando se agregan valores extremos
y_alterado = y.copy()
y_alterado[ y_alterado == max(y_alterado) == 100000 ]
# Esto demuestra de la media es una de las medidas que se ve afectada por valores extremos
print(np.median(y))
print(np.mean(y))
print(np.mean(y_alterado))
# En el caso de la mediana nos da exactamente el mismo valor
# Hay medidas que pueden o no verse afectadas por valores extremos
print(np.median(y))
print(np.median(y_alterado))
```
## Diagramas de frecuencia 

Los Diagramas de freciencia o Histogramas son representaciones de las categorias y de los numero que puede tomar una variable aleatoria.

### Variables para Histogramas
- Variables categoricas: Tablas de frecuencia

- Variables numericas: Percentiles, Deciles, Quintiles y Quartiles, outliers o valores extremos

En este artículo les ayudara a entender el por qué se usar el 1.5 como factor de escalamiento del [IQR](https://medium.com/mytake/why-1-5-in-iqr-method-of-outlier-detection-5d07fdc82097 "IQR")

```python
import pandas as pd
import numpy as np
import scipy
import scipy.stats
import matplotlib.pyplot as plt # va a permitir graficar 

df = pd.read_csv('nombre_del_archivo.csv')
df.columns
# frecuencias para variables categoricas
ycat = df['una_columna']
# Transformar la varibles en un valor categorico
ycat = ycat.apply(lambda x: 'Cat-' + str(int(x)))
# Encontrar las frecuencias asociadas a la primera varibale 
valores, conteo_freq = np.unique(ycat, return_counts = True)
valores, conteo_freq
# Dise;ar una tabla con los valores encontrados 
tabla_frecuencias = dict(zip(valores, conteo_freq))
tabla_frecuencias

# Variable numerica
ynum = df['una_de_las_variables'].copy()
np.min(ynum), np.max(ynum)
# Identificar los valores que acumulan un x porciento de probabilidad en los datos
np.percentile(ynum, q=100) # <- esto es igual a np.max(ynum)
np.percentile(ynum, q=0) # <- esto es igual a np.min(ynum)
np.percentile(ynum, q=50) # <- esto es igual a la mediana np.median(ynum)

# Identificar los cuartiles
# Los cuales son una medida muy similar a los percentiles pero cuando estamos parados en unos valores puntules acumulan cierta probabilidad 
valores = [0,25,50,75,100]
np.percentile(ynum, q= valores)

# Podemos llamr quintiles a aquellos valores que dividen la varible en 5 grupos 
valores = [0,20,40,60,80,100]
np.percentile(ynum, q= valores)

# Deciles
valores = list(range(0,110,10))
np.percentile(ynum, q= valores)

# Valores atipicos estan muy asociados a los percentiles
y = df['variable_de_interes']
# describe es una funcion que permite en una sola linea ver la cuenta, media, desviacion estandar y los cuartiles
y.describe()

# outlier = valor atipico
# todo todo valor que caiga por fuera del rango rega considerado un aoutlier
Q1 = np.percentile(ynum, q = 25)
Q3 = np.percentile(ynum, q = 75)

RI = Q3 - Q1
limit_inf = Q1-1.5*RI
limit_sup = Q3+1.5*RI

[limit_inf, limit_sup]

# Para hacer un histograma haremos uso de la libreria matplotlib.pyplot
%matplotlib inline
plt.hist(y)

```
