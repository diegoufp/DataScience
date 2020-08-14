# Fundamentos Matemáticos para Inteligencia Artificial

## Matematica Basica

El **Machine Learning** implica muchisimos calculos y muchas operaciones que deben hacerse de manera economica, es decir que no suponga mucho coste computacional o de memoria para la maquina. Para esto necesitamos una herramienta que comienza con los **vectores**, continua con las **matrices** y concluye con **algebra lineal**. Esa herramienta economizara mucho nuestras operaciones de modo que no le tome mucho tiempo.

### Vectores

Los vectores son segmentos orientados en el plano. Se caracterizan por sus coordenadas.

Los vectores pueden operarse, es decir que se pueden hacer sumas, restas, producto escalar y producto vectoral.

**Combinacion lineal**: Multiplicar entre si dos series de numeros y se suman.


Ejemplo: 
ō(1,1,2)
ū(0,2,1)

- **Producto escalar**
Esto es una combinacion lineal
ō * ū = 1*0 + 1*2 + 2*1 = 4 ∈ R (Numero real)

- **Producto vectorial**
(con el circunflejo indican las coordenadas "∧")
(se multiplican en diagonal)
Se tiene que elaborar una construccion:
```
o ∧ u =             | ĥ  î  ĵ   
                    | 1  1  2
0ĵ =  0 * 1 * ĵ =    | 0  2  1  = ĥ * 1 * 1 = 1ĥ  
4ĥ = ĥ * 2 * 2 =    | ĥ  î  ĵ   = 1 * 2 * ĵ = 2ĵ
1î = 1 * î * 1 =    | 1  1  2  = 0 * î * 3 = 0î
------                                      ------
4ĥ + 1î                                     1ĥ + 2ĵ
```
Despues se restan los dos resusltados:
```
1ĥ + 2ĵ - ( 4ĥ + 1î ) = 1ĥ + 2ĵ - 4ĥ - 1î  = -3ĥ - 1î + 2ĵ
```

El resultado `-3ĥ - 1î + 2ĵ` es un vector.

### Matrices

Una **Matriz** es una organizacion bidimencional de numeros. Es decir, nosotros vamos a organizar los numeros en cuadriculas. Pueden ser cuadriculas que tengan un numero determinado de columnas y un numero determinado de filas, si tiene el mismo numero de filas y columnas se llaman **Matrices cuadradas**.

- Ejemplo de matriz cuadrada:
```
[    
     1  0  3 -1
    -4  3  7  1
     2 -2 -5 -8
     0  2  0  9
]
```

- **Matriz de Identidad**
Hay 1 y 0. Los 1 estan en la diagonal principal y los 0 el resto. Esto es equivalente a 1, es decir,  que si multiplicas una **matriz** por su **matriz de identidad** te dara la misma matriz.

Tambien existen **Matrices fila** y **Matrices columna** , en pocas palabras son vectores, eso quiere decir que una matriz es un vector muy grande o un vector es un caso muy particular de una matriz.

```
[
    1 0 0 0
    0 1 0 0
    0 0 1 0
    0 0 0 1
]
```

- **Matriz fila**
```
[   1  4  -2    ]
```

- **Matriz columna**
```
[
     0
     3
    -6
]
```

#### Multiplicar dos matrices

```
[    
     1  0  3
    -4  3  7
     2 -2 -5   
                ] 
```
por
```
[
    2  1  0
    3  1 -2
    0 -1 -2
                ]
```

- Primera ecuacion:

La primera fila se va a multiplicar con la primera columna
La ecuacion seria:
(1*2) + (0*3) * (3*0) = 2 + 0 + 0 = 2
```
[ 
    2


]
```

- Segunda ecuacion
La primera fila y la segunda columna
La ecuacion seria:
(1*1) + (0*1) + (3*-1) = 1 + 0 + -3 = -2
```
[
    2 -2


]
```

- Tercera ecuacion
La primera fila y tercera columna
La ecuacion seria:
(1*0) + (0*-2) + (3*-2) = 0 + 0 + -6 = -6
```
[
    2 -2 -6


]
```

- Cuarta ecuacion
La segunda fila y primera columna
La ecuacion seria:
(-4*2) + (3*3) + (7*0) = -8 + 9 + 0 = 1
```
[
    2 -2 -6
    1

]
```

Y asi sucesivamente hasta completarlo, el resultado seria:
```
[
     2 -2  -6
     1 -8 -20
    -2 -5  14
                ]
```

### Algebra lineal

El algebra lineal era una herramienta muy economica para resolver sistemas complejos, es decir, que a la maquina no le cueste tanto trabajo esos calculos que le costara realizar.

- Fundamentos:
**sistema matricial** el producto de 2 matrices

En este caso ejemplo solo conocemos la primera matriz, la segunda amtriz no sabemos cual es.

```
# Primera matriz

[
    1 -3  2
    5  6 -1
    4 -1  3
                ]
```
```
# Segunda matriz (matriz vector)
# Lo que la maquina necesitara averiguar
[
    x
    y
    z
        ]
```

