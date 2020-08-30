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

- Varibale de Bernoulli
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

## Visualizacion de datos 

```python
import scipy.stats
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Para poder visualizar los graficos en el ambiante de jupyter notebook
%matplotlib inline

df = pd.read_csv('nombre_Del_archivo.csv')
df.columns

# Variables Categoricas
y = df['cuartil-a;o'].apply(lambda x: 'cuartil-' + str(int(x)))
# Diagrama de barras
# El orden de las barras python los organiza empezado de mayor frecuencia a menor frecuencia
fig, ax = plt.subplots()
ax.bar(y.value_counts().index, y.value_counts())
ax.set_xlabel('Cuartiles del a;o')
ax.set_ylabel('Frecuencia')

# Se;alar un cuartil en particular
fig, ax = plt.subplots()
ax.bar(y.value_counts().index, y.value_counts())
ax.set_xlabel('Cuartiles del a;o')
ax.set_ylabel('Frecuencia')
ax.patches[3].set_facecolor('red')

# Diagrama de pastel
fig, ax = plt.subplots()
ax.pie(y.value_counts(), labels = y.value_counts().index)
# Agregar un titulo
ax.set_title('Diagrama de pie')

# Variables Numericas
y = df['variable']
fig, ax = plt.subplots()
ax.hist(y, bins = 30)
ax.set_xlabel('Viento')
ax.set_ylabel('Frecuencias')
# Mediciones
# c = color de la linea
# linestyle = estilo de linea
plt.axvline(np.mean(y), c = 'r', linestyle = '--', label = 'Promedio')
plt.axvline(np.mean(y)+np.std(y), c = 'k', linestyle = '--', label = '+ 1-desviacion')
plt.axvline(np.mean(y)-np.std(y), c = 'k', linestyle = '--', label = '- 1-desviacion')
ax.legend()
```

### Boxplot y scatterplot

```python
# Boxplot
y = df['variable_de_interes']
fig, ax = plt.subplots()
ax.boxplot(x = y)
# Boxplot que permita mapear el conportamiento de 2 variables
sns.boxpot(x = 'primera_variable', y = 'segunda_varible', data= df)

# Scatterplot
# Visualizacion de puntos
fig, ax = plt.subplots()
ax.scatter(df['varible_uno'], df['varible_dos'])
# La visualizacion de puntos al tener tantos valores puede ser un poco confusa para ello se puede utilizar un parametro
# El parametro se llama alpha que ayuda a difuminar los puntos y permitir visualizar mas claramente la concentracion de los datos.
ax.scatter(df['varible_uno'], df['varible_dos'], alpha = 0.03)
ax.title('Distribucion conjunta')

# Para agregarle color con gaussian_kde
from scipy.stats import gaussian_kde
xy = np.vstack(df['varible_uno'], df['varible_dos'])
z = gaussian_kde(xy)(xy)
fig, ax = plt.subplots()
ax.scatter(df['varible_uno'], df['varible_dos'], c=z, label='var1 vs var2')
```

## Teorema de Bayes

El teorema de bayes nos permite inferir la probabilidad de un evento `a` cuando tenemos informacion parcial sobre este evento, condicionado a un segundo evento llamado `b` y la informacion total de la distribucion de probabilidad de este evento `b`.

Se probaran 3 concentos claves:
- Probabilidad univariada
- Probabilidad conjunta bivariada 
- Probabilidad condicional 

Escenario:
Tenemos 10 esferas cada una marcada con un numero de 1 a 3 y un color que puede ser negro o blanco.

CSV
```csv
bola;color;numero
1;blanco;1
2;negro;1
3;negro;1
4;negro;1
5;blanco;2
6;negro;2
7;negro;2
8;blanco;3
9;blanco;3
10;negro;3
```

Python
```python
import scipy.stats
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

df = pd.read_csv('juego-azar.csv', sep=';')
df.columns

# Probabilidades univariadas
# HAremos un conteo
df.numero.value_counts()
# Para convertir el conteo en probabilidad se divide por el total de casos
df.numero.value_counts()/len(df)
# Calcular la probabilidad univariada de los colores
df.color.value_counts()/len(df)

# Probabilidad conjunta bivariadas
# Realizamos una agrupacion con groupby() y un conteo con size()
df.groupby(['numero', 'color']).size()
# Para convertirlo en probabilidades
df.groupby(['numero', 'color']).size()/len(df)

# Probabilidad condicional 
# P(A|B) = P('B'|2) = 1/3 = El numero de esferas blancas/ El numero total de esferas con el numero 2
1/3

# Teorema de Bayes
# La utilidad de este teorema es para derivar analisis sobre 'A'(que es un evento particular) cuando no conocemos sus probabilidades individuales univariadas P(A)
# Pero si tenemos informacion sobre el elemento condicionado P(A|B) y algunas probabilidades asociado a 'B' que sera P(B)
# EL teorema de bayes nos permite llegar a la probabilidad de A con esta formula similar:
#P(blanco) = P(p_blanca|1)*p(1) + P(p_blanca|2)*p(2) + P(p_blanca|3)*p(3)
p_blanco =  (1/4)*(4/10) + (1/3)*(3/10) + (2/3)*(3/10)
p_blanco

# Para una representacion mas visual
pd.crosstab(index=df.color, columns=df.numero, margins=True)/len(df)
```

