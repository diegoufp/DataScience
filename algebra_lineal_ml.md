# Algebra Lineal Aplicada a Machine Learning

## Transformaciones lineales y descomposición de matrices

### Podemos y debemos pensar a las matrices como transformaciones lineales

```py
# a las matrices las podemos pensar como transformaciones lineales
# que cuando las aplicamos a un espacio o a un vector generan una transformacion
# la transformacion en el caso de un vector podria ser que lo estiran o lo achican o incluso generamos una rotacion

%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt


A = np.array([[-1,3],[2,-2]])
print(A)
# [[-1  3]
#  [ 2 -2]]
# que transformacion generara esta matriz, cuando se la aplicamos al vector?

vector = np.array([[2],[1]])
print(vector)
# [[2]
#  [1]]

# vamos a necesitar definir una funcion que va ser utilizada varias veces
# lo mejor es escribirla en un archivo separado para despues llamarlo desde este archivo
# Recibirá los vectores, los colores y el nivel de trasparencia con el cual trabajaremos 

def graficarVectores(vecs, cols, alpha = 1):
    
    # Agregamos el eje vertical. Este se cruzará en x = 0, el color será gris y el orden de z será 0 
    plt.axvline(x = 0, color = "grey", zorder = 0)
    # Agregamos el eje horizontal. Este se cruzará en y = 0, el color será gris y el orden de z será 0 
    plt.axhline(y = 0, color = "grey", zorder = 0)
    
    # Ahora ara cada uno de los vectores en el parámetro 
    for i in range(len(vecs)):
        # Tomaremos que la x es la concatenación de esos valores como 0 0 que es lo que estamos tomando como punto de origen 
        # Después de agregar el 0 0 le concatenamos el vector i 
        x = np.concatenate([[0,0], vecs[i]])
        # Vamos a graficar y agregamos todas las coordenadas
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   # Los ángulos estarán expresados en xy y la escuela de unidad será xy 
                   angles = 'xy', scale_units = 'xy',
                   # La escala con la que graficaremos será 1 
                   scale = 1,
                   color = cols[i],
                   alpha = alpha
                  )

print(vector)
# [[2]
#  [1]]
# queremos graficar el vector que habiamos definido pero necesitamos pasarselo de otra manera 
# lo que hace 'flatten' es devolvernos como una tira nuestro vector que estaba definido como una columna
print(vector.flatten())  #[2 1]
# cual es el efector de esto sobre una matriz?
# habitualmente a una imagen la vamos a tener representada en una matriz 
# y cuando queramos hacer cosas con algoritmos de deeplearning o machine learning
# vamos a tener que volverlas un vector alargado
#pero para nosotros es mejor continuar viendolo como una matriz 
# entonces vamos a utilizar el comando flatten
print(A)
# [[-1  3]
#  [ 2 -2]]
print(A.flatten()) # [-1  3  2 -2] 

graficarVectores([vector.flatten()], cols = 'blue')
plt.xlim(-0.5, 3)
plt.ylim(-0.5,2)


# para ver cual es la transformacion tenemos que defivnir al vector transformado
vector_transformado = A.dot(vector)
print(vector_transformado)
# [[1]
#  [2]]

graficarVectores([vector.flatten(), vector_transformado.flatten()], cols = ['blue', 'orange'])
plt.xlim(-0.5, 3)
plt.ylim(-0.5,2)
# lo que estamos viendo es que nuestro vector paso de ser [[2],[1]] y paso a ser el [[1],[2]]

# tambien podemos pedirle el determinante de nuestra transformacion
print(np.linalg.det(A))

# lo que hubieramos esperado es que estos dos vectores no tuvieran la misma norma 
# pero por una de esas casualidades ocurrio que conservamos la misma norma
print(np.linalg.norm(vector))
print(np.linalg.norm(vector_transformado))
```

### Autovalores y Autovectores

