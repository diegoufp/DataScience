# Fundamentos de algebra lineal con python

El **álgebra lineal** es una rama de las matemáticas que estudia conceptos tales como vectores, matrices, espacio dual, sistemas de ecuaciones lineales y en su enfoque de manera más formal, espacios vectoriales y sus transformaciones lineales.

## Anaconda + Python, Creación de un entorno y actualización de paquetes 

**Por qué Python para Data Science**

Si ya conoces el lenguaje Python no hace falta que te cuente porque es el elegido en la industria para dar vida a los proyectos de Data Science. Pero si no estás familiarizado con Python estas son algunas de sus características:

- Es poderoso y sencillo
- Tiene múltiples paquetes estadísticos y de aprendizaje automático, listos para usar
- Una comunidad muy activa a la que siempre puedes consultar

Y cuenta con muchas más.

**Por qué Anaconda**

Anaconda nos provee de una plataforma muy completa para poder desarrollar nuestros proyectos de Data Science, simplifica la tarea de instalación y configuración de las distintas aplicaciones que necesitaremos usar en nuestro viaje. Podemos utilizarlo tanto por terminal como por interfaz gráfica (GUI). Por el momento avancemos con la segunda opción, es más amigable para quien no está acostumbrado a la línea de comandos.

Algunas ventajas de utilizar Anaconda para tus proyectos son:

- Manejar los entornos de trabajo con Conda (todas las dependencias de librerías se resuelven en el momento de instalación)
- Posibilidad de compartir, colaborar y reproducir los proyectos
- Puedes pasar tu proyecto a producción solo con un click (una vez configurado)

Dentro de las variadas aplicaciones que nos ofrece Anaconda vamos a utilizar Jupyter Notebooks con Python 3.7.

**Instalación**