## Funciones de distribución discreta y continua

### Distribuciones discretas

Cuando estamos habalndo de distribuciones discretas todo el **rango** de la funcion debe cumplir y contener a todos lo valores de `X` y cada uno de los valores de x no debe superar el valor de 1.

El calculo de **probabilidad** de la variable aleatoria `X` sera puntualmente una probabilidad de `P(xi)` en la que `xi` ya es un valor puntual.

**Calculo de probabilidad acumulada** es la suma de las probabilidades de tener una valor igual o menor a un `xi`.

**Regla de completitud de Espacio** que es contemplar todos los valores posibles que puede tomar la variable aleatoria `X`, luego la sumatoria de todas la probabilidades del rango, de los diferentes valores que tiene x, y debe sumar simepre 1.

Las medidas de tentecia central para una variable aleatoria como **Valor esperado** o promedio.

La desviacion estandar que en este caso la llamaremos **Varianza**, que es cuadrado de las diferencia entre la media su valor `X`.

Los elementos de **Distribuciones discretas** se tiene que validar dentro de una funcion de **densidad continua**.

El **valor esperado** al igual que la **varianza** cumplen una serie de caracteristicas y una forma especifica a la hora de calcularse.

```python
import scipy.stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from scipy.stats import binom

# P es la probabilidad de exito
# n es el numero de intentos para obtener el numero dado de exitos.

p = 0.3
n = 8
x = list(range(0,9))
# y contendra las probabilidades asociadas a los valores de x
y = list([])

for i in x:
    # binom.pmf nos va a permitir calcular para x particulas su probabilidad asociada
    # Esta funcion recibe como parametro p y el numero de intentos
    y.append(binom.pmf(i, p=p, n=n))
    
# Generamos una grafica de esta probabilidades 
fig, ax = plt.subplots()
ax.bar(x,y)
ax.set_ylabel('Probabilidad discreta')
# El grafico contiene la distribucion de probabilidad de la variable y las alturas de dischas probabilidades nunca son superiores a 1 ni inferiores a 0

# Corroborar Regla de completitud de Espacio, es decir que la suma de todas sus probabilidades de como resultado 1
np.sum(y)

# media 
# Utilizando numpy usaremos el promedio ponderado, esto es por que debemos calcular el valor que va a tomar cada uno de los x de esta dritribucion ponderada por su probabilidad
media = np.average(x, weights = y)
# Varianza
varianza = np.average(((x - media)**2), weights = y)

# Para agregarlo al grafico 
fig, ax = plt.subplots()
ax.bar(x,y)
ax.set_ylabel('Probabilidad discreta')
ax.axvline(x = media, c = 'r', linestyle = '--', label = 'Valor Esperado')
# Dentro de una distribucion normal encontramos que la gran mayoria de los valores en una distribucion caen dentro de los primeros 3 sigma a la izquierda y 3 sigma a la derecha de la media.
# El concepto de six-sigma donde se espera que caigan el 99% de los datos 
ax.axvline(x = media + 3*np.sqrt(varianza), c = 'r', linestyle = '--', label = 'Desviacion Estandar')
ax.legend()
```

### Distribucion continua 

Las **distribuciones de probabilidad continuas**, como la distribución normal, describen valores en un rango o escala y se muestran como figuras sólidas en la galería de distribuciones. Las distribuciones continuas son en realidad abstracciones matemáticas, ya que suponen la existencia de cada valor intermedio posible entre dos números. Es decir, una distribución continua asume que hay un número infinito de valores entre dos puntos de la distribución.

Curtosis:
Nos da indicios de como están distribuidos los datos.

- Si los datos se son mas uniformes y se acercan mas a la media entonces estamos en presencia de una distribución leptocúrtica (coeficiente de curtosis >0)
- Si los datos están muy dispersos y la curva no presenta una cima pronunciada, estamos en presencia de una distribución platicúrtica (coef. de curtosis < 0)
- Si los datos presentan un comportamientos normal la curtosis es igual a 0 (mesocúrtica)

