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

**funciones en archivos diferentes de jupyter notebook**

Crearemos un carpeta en jupyter nootbook y crearemos un archivo de python3 en el cual pondremos nuestra funcion.

Ahora podemos llamar a esta funcion desde otros archivo de notebook.

tenemos que escribir:
```py
# entre comillas sera la direccion donde se encuentra el archivo de la funcion.
%run './funciones_auxiliares/graficarVectores.ipynb'
```


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

## Producto interno entre dos matrices

```py
import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
B = np.array([[2,3],[5,7],[11,13]])

print(A.shape) # (4, 3)
print(B.shape) # (3, 2)

# A = (4, 3) y B = (3, 2)
# En este caso el '3' del A y el 3 del B son iguales y estan alineados
C = A.dot(B)
# en el orden operacion B = (3, 2), (4, 3)
# la dimecion de B '2' y A '4' no son iguales y no estan alineados por lo cual sale un error al tratar de hacer un producto interno
#D = B.dot(A)

print(A)
print(B)
print(C)
# A = [[ 1  2  3]
#     [ 4  5  6]
#     [ 7  8  9]
#     [10 11 12]]

# B = [[ 2  3]
#     [ 5  7]
#     [11 13]]

# C = [[ 45  56]
#     [ 99 125]
#     [153 194]
#     [207 263]]

# Los valores son:

    # 1x2+2x5+3x11= 45
    # 1x3+2x7+3x13=56
    # 4x2+5x5+6x11=99
    # 4x3+5x7+6x11=125
    # 7x2+8x5+9x11=153
    # 7x3+8x7+9x13=194
    # 10x2+11x5+12x11=207
    # 10x3+11x7+12x13=263
```

## Propiedades de las matrices

**la multiplicación de matrices es asociativa y distributiva, no es conmutativa**

```py
# Propiedades
# Asociativa: Es si tenemos una matriz 'A' y la multiplicamos por (BxC)
# podemos elegir el orden por el cual realizamos estas operaciones y nos daria el mismo resultado:
# Ejemplo:  Ax(BxC) = (AxB)xC

# Distributivo: Esto es que si tenemos 'Ax(B+C)' es lo mismo que hacer (AxB)+(AxC)

# Conmutativa: Si tenemos una multiplicacion 'BxC' es lo mismo que hacer 'CxB'

import numpy as np

A = np.array([[2,3],[5,7],[11,13]])
B = np.array([[1,3],[2,1]])
C = np.array([[3,1],[4,2]])

# Asociativa
ABC= A.dot(B.dot(C))
ABC

AB_C = A.dot(B).dot(C)
AB_C

# Distributiva
D = A.dot(B+C)
E = (A.dot(B))+(A.dot(C))

print(D)
print(E)

print(D==E)

# Commutativa
# No siempre o casi nunca ocurre la commutativa
F = B.dot(C)
G = C.dot(B)

print(F==G)

print(F)
print(G)

# pero la multiplicacion de vectores si es commutativa
v1 = np.array([[2],[7]])
v2 = np.array([[3],[5]])

v1_tv2 = v1.T.dot(v2)
v2_tv1 = v2.T.dot(v1)

print(v1_tv2)
print(v2_tv1)

# El producto interno de matrices es:

#     Asociativa: Sí
#     Distributiva: Sí
#     Conmutativa: NO
#     El producto interno de vectores es:
#     Asociativa: Sí
#     Distributiva: Sí
#     Conmutativa: Sí
```

## Transposición de un producto de matrices

```py
# En matematicas existe una propiedad que si tengo '(A.dot(B)).T' == 'B.T.dot(A.T)'
# Esto nos permite operar con las matrices como si fueran numeros y juegar con las propiedades como por ejemplo transponer dos veces ya que transponer dos veces es igual a no transponer
# '(A.dot(B)).T.T' == 'B.dot(A)'

import numpy as np

A = np.array([[2,3],[5,7],[11,13]])
B = np.array([[1,3],[2,1]])

print(A)
print(B)

AB_t = A.dot(B).T
B_tA_t = B.T.dot(A.T)

print(AB_t == B_tA_t)
```

## Cómo comprobar la solución de un sistema de ecuaciones lineal