```py
# las transformaciones lineales ejercen transformaciones sobre nuestros vectores
# busquemos un vectore que cuando le aplicamos informacion no sufre ninguna modificacion
# Esto seria un 'autovector'
%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt


# vamos a necesitar definir una funcion que va ser utilizada varias veces
# lo mejor es escribirla en un archivo separado para despues llamarlo desde este archivo
# Recibirá los vectores, los colores y el nivel de trasparencia con el cual trabajaremos 

def graficarVectores(vecs, cols, alpha = 1):
    
    # Agregamos el eje vertical. Este se cruzará en x = 0, el color será gris y el orden de z será 0 
    plt.axvline(x = 0, color = "grey", zorder = 0)
    # Agregamos el eje horizontal. Este se cruzará en y = 0, el color será gris y el orden de z será 0 
    plt.axhline(y = 0, color = "grey", zorder = 0)
    
    # Ahora ara cada uno de los vectores en el parámetro 
    for i in range(len(vecs)):
        # Tomaremos que la x es la concatenación de esos valores como 0 0 que es lo que estamos tomando como punto de origen 
        # Después de agregar el 0 0 le concatenamos el vector i 
        x = np.concatenate([[0,0], vecs[i]])
        # Vamos a graficar y agregamos todas las coordenadas
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   # Los ángulos estarán expresados en xy y la escuela de unidad será xy 
                   angles = 'xy', scale_units = 'xy',
                   # La escala con la que graficaremos será 1 
                   scale = 1,
                   color = cols[i],
                   alpha = alpha
                  )

organge_light = '#FF9A13'
blue_light = '#1190FF'


X = np.array([[3,2],[4,1]])
print(X)

v = np.array([[1],[1]])
# lo que queremos hacer es encontrar un vectore que cuando le apliquemos la matriz siga siendo el mismo vector 
# incluso si esto fuera un multiplo del vectore original
u = X.dot(v)
print(u)
# [[5]
#  [5]]

graficarVectores([u.flatten(),v.flatten()], cols=[organge_light, blue_light])

plt.xlim(-1,6)
plt.ylim(-1,6)
# aqui lo que estamo teniendo es nuestro vector original que se llamaba 'v' con color azul
# que fue expandido al aplicarle nuestra transformacion x 
# y obtenemos el vector naranja 


# pero no es el mismo vectore, que es loq ue esta ocurriendo?
# lo que esta ocurriendo es que nuestro autovetor, nuestro autovalor  es el autovalor=5 
lambda_1 = 5
lambda_1 * v
# array([[5],
#        [5]])
# aqui lo que estamo diciendo es:
# que un autovector es aquel que cuando le aplico una matriz me devuelve el vector con la misma direccion pero puede tener una amplitud distinta
# osea que puede esta multiplicado por el autovalor 

# veamos que este valor no es unico, podemos tener otro
s = np.array([[-1],[2]])
print(s)

t = X.dot(s)
print(t)
# [[ 1]
#  [-2]]
# vemos que tenemos el mismo vector que el origial 
# que es lo que esta ocurriendo en este caso?
# es que esta siendo miltiplicado por -1

graficarVectores([t.flatten(), s.flatten()], cols=[organge_light, blue_light])

plt.xlim(-3,3)
plt.ylim(-3,3)
# al graficarlo vemos que esta tendiendo un cambio de direccion 
# pero la direccion se mantiene, asi que en realidad no es un cambio de direccion, es un cambio de sentido 
# El vector ahora apunta en el sentido opuesto 

# con esto vimos que una matriz de 2x2 tiene dos autovectores con dos autovalores asociados

# Aquí algunos datos útiles:

#     Para conseguir los autovalores y autoverctores de la matriz A, esta debe ser cuadrada (ej: 2x2, 3x3, 9x9…)
#     La matriz A tendrá tantos autovalores como dimensión tenga A (ej: una Matriz de 3x3 tiene 3 autovalores, matriz de 2x2 tiene dos autovalores)
#     Los autovalores pueden repetirse
#     Estos autovalores son los que forman los autovectores
#     Los autovectores deben ser base, es decir, que desde esos autovectores se pueda generar todo el espacio o demás vectores
# https://www.ciencia-explicada.com/2012/01/autovectores-otro-inutil-capricho-de.html#:~:text=En%20este%20caso%2C%20los%20autovalores,%C3%A1tomo%20de%20hidr%C3%B3geno%20(fuente).
```
### Cómo calcular los autovalores y autovectores