Simetría
La simetría hace referencia a que tan iguales son las dos partes de la distribución.

- Si la distribución es simétrica sus Medidas de tendencia central (media, mediana y moda) serán iguales.

```python
import scipy.stats
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
from scipy.stats import binom
from scipy.stats import norm

# Probabilidad continua
N = 10000

x = list(range(0,N+1))
y = list([])

for i in x:
   y.append(binom.pmf(i, p=0.3, n= N))
    
fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_title('Probabilidad continua')

# Porbabilidad acumulada
for i in x:
    y.append(binom.cdf(i, p=0.3, n= N))
    
fig, ax = plt.subplots()
ax.plot(x,y)
ax.set_title('Probabilidad continua')

mean, var, skew, kurt = norm.stats(moments = 'mvsk')
```

## Distribuciones de mayor aplicación discretas y continuas

### Discretas

1. Distribucion de **Bernoulli** (Experimento Binario asociado a exito o fracaso)

Experimento: Lanzamiento de UNA moneda, Número de caras obtenidas, es una variable aleatoria (un valor numérico que está afectado por el azar.)
Fenómeno o experimento que puede resultar en uno solo de dos posibles resultados, llamados genéricamente ACIERTO (A) o FRACASO (F).
La probabilidad de acierto p es conocida y por ende la de fracaso que será (1 − p) = q.

```python
# Bernoulli
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
import seaborn as sns
%matplotlib inline

p = 0.3
data = bernoulli.rvs(p, size=100)
mean, var, skew, kurt = bernoulli.stats(p, moments='mvsk')
mean, var, skew, kurt
# Ver la forma de la distribucion
ax = sns.distplot(data, bins=30, kde = False, color = 'blue')
ax.set(xlabel= 'Distribucion Bernoulli', ylabel='Frecuencia')
ax.axvline(x=mean, linestyle='--', label = 'Media')
```

2. Distribucion **Binomial**: Numero de exitos x en N ensayos.

Lanzamiento de MUCHAS monedas, una tras otra.
Cuando lanzamos una moneda justa 10 veces, cual es el más probable número de caras?
Lo más probable es que los lanzamientos se distribuyan de igual manera entre caras y sellos, es decir 5 caras y 5 sellos.

```python
# Binomial
import matplotlib.pyplot as plt
from scipy.stats import binom
import seaborn as sns
%matplotlib inline

p = 0.3
# variable de exito
n = 10
data = binom.rvs(p=p, n=n, size=100)
mean, var, skew, kurt = binom.stats(p=p,n=n, moments='mvsk')
mean, var, skew, kurt
# Graficamente
ax = sns.distplot(data, bins=30, kde = False, color = 'blue')
ax.set(xlabel= 'Distribucion Binomial', ylabel='Frecuencia')
ax.axvline(x=mean, linestyle='--', label = 'Media')
ax.legend()
```

3. Distribucion **Geometrica**: Numero de ensayos x hasta 1 exitos.


4. Distribucion **Binomial Negativa**: Numero de ensayos x hasta el K-esimo exito.

Se realizan repeticiones independientes de un proceso Bernoulli, hasta obtener “k” aciertos.
Interesa determinar la probabilidad de que se requieran “x” repeticiones para obtener los k aciertos.

```python
# Geometrica
import matplotlib.pyplot as plt
# La geometrica es un caso particular de la distribucion binomial negativa
from scipy.stats import nbinom
import seaborn as sns
%matplotlib inline

p = 0.3
n = 10
data = nbinom.rvs(p=p, n=n, size=100)
mean, var, skew, kurt = nbinom.stats(p=p,n=n, moments='mvsk')
mean, var, skew, kurt
# Graficamente
ax = sns.distplot(data, bins=30, kde = False, color = 'blue')
ax.set(xlabel= 'Distribucion Binomial Negativa', ylabel='Frecuencia')
ax.axvline(x=mean, linestyle='--', label = 'Media')
ax.legend()
```

5. Distribucion de **Poisson**: Numero de llegdas en N a una longitud de tiempo.

Una binomial se aproxima a una Poisson cuando la probabilidad de éxito es baja

Se asocia con fenómenos o sucesos deﬁnidos en determinados intervalos de tiempo y/o regiones de espacio.

La probabilidad de que el fenómeno suceda por lo menos una vez, es directamente proporcional al tamaño del intervalo de tiempo y/o región espacial.