```py
# Que es un sistema de ecuaciones lineales?
# si nosotros tenemos y = 3x + 5     y = 2x+3
# esto es un sistema de ecuaciones lineales, cada una de las variables no esta multiplicada por otra variable y a su vez tampoco esta elevada a una potencia (es de primer grado)

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5,5)

y_1 = 3*x + 5
y_2 = 2*x + 3

plt.figure()
plt.plot(x, y_1)
plt.plot(x, y_2)
# definiremos entre que valos queremos que nos muestre cada eje
plt.xlim(-5,5)
plt.ylim(-5,5)
# con esto agregamos las coordenadas(como queremos verlo)
plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')
# EN la greafica podemos ver en que lugar se estan cruzando nuestro sistema de ecuaciones lineal 
# quiere decir que existe un valor de 'x' y un valor de 'y' que hacen verdaderas a esas ecuaciones al mismo tiempo

# si hacemos el despeje manual:
# y = 3x + 5    
# y = 2x+3
# 2x+3 = 3x + 5
# 3-5 = 3x - 2x
# -2 = x -> el primero de nuestros valores

# y = 2x+3
# y = 2(-2)+3
# y = -1 -> el segundo valor

# esto tambien se puede hacer en un sistema matricial:

#[[-3 1]   [[x]   =   [[5]
# [-2 1]]   [y]]       [3]]

# a esto lo multiplicamos con 
# [[x]
#  [y]]

# el resultado que nos da es:
# -3x + 1y = 5 

# que este es igual al primer problema de la ecuacion lineal
# y = 3x + 5 
# -3x + y = 5


# en codigo se haria de esta manera:
A = np.array([[-3,1],[-2,1]])
print(A)
# [[-3  1]
#  [-2  1]]

b = np.array([[5],[3]])
print(b)
# [[5]
#  [3]]

solucion_1 = np.array([-2,-1])
print(solucion_1) # [-2 -1]

A.dot(solucion_1)
# array([5, 3])
# Efectivamente lo que acavamos de hacer es escribir y resulver nuestros sistemas de ecuaciones y escibir 'Ax=b'

# Realmente la división de vectores o matrices “NO EXISTE”. Debido a que no existe tal cosa como “división de matrices” lo que se hace es obtener la matriz inversa.
# Lo correcto para despejar la matriz (o vector) x seria multiplicar por la izquierda la inversa de A y por tanto nos quedaria como: x = A_inv * b
import numpy as np
A = np.array([[-3,1],[-2,1]])
b = np.array([5,3])
A_inv = np.linalg.inv(A) 
# El valor de x es
x =  A_inv.dot(b)
print(x)

```

## Tipos especiales de matrices: Identidad, Inversa, Singulares

```py
import numpy as np

# matriz de identidad
# la matriz de identidad tiene la particularidad de no hacer ninguna modificacion, es el elemento neutro para el producto interno
# el elemento neutro es como el uno para los numeros, ejemplo: 5 * 1

# numpy tiene una funcion que se llama 'eye' cuando se le da un valor nos devuelve una matriz de esa dimecion con todos 1 en la diagonal y 0 fuera de ellas
# estos valores estan todos definidos como floats
# esto quiere decir que aun que nostros le estemos entregando o estemos operando con esta misma matriz con un vector que tenga nada mas que enteros lo que vamos a recibir en respuesta es un float
identidad = np.eye(4)
print(identidad)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

vector = np.array([[2],[3],[5],[7]])
print(identidad.dot(vector))
# [[2.]
#  [3.]
#  [5.]
#  [7.]]
# como podemos ver los devuelve exactamente el mismo vector que habiamos cargado
# la matriz de identidad tiene la particularidad de no hacer ninguna modificacion, es el elemento neutro dentro de las matrices 

# lo siguiente que podemos hacer es pensar a la matriz como una transformacion lineal 
# una transformacion lineal es, tengo un vector que lo trsnformo cuando le aplico una matriz(aplicar una matriz es multiplicar)
# si tenemos la matriz:
# [[2 3]    [[1]   = [[2+3]
#  [4 5]]    [1]]     [   ]]

# del vector [[1],[1]] la primer coordenada se transformo en 5
# la 'identidad' no transforma ese espacio

# Matriz inversa
# si estamos multiplicando '5x3 = 15' la inversa seria dividir '15/3' y este nos daria un igual a '5'
# Existe una matriz 'A' a la cual multiplicada por algo nos de la identidad 'Id'?
# En algunos casos existe
# Creamos una matriz a la cual queremos calcular la inversa
A = np.array([[1,0,1],[0,1,1],[-1,1,1]])
print(A)
# [[ 1  0  1]
#  [ 0  1  1]
#  [-1  1  1]]

inversa_A = np.linalg.inv(A)
print(inversa_A)
# [[ 0.  1. -1.]
#  [-1.  2. -1.]
#  [ 1. -1.  1.]]
# nos devuelve otra matriz de las mismas dimenciones 
# la formula era 'A * A**-1 = Id'

print(A.dot(inversa_A))
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
# lo que nos devuelve es la 'identidad'

# se habia dicho que no siempre existe esta 'identidad'
# cuando no existe la identidad la llamamos una matriz 'singular'
# cuando no existe la inversa la llamamos una matriz 'singular'
singular = np.array([[1,1],[1,1]])
print(singular)
# [[1 1]
#  [1 1]]

# si intentamos hacer la inversa de la matriz singular nos debolvera un error
print(np.linalg.inv(singular))
# por el momento sabemos calcular inversas de aquellas matrices que son cuadradas
# no podemos intentar esto con una matriz que no fuera cuadrada
# La inversa nos sirve para operar directamente sobre nuestra forma matricial y con eso tendriamos el resultado que estamos buscando para resolver un sistema de ecuaciones lineales

# Matriz identidad = Como el 1 en matematicas, el elemento neutro
# Matriz Inversa = Cumple lo siguiente: A*A^-1 = Id
# Matriz Singular = No se le puede calcular la inversa
```

## Sistema de ecuaciones lineales

### Ejemplos de sistemas sin solución, con una solución y con infinitas soluciones

