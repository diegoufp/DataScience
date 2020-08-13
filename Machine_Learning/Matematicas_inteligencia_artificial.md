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