La probabilidad de que el fenómeno ocurra más de una vez, en intervalo y/o regiones relativamente pequeños es tan pequeña que se puede despreciar.


```python
# Poisson
import matplotlib.pyplot as plt
from scipy.stats import poisson
import seaborn as sns
%matplotlib inline

lamda_p = 100
# el parametro mu esta asociada a la media
data = poisson.rvs(mu = lamda_p, size=100)
mean, var, skew, kurt = poisson.stats(mu= lamda_p, moments='mvsk')
mean, var, skew, kurt
# Graficamente
ax = sns.distplot(data, bins=30, kde = False, color = 'blue')
ax.set(xlabel= 'Distribucion Poisson', ylabel='Frecuencia')
ax.axvline(x=mean, linestyle='--', label = 'Media')
ax.legend()
```

### Continuas

- Distribucion **Exponencial**

Es el caso inverso de la funcion de poisson, es decir, en poisson condabamos numero de eventos * unidad de tiempo y en exponencial vamos a contar el tiempo que nos toca llegar a uno de esos eventos.

Utilizada generalmente para análisis de fiabilidad, p.e: probabilidad de que un componente falle transcurrido una cierta cantidad de tiempo. Investiguen sobre la “perdida de memoria” de la distribución exponencial.

```python
# Exponencial
import matplotlib.pyplot as plt
from scipy.stats import expon
import seaborn as sns
%matplotlib inline

data = expon.rvs(size=100000)
mean, var, skew, kurt = expon.stats(moments = 'mvsk')
# Graficamente
ax = sns.distplot(data, bins=500, kde = False, color = 'blue')
ax.set(xlabel= 'Distribucion Exponencial', ylabel='Frecuencia')
ax.axvline(x=mean, linestyle='--', label = 'Media')
ax.legend()
```

- Distribucion **Normal**

dadas sus características, se utiliza para inferencia estadística, es decir, estimar/evaluar parámetros de toda una población, basados en una muestra. Aquí es donde se utilizan los famosos intervalos de confianza. Investiguen sobre las “pruebas de hipótesis”.

```python
# Normal
import matplotlib.pyplot as plt
from scipy.stats import norm
import seaborn as sns
%matplotlib inline

# Por defecto la funcion normal tiene una media de 0 y una varianza de 1
data = norm.rvs(size=10000000)
mean, var, skew, kurt = norm.stats(moments = 'mvsk')
# Graficamente
ax = sns.distplot(data, bins=500, kde = False, color = 'blue')
ax.set(xlabel= 'Distribucion Normal Estandar', ylabel='Frecuencia')
ax.axvline(x=mean, linestyle='--', label = 'Media')
ax.legend()
```

- Distribucion **Uniforme**

Asume que cada uno de los eventos estan distribuidos con una misma probabilidad.

se utiliza generalmente en el ámbito de simulación, por ejemplo “creación” de escenarios aleatorios, números aleatorios, etc.

```python
# Uniforme
import matplotlib.pyplot as plt
from scipy.stats import uniform
import seaborn as sns
%matplotlib inline

data = uniform.rvs(size=10000000)
mean, var, skew, kurt = uniform.stats(moments = 'mvsk')
# Graficamente
ax = sns.distplot(data, bins=500, kde = False, color = 'blue')
ax.set(xlabel= 'Distribucion Uniforme 0 - 1', ylabel='Frecuencia')
ax.axvline(x=mean, linestyle='--', label = 'Media')
ax.legend()
```

## Estandarización, covarianza y correlación

### Estandarizacion

1. **Centrar** la variable: restar su media a cada uno de los valores originales.

2. **Reducir**la variable: dividir todos sus valores por la desviacion.

El **resultado** de una variable estandarizada va a ser una variable aliatoria que va  a tener un valor esperado 0 y una varianza o desviacion estandar igual a 1.

El efecto de estandarizar nos va a permitir llevar nuestra variable de una dimencion especifica a una variable adimencional.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

df = pd.read_csv('iris-data.csv', index_col=0)

df.columns

df.tipo_flor.value_counts()

# Original
y = df['lar.petalo']
fig, ax = plt.subplots()
ax.set_title('Variable Original')
ax.hist(y, bins = 30)
ax.axvline(x= np.mean(y), c='k', label='media', linestyle='--')
ax.axvline(x= np.mean(y) + np.std(y), c='r', label='desviacion estandar', linestyle='--')
ax.legend()   