```py
%matplotlib notebook

import numpy as np
import matplotlib.pyplot as plt

# sistema de ecuaciones sin soluciones
# cuando tenemos mas ecuaciones que variables es 'sobre determinado'
# 'y = 3x + 5'
# 'y = -1x + 3'
# 'y = 2x + 1'

x = np.arange(-6,6)

y_1 =  3*x + 5
y_2 = -1*x + 3
y_3 = 2*x + 1

plt.figure()
plt.plot(x, y_1)
plt.plot(x, y_2)
plt.plot(x, y_3)

plt.xlim(-8,8)
plt.ylim(-8,8)

plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')
plt.show()
# este va a ser un grafico distinto a los que se habia visto anteriormente
# en este hay un boton el cual mientras este activo nos permite interactuar con el grafico
# lo que podemos concluir de las tres lineas que estan representando nuestras ecuaciones es que:
# Es que no existe un punto en el que hacia ciertas estas ecuaciones al mismo tiempo 
# Solamente s ellegan a unir dos ecuaciones y no las 3
# por lo tanto este es un sistema 'sobredeterminado'
# 'sobredeterminado' es que tenemos mas ecuaciones que variables entonces no tiene solucion



# sistemas de ecuaciones con solucion 
# cuando solamente nos quedamos con dos ecuaciones entonces esta 'determinado'
x = np.arange(-6,6)

y_2 = -1*x + 3
y_3 = 2*x + 1

plt.figure()
plt.plot(x, y_2)
plt.plot(x, y_3)

plt.xlim(-8,8)
plt.ylim(-8,8)

plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')
plt.show()
# En este caso las ecuaciones logran cruzarse en un punto
# por lo tanto esta tiene solucion y es unica



# sistema de ecuaciones donde tiene infinitas soluciones
# cuando se dara el caso de que existen infinitas soluciones?
# cuando nos quedamos unicamente con una de las variables
# cuando solamente nos quedamos con una ecuaciones que tiene dos variables entonces esta 'indeterminado' y tiene infinitas soluaciones
x = np.arange(-6,6)
# si tenemos una sola ecuacion con dos varaibles entonces nuestro sistema tiene una grado de libertad, 
# cualquier valor que tome 'x' va a ser solucion 
y_3 = 2*x + 1

plt.figure()
plt.plot(x, y_3)

plt.xlim(-8,8)
plt.ylim(-8,8)

plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')
plt.show()
# cuando graficamos nos queda nadamas que una recta, 
# entonces cualquier punto de la recta resulta ser la solucion del sistema
```

### Graficar vectores

```py
%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([2,5])
v2 = np.array([3,2])

# 'alpha' indica el valor de transparencia que va a tener al momento de graficar 
def graficarVectores(vecs, cols, alpha = 1):
    
    plt.figure()
    plt.axvline(x=0, color = 'grey', zorder = 0)
    plt.axhline(y=0, color = 'grey', zorder = 0)
    
    for i in range(len(vecs)):
        # cuando queremos graficar un vector lo estamos haciando dentro de nuestro sistema de ejes cartesianos
        # para poder graficar un vector necesitamos decir cuales es el origen 
        # y lo que estamos haciendo es decir que todos los vectores van a tener como origen el [0,0]
        x = np.concatenate([[0,0], vecs[i]])
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   angles='xy', scale_units = 'xy', scale=1, color =cols[i],
                   alpha= alpha)

graficarVectores([v1,v2],['orange', 'blue'])
# agregaremos cuales son los limites para los 'x' y 'y'
plt.xlim(-1,8)
plt.ylim(-1,8)
```

### ¿Qué es una combinación líneal?

```py
# Una conbinacion lineal es multiplicar a un vector por un escalar, a otros vector por otro escalar ysumar el resultado de ambos para obtener un nuevo vector.
# (v1*2)+(v2*3) = V1V2

%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

%run './funciones_auxiliares/graficarVectores.ipynb'

v1 = np.array([2,5])
v2 = np.array([3,2])

v1v2 = 2*v1+1*v2

print(v1v2)

graficarVectores([v1,v2,v1v2], ['orange', 'blue', 'red'])
plt.xlim(-1,8)
plt.ylim(-1,12)

# definamos una funcion para graficar todas las posibles combinaciones lineales
# o almenos un subconjunto de ellas, que nos permitira tener una mejor nocion de la importancia de las combianciones lineales
for a in range(-10,10):
    for b in range(-10,10):
        plt.scatter(v1[0]*a + v2[0]*b, v1[1]*a+v2[1]*b,
                   marker = '.',
                   color = 'orange')
        
plt.xlim(-100,100)
plt.ylim(-100,100)

plt.axvline(x=0, color = 'grey')
plt.axhline(y=0, color = 'grey')

plt.show()
# aqui lo que estamos viendo son unas posibles combinaciones lineales de dos vectores
# por lo que estamos viendo si continuaramos ampliando el rango en los cuales se mueven los escalares 'a' y 'b' podriamos describir todo el espacio
# con los vectores correctos nos permiten descrirbir un espacio entero.
```

### ¿Qué es un espacio y un subespacio?