```py
# como calcular los autovalores y los autovectores?
%matplotlib inline

import numpy as np
import matplotlib.pyplot as plt

X = np.array([[3,2],[4,1]])
print(X)
# ya conocemos los resultados con lo cual ahora comparemos como podriamos encontrarlos sin ofrecerlos directamente

# python por medio de numpy nos ofrece la libreria 'np.linalg.eig' que Obtiene los autovalores y autovectores asociados
print(np.linalg.eig(X))
# (array([ 5., -1.]), array([[ 0.70710678, -0.4472136 ],
#        [ 0.70710678,  0.89442719]]))

autovalores, autovectores = np.linalg.eig(X)
print(autovalores) # [ 5. -1.]
print(autovectores[:,0]) #[0.70710678 0.70710678]
# pero ese autovector no se parece al que nostros teniamos, sera que es el mismo?
print(autovectores[:,1]) # [-0.4472136   0.89442719]
# este segundo autovector tampoco se parece al que teniamos de antes

# vamos a necesitar definir una funcion que va ser utilizada varias veces
# lo mejor es escribirla en un archivo separado para despues llamarlo desde este archivo
# Recibirá los vectores, los colores y el nivel de trasparencia con el cual trabajaremos 

def graficarVectores(vecs, cols, alpha = 1):
    
    # Agregamos el eje vertical. Este se cruzará en x = 0, el color será gris y el orden de z será 0 
    plt.axvline(x = 0, color = "grey", zorder = 0)
    # Agregamos el eje horizontal. Este se cruzará en y = 0, el color será gris y el orden de z será 0 
    plt.axhline(y = 0, color = "grey", zorder = 0)
    
    # Ahora ara cada uno de los vectores en el parámetro 
    for i in range(len(vecs)):
        # Tomaremos que la x es la concatenación de esos valores como 0 0 que es lo que estamos tomando como punto de origen 
        # Después de agregar el 0 0 le concatenamos el vector i 
        x = np.concatenate([[0,0], vecs[i]])
        # Vamos a graficar y agregamos todas las coordenadas
        plt.quiver([x[0]],
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   # Los ángulos estarán expresados en xy y la escuela de unidad será xy 
                   angles = 'xy', scale_units = 'xy',
                   # La escala con la que graficaremos será 1 
                   scale = 1,
                   color = cols[i],
                   alpha = alpha
                  )

v = np.array([[-1],[2]])
Xv = X.dot(v)

v_np = autovectores[:,1]

graficarVectores([Xv.flatten(), v.flatten(), v_np], cols = ['green', 'orange', 'blue'])

plt.ylim(-4,2)
plt.xlim(-7,3)
# lo que estamos viendo es que efectivamnete los 3 son el mismo vector en algun sentido 
# en el sentido de que conservan la misma direccion 
# lo unico que esta cmabiando es su amplitud
# y en algun caos tambien la direccion
# entonces lo que estamos tiendo es que lo que cambia es el autovalor asociado
# entonces podemos ver que al autovector encontrado por numpy es un multiplo del autovector que nosotros propusimos 
# que quiere decir esto?
# los autovectores son el mismo, lo que pueden variar es en amplitud o en direccion pero el sentido se mantiene  
```

### Descomposición de matrices