# Estandarizacion de una variable
# 1. Centrar la variable: restar su media a cada uno de los valores originales. 
# 2. Reducir la variable: dividir todos sus valores por la desviacion.
y = df['lar.petalo']
fig, ax = plt.subplots()
ax.set_title('Variable Estandarizada')
# Para estandariazar debemos restar a cada valor de 'y' su media.
# Y despues dividiremos cada uno de los valores de 'y' (que han sido restados en su media) sobre la desviacion.
ax.hist((y - np.mean(y))/np.std(y), bins = 30)
ax.axvline(x= np.mean(np.mean(y - np.mean(y))/np.std(y)), c='k', label='media', linestyle='--')
ax.axvline(x= np.mean(np.mean(y - np.mean(y))/np.std(y)) + np.std((y - np.mean(y))/np.std(y)), c='r', label='desviacion estandar', linestyle='--')
ax.legend() 
```
### Covarianza y correlacion

Ambas miden el valor de la relacion **lineal** entre dos variables aleatoria `X` y `Y`

- **Convarianza**

Sin embargo a diferencia de la correlacion, la **covarianza** nos hablara unicamente de la direccion de esta relacion.

    - Mide la **direccion** (signo) de la relacion entre X y Y
    - Magnitud **no estandarizada**
    - Rango `Cov(X)=[-infinito, infinito]`

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

# Covarianza
fig, ax = plt.subplots()
ax.scatter(df['lar.petalo'], df['lar.sepalo'], alpha = 0.7)
ax.set_xlabel('lar.petalo')
ax.set_ylabel('lar.sepalo')
# Las escalas que tiene el grafico aveces no son las que tiene originalmente, paar ello podemos utilizar ax.autoscale() para garantizar que la variable conserva las escalas que tiene originalmente
ax.autoscale()
```

- **Correlacion**

Mientras que la **correlacion** nos permitira entender tanto la direccion de la relacion como la fuerza que tiene. La correlacion entonces sera un valor entre -1 y 1, en donde mas cercano a -1 estaremos mas cerca de una correlacion inversa perfecta y las cercano a 1 estaremos mas cerca de una correlacion directa perfecta entre las dos variables X y Y.

    - Mide direccion (signo) de la relacion entre X y Y
    - Mide la **fuerza** (magnitud **estandarizada**)
    - Rango Cov(X) = [-1,1]
    - Relacion lineal perfecta = -1 o 1

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

%matplotlib inline

# Correlacion
np.cov(df['lar.petalo'], df['lar.sepalo'])
# Vamos a pedir a pandas que nos genere la correlacion entre todas las variables al interior del dataset
df.corr(method= 'spearman')
# En esta caso queremos buscar la correlacion entre df['lar.petalo'] y df['lar.sepalo'] la cual es una asociacion (0.881898) muy cercana a 1(1 es el valor mazimo)
# Hay otras formas de medir la correlacion como como kendal
df.corr(method= 'kendall')
# Pero esta no va a medir correlaciones lineales necesariamente y por eso pueden variar en su magnitud

# Correlacion de forma mas grafica
corr = df.corr(method= 'kendall')
sns.heatmap(corr, xticklabels = corr.columns, yticklabels = corr.columns)
# Hora se puede ver graficamente y de forma mas puntual que variables tienen una correlacion con una magnitud mucho mas fuerte negativa(las mas oscuras) o una correlacion mucho mas fuerte positiva cercana a 1 ( las mas claras)
# si la correlacion es igual a cero entronces es una correlacion nula o inexistente
```

## Estimadores a traves de datos

Criterios para seleccion de un estimador:

1. Que sea **centrado**, es decir, que el valor esperado del estimador tenga como resultado el valor del parametro que queremos calcular.

2. De **minima varianza** o el parametro que ofrezca la menor varianza posible.

3. Es deseable que tenga una relacion **lineal** entre el parametro que quiere estimar.

```python
import sklearn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy import stats
import seaborn as sns
from scipy.stats import norm
%matplotlib inline

# Se va simular que se toma una muestra de la distribucion normal y que la muestra tuvo valor 3
x1 = 3
# Como no conocemos lo valores poblacionales de esta distribucion vamos a generar una serie de hipotesis
# Vamos a decir que el parametro poblacional podria estimarse con mu1 = 4 o con mu2 = 7 
# Y se calculara la probabilidad de haber obtenido esta muestra bajo estas hipotesis del parametro poblacional 
mu1 = 4
mu2 = 7
sigma = 1
# sigma sera la desviacion estandar que debemos conocer de antemano 
sigma = 1
# y pediremos a esta funcion entonces la densiti probabiliti function
p_muestra = norm.pdf(x1,mu2, sigma)
p_muestra