```py
# veremos que ocurre dependiendo de los vectores con los que trabajemos
%matplotlib notebook

import numpy as np
import matplotlib.pyplot as plt

v1 =  np.array([1,1])
v2 = np.array([-1,-1])

for a in range(-10,10):
    for b in range(-10,10):
        plt.scatter(v1[0]*a + v2[0]*b, v1[1]*a+v2[1]*b,
                   marker = '.',
                   color = 'orange')
        
plt.xlim(-25,25)
plt.ylim(-25,25)

plt.axvline(x=0, color = 'grey')
plt.axhline(y=0, color = 'grey')

plt.show()
# lo que nos ocurrio es que vimos dos vectores que son [1,1] y [-1,-1]
#y cuando hicimos las convinaciones lineales lo unico que obtuvimos es una recta 
# esto en si mismo es un espacio
# si nos abstaemos de que estamos en 'r2' y solamente hubieramos entregado para graficar a 'x' hubieramos obtenido lo mismo
# En lugar de esos nosotros lo que dimos son elementos en 'R2' y lo que conseguimos es un 'subespacio' que es 'R1'
# ser un espacio o un subespacio depende de donde nos estemos parando y como lo estemos viendo 

# que ocurre cuando damos otros elementos?
v1 = np.array([1,0])
v2 = np.array([2,-3])

for a in range(-10,10):
    for b in range(-10,10):
        plt.scatter(v1[0]*a + v2[0]*b, v1[1]*a+v2[1]*b,
                   marker = '.',
                   color = 'orange')
        
plt.xlim(-100,100)
plt.ylim(-100,100)

plt.axvline(x=0, color = 'grey')
plt.axhline(y=0, color = 'grey')

plt.show()
# esta vez nos esta dando 'R2'
# es posible entonces con estos dos vectores generar todo el espacio
# la convinacion lineal de dos elemetos solo nos podran devolver un elemento del mismo lugar donde ellos estan viviendo 
# En algebra lineal nosotros siempre estamos trabajando en espacios vectoriales
# los 'espacios vectoriales' no son mas que numeros 'R', 'R1', 'R2', 'R3', no es mas que los numeros que usamos habitualmente escritos como vectores 

# ahora veamos como 'R2' que recien vimos que era un espacio
# en realidad era un subespacio de 'R3'
# esta libreria nos va a permitir visualizar lo que estamos queriendo relaizar
from mpl_toolkits.mplot3d import Axes3D
# vamos a crear un vector en 'R3' pero que solamente cuenta con valores en 'R1' y 'R2'
v1 = np.array([1,0,0])
v2 = np.array([2,-3,0])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for a in range(-10,10):
    for b in range(-10,10):
        ax.scatter(v1[0]*a + v2[0]*b, v1[1]*a+v2[1]*b, 
                   v1[2]*a + v2[2]*b,
                   marker = '.',
                   color = 'orange')
        
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

plt.axvline(x=0, color = 'grey')
plt.axhline(y=0, color = 'grey')

plt.show()
# aqui vemos que engregamos 2 vectores pero solo fuimos capaces de generar un elemento en 'R2' por mas que nuestros vectores estan viviendo en 'R3'
# En algebra lineal se llama hiperplano a una dimencion menos del espacio en el cual estamos trabajando 
# si estamos trabajando en'R3' un hiperplano es 'R2'
```

### Vectores linealmente independientes