```py
# descomponer una matriz quiere decir entontrar dos o mas matrices que me puedan ayudar a escribir mi matriz original y que tengan ciertas propiedades
# como por ejemplo: cuando tenemos el 6, que lo podemos escribir como 3x2 y el 3 y el 2 tienen la propiedad de ser primos 
#A = ['autovectores']['autovalores']['inversa de  la matriz de autovectores']
import numpy as np

A = np.array([[3,2],[4,1]])
print(A)

autovalores, autovectores = np.linalg.eig(A)

print(autovalores)
print(autovectores)


# queremos ver que esto nos sirve para calcular estas matrices que dijimos
#A = ['autovectores']['autovalores']['inversa de  la matriz de autovectores']
# ['autovectores'] = v
# ['autovalores'] = lambda
# ['inversa de  la matriz de autovectores'] = v**1
A_calc = autovectores.dot(np.diag(autovalores)).dot(np.linalg.inv(autovectores))
print(A_calc)
# [[3. 2.]
#  [4. 1.]]
# y nos imprime exactamente la matriz que teniamos antes 
print(A)
# [[3 2]
#  [4 1]]

# tenemos otros descomposiciones que tambien son muy utiles 
# por ejemplo:
# en el caso de que nuestra matriz 'A' sea una matriz, real(que todos los numero que tiene dentro de la matriz son los numeros que conocemos habitualmente y no hay numero complejos ) y simetrica(que 'A' sea igual a 'A' traspuesta)
A = np.array([[3,2],[2,3]])
print(A)

print(A == A.T)
# [[ True  True]
#  [ True  True]]
# efectivamente coincide con su traspuesta 

autovalores, autovectores = np.linalg.eig(A)
print(autovalores) # [5. 1.]
print(autovectores)
# [[ 0.70710678 -0.70710678]
#  [ 0.70710678  0.70710678]]

# A = A.T
#A = v.diag(lamdas).v.T
# calcular una traspuesta es muchusimo mas sensillo y computacionalmente mas economico  que calcular una inversa
# entonces nuestro caso ideal seria que en lugar de tener una matriz cualquiera, tengamos una matriz real y simetrica 
# lo cual nos permitiria calcular todos estos numeros sin tener que realizar la inversa
A_calc = autovectores.dot(np.diag(autovalores)).dot(autovectores.T)
print(A_calc)
# [[3. 2.]
# [2. 3.]]
# y obtenemos asi nuestra matriz original
print(A)
# [[3 2]
#  [2 3]]

# de esta manera vimos que podemos escribir a nuestra matriz cuando es cuadrada en funcion de los autovalores y los autovectores 
# y en el caso de que sea simietrica podemos usar la traspuesta enlugar de la inversa 
```

### ¿Cómo descompongo una matriz no cuadrada (SVD)?

```py
# la descomposicion de matrices en autovalores y autovectores solo podemos efectuarla cuando nuestra matriz es cuadrada 
# eso quiere decir que no podemos descomponer una matriz que no sea cuadrada?
# no, para ello necesitamos la descomposicion en valores singulares(SVD)
# de que se trata la descomposicion en valores singulares?
# antes nostros teniamos  que podiamos descomponenlo todo en matrices cuadradas 
# ahora vamos a ver un ejemplo donde toda las matrices que tengamos van a ser distintas salvo la diagonal que tambien podria ser no cuadrada 
import numpy as np

A = np.array([[1,2,3],[3,4,5]])
print(A)

U, D, V = np.linalg.svd(A)

print(U)
# [[-0.46410668 -0.88577931]
#  [-0.88577931  0.46410668]]
print(D) # [7.97638869 0.61418515]
# 'D' nos r4egresa dos valores, si queremos ver la matriz de 'D' tenemos que:
print(np.diag(D))
# [[7.97638869 0.        ]
#  [0.         0.61418515]]
print(V)
# [[-0.39133557 -0.5605708  -0.72980603]
#  [ 0.8247362   0.13817999 -0.54837623]
#  [ 0.40824829 -0.81649658  0.40824829]]
# 'V' en este caso es una matriz de 3x3
# lo que estamos teniendo son dos matrices de 2x2 y por otro lado una matriz de 3x3
# entonces lo que obtendriamos al recontruir nuestra matriz es que lo vamos a estar escribiendo como:
# A = U D V

# los vectores y matrices pueden ser pensados como subtransformaciones del espacio
# si tuvieramos por ejemplo una matriz de 3x2, lo que estamos haciando al transformar el espacio
# es tomar un espacio de 'R3' y convertirlo en 'R2' 
# esto quiere decir que lo que estamos haciendo es condensar informacion que tenemos en el tercer eje dentro de los unicos dons ejes que vamos a conservar  
```