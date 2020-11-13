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