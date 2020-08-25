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
```