# En esta escenario estamos muestrando dos valores en lugar de uno solo
# Queremos buscar la probabilidad conjunta de que ocurrieran estos 2 casos
x1 = 3
x2 = 10
mu1 = 4
mu2 = 7
sigma = 1
sigma = 1
p_muestra = norm.pdf(x1,mu2, sigma) * norm.pdf(x2,mu2, sigma)
p_muestra

# Generaremos una muestra mas grande
muestra_10 = norm.rvs(5, sigma, size = 10)
y = list([])
for i in range(10):
    y.append(3000)
# Visualmente
data1 = norm.rvs(mu1, sigma, size = 100000)
data2 = norm.rvs(mu2, sigma, size = 100000)
# Normalmente en la grafica apareceran a escala de probabilidad, si quisieras que lo tome como frecuencian entonces tienes que agregar el parametro kde=False
ax = sns.distplot(data1, bins = 50, color = 'blue', kde = False)
ax.set(xlabel = 'Distribucion normal mu1', ylabel = 'Frecuencia')

ax = sns.distplot(data2, bins = 50, color = 'red', kde = False)
ax.set(xlabel = 'Distribucion normal mu1', ylabel = 'Frecuencia')

ax.scatter(muestra_10, y, c='k')
# Como resultado se puede observar como la muestra puede pertenecer con mayor o menor porbabilidad a alguna de las dos hipotesis que se planeo sobre el parametro poblacional 
```

## Estimadores de maxima verosimilitud

Estimadores de maxima verosimilitud son estimadores que han sido calculados maximizando la funcion de verosimilitud o funcion de probabilidad de ocurrencia de la muestra.

Cada vez que tomamos el valor de una poblacion como una muestra debemos clacular su probabilidad asociada.

Entonces los **Estimadores de maxima verosimilitud** seran funciones de la muestra que nos permitan calcular la mejor version(mejor estimador) del parametro estimado.

La forma analitica que hacen uso las funciones de maxmima verosimilitud
```
L(Parametro | Muestra): Likelihood
```

1. El método de máxima verosimilitud consiste en obtener el valor de lambda donde la **L(lambda) sea máximo**.

2. L(lambda) es la **función de máxima verosimilitud**, y está definida como el producto entre todos los valores de la muestra aleatoria evaluados en su función de densidad.

3. En este caso la distribución a estudiar es una **exponencial**, esto es importante, porque TODA distribución exponencial tiene función de densidad = **parametro * e^(parametro*x)**, entonces ya tenemos una función con que trabajar.

4. Se desarrolla la función para después aplicar Logaritmo natural.

5. **Por qué logaritmo natural?** Por dos razones, una tiene que ver con lo práctico de utilizar logaritmos en términos operatorios, pero la mas importante es que, dadas las propiedades de los logaritmos, **la función L(lambda) es máxima en el mismo punto que Ln(L(lambda)). **

6. Se desarrolla la nueva función que se simplifica gracias a las propiedades de los logaritmos.

7. **Por qué se deriva y se iguala a cero?** recuerden que la primera derivada hace referencia a la pendiente de la función, y si la pendiente es cero significa que **estamos en presencia de un mínimo o un máximo**.

8. Acá falto algo, porque para poder asegurar que ese valor de lambda es máximo, se debe derivar por segunda vez, si la segunda derivada es < 0 entonces estamos frente a un máximo, no se puede asegurar nada sin hacer este análisis.

9. Sorpresa! el estimador de max verosimilitud de una función es el promedio muestral.

### Mejores estimadores
- **Promedio muestral**:
Mejor estimador para la media de una distribucion **exponencial**.
Mejor estimador para una distribucion **normal**, **poisson** y **Bernoulli**

- **Varianza Muestral**
Mejor estiamdor para sigma en una distribucion normal

## Distribuciones muestrales

Estumador: Es una funcion de la muestra.

Estadistico: Una funcion que va a involucrar la muestra con el parametro poblacional bajo una hipotesis.

Y sobre esta hipotesis se podra generar utilizando transformaciones, estandariazaciones las distribuciones muestrales para el calculo de probabilidad.

### Parametros pobracional a estimar

- **Media Muestral**: Media, Proporecion o Lambda.
    - **Normal Estandar**: Distribucion con Varianza conocida.
    - **t-Student**: Distribucion con Varianza Desconocida.

- **Varianza Muestral**: Varianza.
    - **Chi-cuandrada**: Distribucion de una sola Varianza.
    - **F Fisher-Snedecor**: Distribucion del Cociente de la Varianza X sobre Varianza Y.

```python
import matplotlib.pyplot as plt
from IPython.core.display import Image
import seaborn as sns
from scipy.stats import t

