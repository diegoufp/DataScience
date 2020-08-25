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