Un conjunto de vectores se dice [**linealmente independiente**](https://www.superprof.es/apuntes/escolar/matematicas/analitica/vectores/vectores-linealmente-dependientes-e-independientes.html "linealmente independiente") si ninguno de ellos puede ser escrito con una combinación lineal de los restantes. 

```py
# cuando tenemos una matriz 'ax = b' en este caso podemos pensar que tenemos:
# un vector 'v1' y un vector 'v2' que se multiplica por 'x'
# y lo que nos preguntamos es, Sera posible escribir a nuestra solucion 'b' como una convinacion lineal de 'v1 y 'v2'
# si eso fuera posible obtendriamos los valores de 'x1' y 'x2' que hicieran verdadero este sistema de ecuaciones lineal
# con esto vemos a nuestra matriz 'a' como un sistema generador 
# donde puede estar generadondo un espacio o un subespacio , dependera de los vectores que componen a 'a'

%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

v1 = np.array([1,1])
v2 = np.array([-1,-1])

for a in range(-10,10):
    for b in range(-10,10):
        plt.scatter(v1[0]*a+v2[0]*b,
                   v1[1]*a+v2[1]*b,
                   marker = '.',
                   color='orange')
        
plt.xlim(-25,25)
plt.ylim(-25,25)

plt.axvline(x=0, color='grey')
plt.axhline(y=0, color='grey')

plt.show()
# lo que estamos teniendo es una matriz con los valores [[1,1],[-1,-1]] que nos esta generando solamente una dimecion dentro de 'R2'
# Si proponemos como solucion de este sistema los valores de [[-10,10]]
# sera que existe un 'x1' y un 'x2' que hacen esto verdadero?


# En realiad no es posible por que el vector que estamos intenando escribir '[[-10,10]]' vive completamente afuera del subespacio generado por los dos vectores [[v1],[v2]]
# podemos ver entonces que el sistema de ecuaciones lineal no tendra solucion
# esto ocurre por que enrealidad 'v1' es linealmente dependiente con respecto a 'v2', no son linealmente infependientes 
print(v1 == -1 * v2)
# lo que ocurre al hacer esto que nos quedamos con una dimecion menos
# mas alla de que nuestra matriz en principio parece cuadrada(es cuadrada), pero no todos us vectores son linealmente independientes
# Se concluye que un conjunto de vectores es 'linealmente indendiente' si ninguno de ellos se puede escribir como combinacion lineal de los otros vectores
# visto de otra manera esto es:
# si vemos el espacio generado por 'v1' y 'v2' es el mismo espacio que genera solamente usar 'v1' o solamente usando 'v2'
# esto quiere decir que usar los dos vectores al mismo tiempo no nos aporta informacion, no nos aporta una nueva dimencion
```

### Validar que una matriz tenga inversa

```py
# para que un sistema de ecuaciones lineales tenga solucion necesitamos que la matriz 'a' que representa este sistema de ecuaciones sea cuadrada y que todos sus vectores sean linealmente idependientes
# osea que no contenga ningun vector 'ld'
import numpy as np

A = np.array([
[0,1,0,0],
[0,0,1,0],
[0,1,1,0],
[1,0,0,1]]
)
# a primera vista esta matriz es cuadrada pero vamos a ver que no es ese el caso
# Es cuadrada pero no todos sus vectores son linealmente idependientes 
# cuando quitemos el vector que es lineal mente dependiente para que nos queden todos linealmente idependientes, la matriz dejara de ser cuadrada

# Una forma de identificar cual fila es la que es linalmente dependiente 
# es usando los autovectores y autovalores
# los autovectores y autovalores es una forma de descomponer nuestra matriz
# asi como cuando tenemos un numero , por ejemplo:
# 8 = 4 * 2
# aqui lo que estamos haciendo es decomponer al 8 como la multiplicacion de dos elementos
# tambien podemos elegir descomponer al 8 como la suma de dos elementos
# 8 = 5 + 3
# En este caso al descomponer nuestra matriz 
# la estamos descomponiendo como la multiplicacion de otras dos matrices que enverdad seran 3


# 'linealg.eig' es la manera de buscar los autovalores y autovectores 
lambdas, V = np.linalg.eig(A.T)

# esto lo que nos va a estar devolviendo es la fila que es li
print(A[lambdas == 0, :])
#print: [[0 1 1 0]]
# aqui lo que podemos ver es que la tercera fila, la '[[0 1 1 0]]' es linealmente dependiente
# lo que esta ocurriendo es que el [[0 1 1 0]] lo podriamos escribir como la suma del vector una que es el [[0 1 0 0]] y el vector 2 que es el [[0 0 1 0]], si los sumaramos obtenemos [[0 1 1 0]]
# decir que el vector 3 es el que es lineal mente dependiente es una convencion, tambien podemos decir que en realidad es el vector dos al cual lo podemos escribir como una convinacion lineal del vector 1 y el vector 3
# si tenemos 3 vesctores y una de ellos puede ser escrito en funcion de los otros dos podemos elegir a cual vamos a escribir en funcion de los otros
# entonces podemos ver que si intentamos calcular la inversa de esta matriz nos va  adar que es singular 
# sigular es una matriz que no tiene inversa
# pero tambien se le puede caracterisar por que tiene un vector ld dentro de sus filas
#np.linalg.inv(A)



# se concluye que para que un sistema de ecuaciones lineales tenga solucion
# la matriz 'A' que los reprecenta no debe tener vectores 'linealmente dependientes'
# osea no tiene que haber ni filas ni columnas que puedan ser escritas como combinacion de las demas filas o columnas 

# También quiero mencionarles que existe una versión de inversa cuando la matriz “no es cuadrada”. se llama la “inversa generalizada” o “inversa de Penrose-Moore”. 


# matematicamente pasa lo siguiente:
#para calcular la matriz inversa se calcula primero la transpuesta de la matriz adjunta y esta se divide por el determinante de la matriz.

#Cuando en una matriz tenemos vectores LD tantos en columnas como en filas el determinante es 0, SIEMPRE haciendo que la division no se pueda resolver

```

## Normas

### Qué es una norma y para qué se usa. Desigualdad Triangular

**Norma** es una funcion que ayuda a medir el tama;o de una vector. La norma lo que hace es recibir de entrada un vector y a ese vector asociarle un numero, un numero que no puede ser negativo.

**Para que quisieramos saber cual es tam;o de un vector?**
Nos ayuda a identificar el error que estamos comentiendo al hacer nuestras aproximaciones o las clasificaciones.

```py
# primera propiedad
# La norma de un vector 'v' tiene que ser igual o mayor a 0
# norma(v) >= 0
# si pensamos que la norma mas habitual que conocemos es la que mide la distancia de un punto al origen 
# y tal como es una distancia nunca puede ser negativa

# segunda propiedad
# 'norma(v) == 0' si y solo si 'v = 0' 

# la tercera propiedad es lo que se conoce como la desigualdad triangular 
# y esto quiere decir que si tenemos 2 vectores y realizamos la suma de ambos y calculamos entonces sus nomas, entonces la norma de el vector recultante 'v3' es menor o igual que la suma de las normas 
# 'norma(v3) <= norma(v1) + norma(v2)'

# cuarta propiedad
# la norma del un escalar por un vector es igual al valor absoluto por la norma del vector original
# 'norma(a*v)=abs(a)*norma(v)'

%matplotlib inline

import numpy as np

import matplotlib.pyplot as plt
# sacaremos la paleta de colores de 'seaborn'
import seaborn as sns 


v1 = np.array([2,7])
v2 = np.array([3,5])

v1v2 = v1+v2


# para calcular las norma usamos la funcion de numpy 'linalg.norm'
# 'linalg.norm' utiliza varios parametros, en esta ocacions usaremos el paremetro por default(la norma 2)
np.linalg.norm(v1v2)

# la desigualdad triangular nos dice que:
# nos indica que la norma de 'v1v2' tiene que ser menor que la norma v1 mas la norma v2
# norma(v1v2) <= norma(v1) + norma(v2)

norma_v1 = np.linalg.norm(v1)
norma_v2 = np.linalg.norm(v2)
norma_v1v2 = np.linalg.norm(v1v2)

print(norma_v1v2 <= (norma_v1 + norma_v2))
# print: True
# efectivamente vemos que esta cumpliendo la desigualdad triangular 
# el unico caso en el cual la desigualdad triangular adquiere la igualdad es:
# cuando los 3 vectores estan uno sobre el otro, este es el unico caso.

# agregaremos esta vez dos corrdenadas 0 al principio , con esto estamos incluyendo el origen del vector y el finald el vector 
v1 = np.array([0,0,2,7])
v2 = np.array([0,0,3,5])

v1_aux = np.array([v1[2], v1[3], v2[2], v2[3]])
v1v2 = np.array([0,0,5,12])

plt.quiver([v1[0], v1_aux[0], v1v2[0]],
           [v1[1], v1_aux[1], v1v2[1]],
           [v1[2], v1_aux[2], v1v2[2]],
           [v1[3], v1_aux[3], v1v2[3]],
           angles = 'xy', scale_units = 'xy',
           scale = 1, color = sns.color_palette()
           )

plt.xlim(-0.5, 6)
plt.ylim(-0.5,15)
```

### Tipos de normas: norma 0, norma 1, norma 2, norma infinito y norma L2 al cuadrado 

```py
# hay muchos tipos de normas que se usan en aprendizaje automatico (machine learning), para medir diversas cosas, algunas de ellas son los errores.
# a las normas las vamos a estas llamando con la aletra 'L'
# 'L0' nos devuelve la cantidad de elementos de nuestro vector distintos de 0
# 'L0: #vi != 0'

# 'L1' nos va a devolver la suma sobre 'i' de los valores absoluto de los elementos de nuestro vector 
# 'L1: sum(i).abs(vi)'

# 'L2' es la magnitud del vector desde su origen.(distancia euclidiana)
# se usa mucho en lenguaje automatico la '(L2)**2' esto es la misma distancia auclidiana pero si calcularle la raiz cuadrada 
# la ventaja es que podriamos calcularle la norma a aun vector directamente aplicando el producto interno del vector contra si mismo, esto tiene muchas ventajas computacionales
# por ejemplo: podemos representar todo con una matriz, calcular el producto interno y tener la norma al mismo tiempo de muchisimos vectores (todos los que estuvierand entro de esa matriz)

# 'L_infinito' lo que nos devuelve es el mayor valor dentro de los valores absolutos de nuestro vector
# 'L_infinito: max(i).abs(vi)' 

import numpy as np

vector = np.array([1,2,0,5,6,0])
# al momento de pedirle la norma 'L0' nos va a devolver la cantidad de elementos distintos de 0
# En este caso cuando lo hagamos nos tendria que devolver 4 por que tenemos 2 valores 0 de los 6 totales
# 'ord' es el numero de la norma que deseams calcular
print(np.linalg.norm(vector, ord=0))
# print: 4.0

vector = np.array([1,-1,1,-1,1])
# la norma 'L1' nos devuelve la suma de los valores absolutos 
# entonces lo que esperamos que nos devuelva es la longitud del vector
print(np.linalg.norm(vector, ord=1))
# print: 5.0

vector = np.array([1,1])
# vamos a ahcer un representacion grafica
# esto tiene sentido hacerlo cuando estamos en 'R2' o 'R3' donde nuestra mente es capaz de ver una representacion grafica de estos vectores
# lo importante de las normas es que las podemos utilizar independientemente del tama;oque estamos teniendo(del espacio en el cual estamos trabajando), aun cuando nosotros no logremos interpretar cual seria su representacion fisica 
# probaremos ejecutar la norma sin el parametro 'ord' y con el parametro 'ord'
print(np.linalg.norm(vector, ord=2))
print(np.linalg.norm(vector))
# print:
# 1.4142135623730951
# 1.4142135623730951
# nos regerso el mismo numero ya que la funcion norma nos devulve por defecto la norma 2

# ahora probaremos la norma 'L2' elevada al cuadrado
vector = np.array([1,2,3,4,5,6])
print(np.linalg.norm(vector, ord=2)**2)
# print: 91.0
#seria que es igual a que si hacemso el rpoducto interno?
print(vector.T.dot(vector))
# print: 91
# como se hia dicho esto tiene una serie de ventajas computacionales y es por eso que la noma 'L2' es la norma mas usada

vector = np.array([1,2,3,-100])
# como la norma 'L3' nos tiene que devolver el valor absoluto mas grande nos tendria que devolver 100 en esta ocacion
# para especificar la norma infinito tenemos que usar 'np.inf' el cual es el infinito de numpy
print(np.linalg.norm(vector, ord=np.inf))
# print: 100.0
```

### El producto interno como función de una norma y su visualización

```py
# SI tenemos un vector 'v1'  y un vector 'v2, lo que queremos decir es que:
# 'v1' traspuesto, producto interno 'v2' va a sef igual a la norma 2 de 'v1' por la norma 2 de 'v2' por el angulo, por el coseno del angulo que estan formado
# 'v1.t.dot(v2) = norma_2(v1)*norma_2(v2)cos(algulo)'

%matplotlib inline

import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

v1 = np.array([0,0,0,3])
v2 = np.array([0,0,3,3])

plt.xlim(-2,6)
plt.ylim(-2,6)

plt.quiver([v1[0], v2[0]],
          [v1[1], v2[1]],
          [v1[2], v2[2]],
          [v1[3], v2[3]],
          angles = 'xy', scale_units= 'xy',
          scale = 1, color= sns.color_palette()
          )
plt.show()

# para comprobar la igualdad
v1 =  np.array([0,3])
v2 = np.array([3,3])
# cuando tenemos esto podemos ver cual es eproducto interno que estamos tendiendo entre las traspuesta de 'v1' con 'v2'

print(v1.T.dot(v2))
#print: 9

norma_v1 =  np.linalg.norm(v1)
norma_v2 =  np.linalg.norm(v2)

# pasa usar coseno numpy nos da al funcion 'np.cos', ahora esta funcion necesita que le pasemos los valores en radianes y nosotros los tenemos en grados
# entonces vamos a usar la funcion 'np.np.deg2rad'
# en esta ocasio el calor de 45 son los grados que forman los vectores
print(norma_v1 * norma_v2 * np.cos(np.deg2rad(45)))
# print: 9.0
# entonces la igualdad de esta se verifica

# lo que acavamos de hacer nos da tambien una manera de poder calcular el angulo que forma nuestros vectores si conocemos el producto interno y a su vez tenemos cual es la norma de cada uno de ellos.
# una de las cosas que se usan en 'machine learning' es la similitud coseno
# si nosotros somos capaces de representar en un vector todas las palabras de un documento y en otro vector todas las palabras de otro documento
# podriamos evaluar cual es el angulo que estos dos vectores estan formando y si ese angulo fuese peque;o esto quiere decir que esos dos documentos se parecen mucho 
# por el contrario, si difirieran en 90 grados dirian que no tienen nada que ver un documento con el otro

# se concluye que el producto interno lo podemos expresar con normas y con el angulo que forman nuestros vectores 
```

## Matrices y vectores especiales

## La matriz diagonal y la matriz simétrica: sus propiedades 

```py
# La 'amatriz de identidad' es elemento neutro del producto interno
# otra matriz especial es la 'matriz inversa' :
# si tenemos una matriz 'A' y la multiplicamos por su inversa 'A**-1' lo que obtenemos es la 'Matriz de Identidad': 'A.dot(A_inv)= Id'
# La 'matriz singular' es aquella tal que no existe su inversa.

# ahora veamos las 'matrices diagonales' y 'matriz simetrica'
# MATRIZ DIAGONAL
import numpy as np

vector = np.array([1,2,3,4,5])

matriz = np.diag(vector)
print(matriz)
# [[1 0 0 0 0]
#  [0 2 0 0 0]
#  [0 0 3 0 0]
#  [0 0 0 4 0]
#  [0 0 0 0 5]]

print(matriz[0:4,0:3])
# este es un ejemplo de amtriz diagonal pero que no es cuadrada
# [[1 0 0]
#  [0 2 0]
#  [0 0 3]
#  [0 0 0]]

print(matriz[0:3,0:4])
# este seria otro ejemplo de una matriz diagonal pero que no es cuadrada
# [[1 0 0 0]
#  [0 2 0 0]
#  [0 0 3 0]]

A = np.diag([2,3,4,5])
print(A)
# [[2 0 0 0]
#  [0 3 0 0]
#  [0 0 4 0]
#  [0 0 0 5]]

v1 = np.array([[1,1,1,1]])

print(v1) # [[1 1 1 1]]
# Esto es una 'ponderacion de los elementos por el vector por el cual estamos multiplicando'
print(A.dot(v1.T))
# Nos devolvio el vector columna:
# [[2]
#  [3]
#  [4]
#  [5]]
# no hubo ninguna tipo de combinacion lineal y solamente nos quedaron amplificados las componentes de cada uno de nuestros vectores 

# calcular la inversa
# si tenemos una matriz 'A' y la multiplicamos por su inversa 'A**-1' lo que obtenemos es la 'Matriz de Identidad': 'A.dot(A_inv)= Id'

# en est ocacion iniciaremos por un medio por que el primer elemento era un 2
A_inv = np.diag([1/2, 1/3, 1/4, 1/5])
print(A_inv)
# [[0.5        0.         0.         0.        ]
#  [0.         0.33333333 0.         0.        ]
#  [0.         0.         0.25       0.        ]
#  [0.         0.         0.         0.2       ]]

identidad = A.dot(A_inv)

print(identidad)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]
# esto computacionalmente tiene muchos beneficios por que si la inversa es solamente calcular 1 sobre el numero que esta en la diagonal, entonces no son muchas las operaciones que debo realizar

# ahora vamos a intentar calcular la inversa con la funcion que usamos antes
A_inv_calc = np.linalg.inv(A)
# si la imprimimos obtenemos lo mismo
print(A_inv_calc)
# [[0.5        0.         0.         0.        ]
#  [0.         0.33333333 0.         0.        ]
#  [0.         0.         0.25       0.        ]
#  [0.         0.         0.         0.2       ]]


# cuando una matriz es simetrica?
# una matriz es 'simetrica' cuando su traspuesta es igual a la matriz: 'A = A.T'
# En este caso nuestra matriz 'A' es simetrica.
print(A.T) 
# [[2 0 0 0]
#  [0 3 0 0]
#  [0 0 4 0]
#  [0 0 0 5]]
print(A)
# [[2 0 0 0]
#  [0 3 0 0]
#  [0 0 4 0]
#  [0 0 0 5]]

# para matrices en general es un poco mas complicado
simetrica = np.array([[1,2,3],
                     [2,-1,7],
                     [3,7,11]])
print(simetrica)
print(simetrica.T)
# en este caso nos arroja de vuelta la misma matriz
# No es unicamente las amtrices diagonales las que pueden ser simetricas 

# una propiedad que se vio antes es que si:
#'(A.dot(B)).T == B.T.dot(A.T)'
# cuando son simetricas lo que queda quedando es que:
# '(A.dot(B)).T == B.dot(A)
# esto tambien tiene implicaciones muy importantes por que simplifica mucho las operaciones que estamos realizando.
```

## Vectores ortogonales, matrices ortogonales y sus propiedades

```py
# Existe en solitario un vector ortogonal?
# la respuesta es no, para poder ser ortogonal hacen referencia a otro vector, entonces siempre que hablemos de vectores ortogonales vamos a estar hablando de 2 o mas vextores.
# Ser 'ortogonal' es que el angulo que forman estos dos vectores es de 90 grados.
# usaremos el producto interno por que nos permite conocer el angulo entre los vectores.

%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

x = np.array([0,0,2,2])
y = np.array([0,0,2,-2])

plt.quiver([x[0],y[0]],
           [x[1],y[1]],
           [x[2],y[2]],
           [x[3],y[3]],
           angles = 'xy', scale_units = 'xy',
           scale= 1)
plt.xlim(-2,4)
plt.ylim(-3,3)

plt.show()
# lo que vemos es que tenemos dos vectores que forman un angulo de 90 grados 

# vamos a comprobar esto mismo usando el producto interno
v1 = np.array([2,2])
v2 = np.array([2,-2])

print(v1)
print(v2)

print(v1.dot(v2.T)) # 0
# los que nos devuelve es el cero, entonces estos dos vectores efectivamente tienen un aungulo de 90 grados
# y podemos decir que son ortogonales entre ellos


# ORTONORMAL
# Para que un vector sea 'ortonormal' su normal debe ser 1.
print(np.linalg.norm(v1)) # 2.8284271247461903
print(np.linalg.norm(v2)) # 2.8284271247461903
# con los resultados obtenidos podemos ver que estos dos vectores no son ortonormales

# lo que podriamos hacer para volverlos ortonomales es dividirlos con su norma
vector_ortonormal = v1 * (1/np.linalg.norm(v1))
print(np.linalg.norm(vector_ortonormal)) # 0.9999999999999999
# probemos con otros vectores
v1 = np.array([[1,0]])
v2 = np.array([[0,-1]])
# si calculamos su producto interno podemos ver que nos da 0
print(v1.dot(v2.T)) # 0
# y si calculamos la norma podemos ver qu es 1
print(np.linalg.norm(v1)) # 1
print(np.linalg.norm(v2)) # 1
# por lo tanto son vectores ortonormales

# sin entrar en demacioados detalles
# podemos decir que es inposible tener 'n' vectores mutuamente ortogonales en un espacio de dimencion 'n' osea 'rn', 
#llevado a 'r2' por ejemplo: no podemos tener mas de dos vectores que sean mutuamente ortogonales 
# seria posible incluir un tercer vector que tambien estuviera a 90 grados de los dos vectores anteriores?
# la respuesta es que no es posible 
# para poder tenerlo necesitariamos ir a 'r3' incluyendo una nueva dimencion que nos permitiria tener un tercer vector mutuamente ortogonal a los anteriores
```