Se van a multiplicar las dos matrices:
```
x -3y + 2z = -3
5x + 6y -z = 13
4x - y + 3z = 8
```
```
[ 
    -3
    13
     8
        ]
```

- Soluciones que podemos esperar de este sistema:
Un sistema de ecuaciones asi puede suceder que sea un **Sistema compatible determinado**, un **Sistema compatible indeterminado** o un **Sistema incompatible**. Esto tiene una interpretacion geometrica.

Si pensamos en las ecuaciones de antes como en rectas o planos, esos planos van a poder coincidir o no.

Si tenemos un **Sistema compatible determinado** los 3 planos coincidiran en un punto, un punto que tiene 3 coordenadas, por lo tanto seria la x , y , z un punto determinado que seria la unica solucion.

Si tenemos un **Sistema compatible indeterminado** esto quiere decir que no es un punto, puede ser una recta o puede ser un plano. Lo que ocurriria es que las soluciones pueden ser infinitas.

Si tenemos un **Sistema incompatible** quiere decir que no tiene una solucion, no existe solucion. Puede ocurrir que dos de las ecuaciones coinciden pero la tercera no.

#### Resolver estos sistemas con python
[Documentacion de numpy](https://numpy.org/doc/stable/reference/generated/numpy.matrix.html "Documentacion de numpy")

```python
#Definimos la matriz y la matriz resultado
matriz = np.array([[1,-3,2],[5,6,-1],[4,-1,3]])
matriz_resultado= np.array([[-3],[13],[8]])
#Calculamos la inversa de la matriz
matriz_inv = np.linalg.inv(matriz)
#Realizamos el produto entre la matriz inversa y la matriz resultado
matriz_solucion= matriz_inv.dot(matriz_resultado)
#pd: no olvidar importar numpy
import numpy as np
```

### Metodo de Gauss

Las matrices
```
[                   [                [
    1 -3  2             x               -3
    5  6 -1             y       =       13
    4 -1  3             z                8
            ]              ]                ]
```
Se simplificaran a:
```
[               |
    1 -3  2     |   -3
    5  6 -1     |   13
    4 -1  3     |    8
                |           ]
```

- Procedimiento de Metodo de Gauss
Primero vamos a triangular nuestra matriz, es decir, que los 3 numero que estan en la parte inferior izquierda los queremos convertir en 0.
```
[               |
    1 -3  2     |   -3
    0  6 -1     |   13
    0  0  3     |    8
                |           ]
```
Pero no simplemento los vamos a remplazar con 0, vamos a hacer operaciones para que se conviertan en 0.
```
[               |
    1 -3  2     |   -3          F1
    5  6 -1     |   13          F2
    4 -1  3     |    8          F3
                |           ]
```
La fila numero 2(F2) y la fila numero 3 (F3) al operar entre ellas. Si yo a la **F2** le resto la **F3** la que va a cambiar va a ser la **F2**(**F2**-**F3**).
```
[               |
    1 -3  2     |   -3          F1
    1  7 -4     |    5          F2
    4 -1  3     |    8          F3
                |           ]
```
Si ahora a la **F2** le restamos la **F1** entonces logramos convertir el primer objetivo a 0 (**F2**-**F1**).
```
[               |
    1 -3  2     |   -3          F1
    0 10 -6     |    8          F2
    4 -1  3     |    8          F3
                |           ]
```
Si ahora a la **F3** le restamos la **F1** multiplicada por 4 consiguiriamos convertir otro objetivo a 0 (**F3**-4***F1**).
```
[               |
    1 -3  2     |   -3          F1
    0 10 -6     |    8          F2
    0 11 -5     |   -4          F3
                |           ]
```
Si ahora a la **F3** le restamos 1/10 de **F2** lograremos convertir el ultimo objetivo a 0 (**F3**-1/10**F2**)
```
[               |
    1 -3  2     |   -3          F1
    0 10 -6     |    8          F2
    0  0 16     |  112          F3
                |           ]
```

Ahora al pasarlo a manera de fraccion podremos saber cuanto valen las incognitas mas facilmente.
```
[                   [                [
    1 -3  2             x               -3
    0 10 -6             y       =        8
    0  0 16             z              112
            ]              ]                ]
```
```
x - 3y + 2z =  -3
   10y - 6z =   8
        16z = 112
```
```
z = 112/16 = 7
```
Y asi ir resolviendo las otras incognitas.
```
y = 50/10 = 5
```
```
x = -2
``` 

### Funciones elementales

Una funcion es una aplicacion, es decir, que a la funcion le entran una serie de datos de entrada y la funcion devuelve una serie de datos de salida. A la entrada la llamamos la **variable independiente** y a la salida la **variable dependiente**.

Toda funcion lleva asociada una grafica y esa grafica es muy importante por que nos dice como se comporta la funcion tambien nos dice si es continua, si se va al infinito, si no se va al infinito.

Una manera muy util de traducir la expresion a una grafica es dar una tabla de valores
```
    x | f(x) = x**2
    1 | 1
    2 | 4
    3 | 9
```
No es el metodo mas optimo, hay metodos mucho mas elegantes que te dan muchas mas informacion sobre la funcion, pero esta bien.

**Tipos de funciones**:
Hay funciones que van muchos mas rapido que otras al infinito. Por ejemplo la funcion lineal tiene una velocidad normal pero sin embargo una funcion como la cuadratica iria mucho mas rapido a infinito(crece con mas velocidad)

- **Funciones Lineales**
La `n` implica el punto donde corta la funcion al eje `y` se llama **ordenada en el origen**. 

```
f(x) = mx + n
```

- **Funcion cubica**
```
f(x) = x**3
```

- **Funcion exponencial**
Es una funcion que siempre crece hacia el infinito
```
f(x) = e**x
```

- **Funcion de raiz de equis**
```
f(x) = (x)**0.5
```

- **Funcion logaritmica**
La funcion logaritmica y la funcion exponencial son inversas la una de la otra.
```
f(x) = log x
```

- **Funciones trigonometricas**
```
f(x) = sen x
f(x) = cos x
```
```
f(x) = tg x
f(x) = cotg x
```
```
f(x) = sec x
f(x) = cosec x
```

- **Funciones hiperbolicas**
```
f(x) = senh x
f(x) = cosh x
f(x) = tgh x
f(X) = ctgh x
f(x) = sech x
f(x) = csech x
```

### Limites

El limite lo unico que hace es evaluar la funcion en un punto dado.

Ejemplo:
Vamos a calcular el limite cuando `x` tiende a 0. Lo unico que tendrias que evaluar seria el 0 donde esta la x.
```
# Seria 0 al cubo que es igual a 0
lim f(x) = 0**3 = 0
x->0
```
El limite de `x` cuando tiende a 1 es igual a 1.
```
lim f(x) = 1**3 = 1
x->1
```

- **Asintota vetrical**
Lo que ocurre en `x=0` es una cosa que se llama asintota vertical, que es cuando la funcion llega hasta un punto y se encuentra una especia de linea invisible de la cual no puede pasar y esta tiende a infinito(en una grafica).

En estos caso lo que tendriamos que hacer es evaluar la cercania de esa asintota vertical.
```
f(x) = 1/x
x=0
```

### Derivadas
Las derivadas son una serie de reglas que se aplican a la funciones.
Una derivada de una funcion es otra funcion.
La primera funcion de la que partimos se llama primitiva y la segunda se llama derivada
```
f(x) ------->  f'(x)
Primitiva ---> Derivada
```

#### Reglas de como una funcion va a derivarse
```
f(x) = K --> f'(x) = 0

f(x) = K * x --> f'(x) = K

f(x) = K * (x)**n --> f'(X) = K * n * (x)**n-1

(d/dx)K * f(x) = K(d/dx)f(x)

(d/dx)f(x)**n = n * f(x)n-1(df/dx)

(d/dx)(f(x) + g(x) + ...) = (df/dx) + (dg/dx) + ...

(d/dx)(f(x) * g(x)) = f(x) * (dg/dx) + g(x) * (df/dx)

(d/dx)(f(x)/g(x)) = (f(x) * (dg/dx) - g(x) * (df/dx)) * +(1/g(x)**2)
```

#### Utiles de las derivadas

- Regla de la cadena
Para los casos en que la funcion es muy poco intuitiva y no sabes como derivarla.
```
(df/dx) = (df/dg) * (dg/dx) 
```

- Derivadas parciales
Si quieres derivar una funcion de varias variables necesitas las derivadas parciales.

En el caso de `f(x,y,z) = (cos x/ (y)**3) + 2(z)**2` se tiene que derivar asi:
```
∂f/∂x = - (sen x) / (y)**3
∂f/∂y = - (3 cos x) / (y)**4
∂f/∂z = 4z
```

### Integrales

La integral de igual forma que la derivada que lleva de `f(x) --> f'(X)`, las integrales es el proceso inverso `f(x) <-- f'(x)`.

```
∫f(x)dx
```
Cuando derivas una funcion estas perdiendo informacion, por eso se tienen los **limites de integracion** para compensar de alguna manera esa perdida de constantes a esto se le llama **integral definida**. Si no se define ese intervalo, si solamente te limitas a la integracion de la funcion al final estas obligado a poner `+C`, es decir, mas una constante que no sabes cual es.
```
f(x) + C
```

Por eso son tan complicadas por que esta casi en el terreno de la especulacion.

- Limites de integracion 
Se esta integrando entre pos puntos del dominio de tu funcion.

### Teoremas

- Teorema de Bolzano

Si una función `f(x)` es continua en un intervalo [a,b], cuyos valores extremos `f(a)` y `f(b)` tienen distinto signo, la función cortará al eje (y por tanto devolverá el valor 0) en algún punto del intervalo.

- Teorema de los Valores Intermedios

En el mismo caso y condiciones explicitadas en el teorema de Bolzano, la función alcanzará cualquier valor intermedio comprendido entre `f(a)` y f(b)]. Como puedes ver, no es más que una generalización del teorema de Bolzano.