%matplotlib inline

# Se va a generar una primera muestra de datos
data1 = t.rvs(100, size=1000000)
# Se generara una segunda muestra pero con menos grados de libertad para que se pueda ver como cambia graficamnete
data2 = t.rvs(4, size=1000000)

ax = sns.distplot(data1, bins = 500, kde = False, color= 'red')
ax = sns.distplot(data2, bins = 500, kde = False, color= 'blue')

# Para ver otro grafico de distribucion se utilizara la funcion chi-cuadrada que nos permite identificar la forma del calculo de probabilidad para varianza
from scipy.stats import chi2
data1 = chi2.rvs(5, size=1000000)
data2 = chi2.rvs(15, size=1000000)
ax = sns.distplot(data1, bins = 500, kde = False, color= 'red')
ax = sns.distplot(data2, bins = 500, kde = False, color= 'blue')

# La funcion F nos permite aproximar cocientes de varianzas
from scipy.stats import f

data1 = f.rvs(5, 25, size=1000000)
data2 = f.rvs(15, 25, size=1000000)
ax = sns.distplot(data1, bins = 500, kde = False, color= 'red')
ax = sns.distplot(data2, bins = 500, kde = False, color= 'blue')

# Hacer calculos de probabilidad 
# probabilidad de tener un 4 en esta distribucion
f.pdf(4, 15, 25)
# Probabilidad acumulada 
f.cdf(4, 15, 25)
# Pra ahacer calculos inversos o encontrar aquel valor que acumule una cierta probabilidad
f.ppf(0.9988900520089906, 15, 25)
```

## Teorema del limite central

Lasuma de `n` variables aleatorias **independientes, con un n > 30** tiende a una distribucion normla o la curva de campana incluso si las variables aleatorias originales no se distribuyen como una normal.

Teorema del limite central nos permitira aproximar la funcion de distribucion de una variable aleatoria de la cual no conocemos previamente su distribucion.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

from scipy.stats import expon
from scipy.stats import uniform

# Definamos una pobracion sobre la cual vamos de derivar analisis 
poblacion = pd.DataFrame()
poblacion['numbers'] = expon.rvs(40, size = 100000)
# Vamos a formar un grafico utilizando pandas
poblacion['numbers'].hist(bins = 100)

# Muestra de la poblacion que hemos definido
muestra_promedio = []
tamano = 5000
for i in range(0, tamano):
    muestra_promedio.append(poblacion.sample(n=100).mean().values[0])
# Genenrar el grafico
fig, ax = plt.subplots()
ax.hist(muestra_promedio, bins = 50 , alpha = 0.5)
ax.set_xlabel('Valor promedio')
ax.set_ylabel('Frecuencia')
# EL grid nos permite ver la parilla de valores para identificar numeros en la grafica
ax.grid()
```

## Prueba de hipotesis 

Una **prueba de hipotesis** es una regla que especifica si se puede aceptar o rechazar una afirmacion acerca de un **parametro poblacional** (lambda, sigma, mu, etc) dependiendo de la evidencia proporcionada por una muestra de datos.

Los pasos para ahcer una prueba de hipotesis:

1. Identificar el parametro poblacional sobre el cual queremos hacer inferencia.
2. Definir una hipotesis nula(siempre de igualdad =) y una hipotesis alterna (mayor que >, menor que < o diferente que).
3. Identificar el estimador que bamos  ausar para nuestro parametro poblacional(Promedio muestral o varianza muestral).
4. Identificar el estadistico y su distribucion (normal, t-student, chi-cuadrada, F-fisher, etc).
5. Asignar el valor estadistico que va a tener la prueba | H0.
6. Toleracincia al error alfa, valor critico y criterio de rechazo de H0.
7. Conclusion de rechazo o no rechazo de H0 con un margen de error de alfa.

### Caso ejemplo

- La empresa Mustage S.A. esta desarrollando una plataforma para otrorgar credito de bajo monto.
- EL tiempo para completar exitosamente una consulta de informacion de clientes ante las fuentes de buro **no debe ser superior a 30 segundos** en **promedio**.
- Muestra de **n = 50** clientes consultados.
- La empresa esta dispuesta a asumir un error del 5% en la prueba.

