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