Para intalar anaconda en la terminal de comandos visitar este [link](https://github.com/diegoufp/DataScience/blob/master/ingenieria%20de%20datos.md#anaconda "link")

Para realizar la instalación debes seguir los siguientes pasos:

- Ir a `https://www.anaconda.com/distribution/`
- Selecciona tu versión de Sistema Operativo: Windows - macOS - Linux
- Haz click en Descargar/Download “Python 3.7 version” (o click en la versión adecuada para tu CPU 64-bit o 32-bit)

Después de descargar el instalador gráfico, debes abrirlo y seguir las instrucciones que se presentarán en pantalla. Estas son una serie de preguntas para realizar la instalación, las opciones por defecto están bien, no hay necesidad de cambiarlas.

**Iniciando Anaconda**

Una vez que finalizada la instalación debes abrir el programa Anaconda Navigator para que podamos crear el entorno en cual estaremos estudiando y actualizar los paquetes.

Haz click en Environments y despues click en +Create. Se abrirá una ventana para crear un nuevo entorno.

Llena los siguientes campos:

- Name: Platzi - FundamentosAL
- Packages: tilde en Python y del menú desplegable selecciona 3.7

momento para configurar el nuevo entorno y actualizarlo. 

Los paquetes que ves son los que están instalados por defecto, necesitas instalar varios más. Haz click en installed y cambiarlo a not installed.

En el recuadro de search packages pon:

- Jupyter Notebook
- scipy (tambien instalará numpy)
- pillow (libreria para manejo de imágenes)
- imageio (lectura / escritura de imágenes)
- matplotlib (para graficar)
- seaborn (visualizaciones estadísticas)
- scikit-learn (aprendizaje automático - lo usaremos para un ejemplo de PCA)

**Ejercicio**

Instala el paquete seaborn. Es un paquete para visualizar datos.

A mi tambien me paso la primera vez no saber por dónde comenzar, así que si necesitas ayuda aqui te dejo un paso a paso.

1 - Desde Anaconda Navigator, haz click en Environments
2 - Selecciona el entorno donde quieres instalar el paquete (Platzi - FundamentosAL)
3 - Selecciona en el menú desplegable Not Installed
4 - Escribe en el recuadro de búsqueda seaborn
5 - Haz click en el paquete seaborn
6 - Haz click en Apply
7 - Haz click en Apply, pero esta vez en el pop up que aparece para aceptar todas las dependencias.

## Jupyter notebook

```py
# Jupyter Notebook

# para saber la version de python
from platform import python_version
print(python_version())

# con 'CTRL' + '/' podemos convertir un gran texto seleccionado en un comentario
# podemos llamar a una funcion que esta escrito en otro archivo de google colab usando:
# %run "..\\direccion_de_la_funcion\"
```

## Creando las bases, escalares, vectores y matrices. ¿Qué es un tensor? ¿Cómo se representa?

```py
# Un escalar en matematicas no es mas que un numero, solo eso
escalar = 5.678
print(escalar)
# En python un escalar es completamente distinto ya que puede ser:
# Un entero, un punto flotante, un numero complejo, un string, un elemento nulo
escalar_python = True
print(type(escalar_python))

# Escalar, vector , la matriz y el tensor se diferencian en 'los grados de libertad que tenemos para interactuar'
# Un vector es un conjunto de numeros 
# la matriz son multiples vectores apilados, en este caso tiene dos grados de libertad(filas y columnas)
# el tensor son multiples matrices, se mueven entre filas y columnas pero tambien entre matrices.

import numpy as np

vector = np.array([1,2,3,4])
print(vector)

matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)

tensor = np.array([
                   [[1,2,3],[4,5,6],[7,8,9]],
                   [[11,12,13],[14,15,16],[17,18,19]],
                   [[21,22,23],[24,25,26],[27,28,29]]
])
print(tensor)

%matplotlib inline
# decirmos a matplotlib que queremos que nuestros graficos figuren abajo de nuestra celda
import matplotlib.pyplot as plt
# y importamos matplotlib.pyplot que es lo que necesitamos para nuestros graficos 

# ahora le pedimos que nos muestre como imagen:
# la interpolation es como se unen los espacios entre dos numeros, en este caso usaremos 'nearest' que es la mas cercana
plt.imshow(tensor, interpolation='nearest')
plt.show()

# para apreciarlo mejor usaremos un pixelart
pixelart = np.array([
                     [[192,192,192],[128,128,128],[192,192,192],[128,128,128],[192,192,192],[232,12,12],[221,11,10],[210,0,0],[199,1,0],[200,0,0],[189,5,5],[128,128,128],[192,192,192],[128,128,128],[192,192,192],[128,128,128]],
                     [[128,128,128],[192,192,192],[128,128,128],[192,192,192],[221,11,10],[254,0,0],[245,0,10],[245,0,10],[234,0,9],[223,6,14],[223,6,14],[189,5,5],[200,0,2],[210,0,0],[128,128,128],[192,192,192]],
                     [[192,192,192],[128,128,128],[192,192,192],[128,128,128],[98,78,43],[106,82,46],[117,92,51],[197,177,144],[209,189,154],[204,184,149],[27,27,27],[197,177,144],[192,192,192],[128,128,128],[192,192,192],[128,128,128]],
                     [[128,128,128],[192,192,192],[128,128,128],[98,78,43],[213,194,162],[117,92,51],[213,194,162],[214,197,169],[218,199,167],[213,194,162],[47,47,47],[209,189,156],[204,184,149],[197,177,144],[128,128,128],[192,192,192]],
                     [[192,192,192],[128,128,128],[192,192,192],[92,68,30],[218,199,167],[128,100,60],[214,197,169],[218,199,167],[218,199,167],[213,194,162],[208,189,156],[27,27,27],[208,189,156],[203,183,150],[197,177,144],[128,128,128]],
                     [[128,128,128],[192,192,192],[128,128,128],[78,57,26],[92,68,30],[197,177,144],[218,199,167],[213,194,162],[208,189,156],[208,189,156],[27,27,27],[47,47,47],[63,63,63],[27,27,27],[128,128,128],[192,192,192]],
                     [[192,192,192],[128,128,128],[192,192,192],[128,128,128],[192,192,192],[204,184,149],[213,194,162],[209,189,154],[204,184,149],[197,177,144],[204,184,149],[204,184,149],[197,177,144],[128,128,128],[192,192,192],[128,128,128]],
                     [[128,128,128],[192,192,192],[128,128,128],[192,192,192],[221,11,10],[210,0,1],[92,49,224],[200,0,0],[212,0,0],[221,11,10],[42,41,220],[192,192,192],[128,128,128],[192,192,192],[128,128,128],[192,192,192]],
                     [[192,192,192],[128,128,128],[192,192,192],[232,12,12],[254,0,0],[245,0,10],[84,45,214],[245,0,10],[234,0,9],[83,46,201],[210,0,1],[221,11,10],[232,12,12],[128,128,128],[192,192,192],[128,128,128]],
                     [[128,128,128],[192,192,192],[232,12,12],[254,0,0],[245,0,10],[234,0,9],[84,45,214],[92,49,224],[84,45,214],[77,41,189],[234,0,9],[245,0,10],[254,0,0],[221,11,10],[128,128,128],[192,192,192]],
                     [[192,192,192],[128,128,128],[197,177,144],[208,191,161],[245,0,10],[84,45,214],[247,223,61],[92,49,224],[83,46,201],[225,202,47],[67,35,172],[232,1,9],[208,191,161],[197,177,144],[192,192,192],[128,128,128]],
                     [[128,128,128],[192,192,192],[204,184,149],[214,197,169],[197,177,144],[84,45,214],[92,49,224],[84,45,214],[83,46,201],[77,41,189],[67,35,172],[197,177,144],[214,197,171],[204,184,149],[128,128,128],[192,192,192]],
                     [[192,192,192],[128,128,128],[209,189,154],[204,184,149],[84,45,214],[98,55,233],[92,49,224],[83,46,201],[77,41,189],[83,46,201],[77,41,189],[67,34,173],[204,184,149],[209,189,154],[192,192,192],[128,128,128]],
                     [[128,128,128],[192,192,192],[128,128,128],[192,192,192],[84,45,214],[84,45,214],[83,46,201],[192,192,192],[128,128,128],[67,35,172],[67,35,172],[67,35,172],[128,128,128],[192,192,192],[128,128,128],[192,192,192]],
                     [[192,192,192],[128,128,128],[192,192,192],[107,83,45],[117,92,51],[111,86,45],[91,67,29],[128,128,128],[192,192,192],[102,78,40],[111,86,45],[103,80,38],[84,61,27],[128,128,128],[192,192,192],[128,128,128]],
                     [[128,128,128],[192,192,192],[107,83,45],[102,78,40],[96,72,34],[91,67,29],[84,61,27],[192,192,192],[128,128,128],[96,72,34],[91,67,29],[84,61,27],[73,54,21],[65,48,18],[128,128,128],[192,192,192]]

])

plt.imshow(pixelart, interpolation='nearest')
plt.show()
```

## Transposición, suma de matrices y escalares

```py
# vamos a ver como se hacen las suma de matrices y vectores siempre y cuando tengan las mismas dimenciones
# matematicamente hablando 'transponer' un vector o una matriz es cambiar las filas por columnas
# si tenemos un vector fila y los tranponemos obtenemos un vector columna
# si tenemos una matriz 3x2 y la transponemos obtenemos una matriz 2x3

import numpy as np

escalar = 5.679
vector = np.array([3,4,5,6])
matriz = np.array([[1,2],[3,4],[5,6]])
tensor = np.array([
                   [[1,2,3,30],[4,5,6,31],[7,8,9,32]],
                   [[11,12,13,33],[14,15,16,34],[17,18,19,35]],
                   [[21,22,23,36],[24,25,26,37],[27,28,29,38]]
])

# EScribir una traspuesta en python es usar la funcion '.T'
# cuando intenamos usar una traspuesta en un escalar aparecera un error por que el escalar es solo un numero y no tiene dienciones
#escalar_t = escalar.T
# Si usamos la trspuesta en un vector nos devuelve el mismo vector
# a efectos practicos en python no vamos a ver una diferencia entre transponer un vector o no
# salvo que estemos haciendo cuenta
vector_t = vector.T
vector_t
# Al transponer la matriz vemos que cambio de una matriz 3x2 a una 2x3
matriz_t = matriz.T
matriz_t.shape
matriz.shape

# Para los tensores tenemos el mismo tipo de operacion transposicion, solamente que es una generalizacion dado que un tensor posee mas dimeciones que una matriz
tensor_t = tensor.T
# vemos que obtenemos un tensor con 3 filas, 3 columnas y 4 matrices, (4, 3, 3)
tensor_t
# al momento de ver el tensor original vemos que este posee 3 filas, 4 columnas y 3 matrices (3,3,4)
tensor_t.T

# la suma de matrices esta definida matematicamente cuando los objetos tienen  las mismas dimenciones
# si tenemos una matriz de 2x2 y otra de 2x2 y las sumamos, nos dara como resulado una matriz de 2x2 con los valores ya sumados
# SI tramos de hacer la siguiente suma:
A = matriz
B = matriz_t
C = A+B
# al final nos saldra un error por que una matris es de 3x2 y la otra es de 2x3

A = np.array([[1,2],[3,4],[5,6]])
B = np.array([[6,5],[4,3],[2,1]])
C = A+B
print(A)
print(B)
print(C)

# Si intentamos hacer una suma de una matriz con un escalar
D = matriz + escalar
D
# nos devuelve la misma matriz pero el escalar le supo a todos los elementos de la matriz
```

## Suma de matrices y vectores (broadcasting)

```py
# Veremos en que casos es posible sumar matrices y vectores con dimenciones distintas
# eso se puede cuando se cumplen las reglas de python para hacer broadcasting
import numpy as np

escalar = 5.679
vector = np.array([3,4,5])
matriz = np.array([[1,2],[3,4],[5,6]])

# si tratamos de sumar un vector con una matriz en este caso no va a ser posible por que el vector esta en fila
#A = vector + matriz
# Esta suma no es posible por que tenemos un vector con 3 elementos, y una matriz con dos elemenos por 3 vectores
# para poder hacer una suma de una matriz con un vector tiene que tener la misma cantidad de elementos por vector
# en esta ocacion vamos a usar la transpuesta en la matriz para convertirlo a una matriz de 3 elemenos por 2 vectores 
# esto es 'broadcasting' , extender la dimecion de menor tama;o para completar la de mayor tama;o
A = vector + matriz.T
A

# en el caso se sumar un escalar a una matriz tambien es 'broadcasting'
C = matriz + 42
print(C)

D = matriz + np.array([[42],[42],[42]])
print(D)
```

## Producto interno entre una matriz y un vector

```py
# producto interno no es lo mismo que multiplicar una matriz por un vector
import numpy as np

escalar = 5.679
vector = np.array([2,3])
matriz = np.array([[1,2],[3,4],[5,6]])


A = matriz * vector

# el producto interno se escribira como '.dot'
B = matriz.dot(vector)

# cuando hacemos una multiplicacion de un vector (2,) y una matriz (3,2), nos da de resultado una matriz (3,2)
print(A)


# si hacemos el producto interno de la matriz por el vector lo que nos devuelve es un vector de dimecion (3,)
print(B)
# este resultado se da por que en la matris tenemos los valores ([[1,2],[3,4],[5,6]])
# y el el vector tenemos los valores ([2,3])
# entonces la primera operacion seria : 1*2 + 2*3 = 8
# la segunda operacion seria: 3*2 + 4*3 = 18
# y la tercera operacion seria: 5*2 + 6*3 = 28 

# tenemos dos maneras para usar la funcion de producto interno
B = matriz.dot(vector)
C = np.dot(matriz, vector)
print(B)
print(C)

# aparte del producto interno tambin existe el producto externo
C = np.outer(vectorA, vectorB)
# Nos devuelve
array([[4, 6],
       [6, 9]])
# Tambien se puede hacer entre vectores y vector por matriz.
# Lo que realiza basicamente es multplica el primer elemento el vectorA por el primer elemento del vectorB y lo coloca. Luego vuelve a multplicar el primer elemento del vectorA pero esta ves por el segundo elemento del vectorB y asi sucesivamente.

vector = np.array([2,3,5])
print("\nVector: ",vector)

matriz = np.array([[1,2,3], [4, 5, 6], [7, 8, 9]])
print("\nMatriz: ",matriz)

A = matriz.dot(vector)
print("\nmatrizXvector: ",A)

B = vector.dot(matriz)
print("\nvectorXmatriz: ",B)
# Y cómo se puede apreciar… los resultados no son iguales…
```