```python
import pandas as pd
import numpy as np
%matplotlib inline
import seaborn as sns
from scipy.stats import expon
from scipy.stats import norm
from scipy.stats import uniform

muestra = [42, 35, 29, 45, 41, 57, 54, 47, 48, 56, 47, 35, 52, 31, 52, 55, 57, 58, 26, 29, 32, 37, 32, 34, 48, 20, 48, 51, 27, 24, 39, 40, 31, 34, 23, 24, 41, 58, 44, 48, 31, 23, 27, 55, 43, 47, 30, 57, 38, 51]
# Hipotesis
media, var, skew, kurt = expon.stats(scale = 30, moments = 'mvsk')
# Paso 1: parametro lambda
# Paso 2: HP
mu = 30
mu > 30
# Paso 3: Mejor estimador
# Estimador 
# Paso 4: Distribucion
promedio = np.mean(muestra)
promedio
# Paso 5:
# Teorema del limite Central = (Promedio-media)/(Desviación Estandar /(n)^(1/2))
z = (promedio - mu)/np.sqrt(var/50)
# Paso 6
alpha = 0.05
# Criterios de rechazo
data_norm = norm.rvs(size=100000)
ax = sns.distplot(data_norm, bins = 500, kde = False, color = 'blue')
ax.set_title('Distribucion normal')

# Para poder visualizar las regiones de rechazo y fallo critico 
valor_critico = norm.ppf(1-alpha, loc = 0, scale = 1)
# Si alpha es la probabilidad de error 1 - alpha nos dara la probabilidad de no error o valor de tolerancia
ax = sns.distplot(data_norm, bins = 500, kde = False, color = 'blue')
ax.set_title('Distribucion normal')
ax.axvline(x = valor_critico, linestyle = '--', label = 'valor cirtico')
ax.axvline(x = z, linestyle = '--', label = 'valor estadistico', color='k')
ax.legend()
# Las pruebas de hipotesis nos han permitido evidenciar que tan probable es que nuestro valor poblacional mu tenga un valor de 30 o superior dada la muestra
# En este caso tenemos una prueba de hipotesis de =>
```

Con esto podemos concluir en el caso de Mustage, estaria a favor de que el tiempo que le toma a una persona logearse y poder acceder a un credito es mayor que lor requerimentos que necesitan sobre el provedor.

## Errores estadisticos

Siempre se va a trabajar con la hipotesis nula y alterna por lo tanto tenemos siempre la opcion de aceptar la hipotesis y en contraste saber si la hipotesis era o no verdadera.

- **Error Tipo I**
**Rechazar H0** cuando en realidad es cierta
`Alpha = P(Rechazar H0 | H0 es cierta)`

- **Error Tipo II**
**No rechazar H0** cuando en realidad es falsa
`Beta = P(No Rechazar H0 | H0 es falsa)`

```python
import pandas as pd
import numpy as np
import seaborn as sns
from scipy.stats import norm

muestra = [42, 35, 29, 45, 41, 57, 54, 47, 48, 56, 47, 35, 52, 31, 52, 55, 57, 58, 26, 29, 32, 37, 32, 34, 48, 20, 48, 51, 27, 24, 39, 40, 31, 34, 23, 24, 41, 58, 44, 48, 31, 23, 27, 55, 43, 47, 30, 57, 38, 51]

mu1 = 37
mu2 = 42
promedio = np.mean(muestra)

desv = 2

z_1 = (promedio - mu1)/desv
z_2 = (promedio - mu1)/desv

data1 = norm.rvs(loc = mu1, scale = desv, size=1000000)
data2 = norm.rvs(loc = mu2, scale = desv, size=1000000)

ax = sns.distplot(data1, bins = 500, kde = True, color = 'blue')
ax = sns.distplot(data2, bins = 500, kde = True, color = 'red')
ax.axvline(x = promedio, c='k', linestyle = '--', label = 'Promedio muestral')
ax.legend()
# Nuestro promedio parece se mas probable bajo la hipotesis de que la media sige un valor igual a 42 y no a 37

# Generar los valores estadisticos a los errores 
# Error tipo 1: p rechazar h0 cuando esta es verdadera
p_prom_mu1 = norm.cdf(z_1)
1 - p_prom_mu1
# La probabilidad de rechazar la hipotesis nula cuando es verdadera sera de 3%

# Error tipo 2: probabilidad de no rechazar h0 cuando esta es falsa
p_prom_mu2 = norm.cdf(z_2)
# De esta forma encontramos que la probabilidad de equivocarnos al no rechazar h0 cuando esta es falsa sera de 25%
# Sendo alpha la probabilidad de equivocarnos al no rechazar h0 siendo esta verdadera es deseable que este sea el error que tienda a 0 
# Tambien tenemos en contraposision la potencia de la prueba que 1 - beta o el error tipo 2
# sin embargo beta no es facilmente calculable por lo cual se suele optimizar el error asociado al alpha (a no rechazar la hipotesis nula cuando esta es verdadera)
```