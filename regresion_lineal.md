# Regresion lineal y Machine Learning

## Proceso general del Machine Learning

1. Labeled observations: observaciones etiquetadas, es decir los datos que tenemos.

2. 
    - a) Set de datos de entrenamiento del modelo.

    - b) Set de datos de prueba, lo que se usara para validar el modelo.

3. Machine learner: el modelo matemático que se encarga de tomar los datos de entrenamiento y aprender con base en ellos.

4. Prediction model: despues del entrenamiento, se puede usar como un modelo predictivo. Al introducir datos nuevos, se deberian tener resultados diferentes.

5. Stats: evaluacion del modelo. En este sentido se debe estudiar la posibilidad de sobreajuste o subajuste.

**Regresión lineal**
Es un **algoritmo** de aprendizaje supervisado que se orienta a la prediccion, ejemplos:

- prediccion del crecimiento de la poblacion,
- prediccion del clima,
- prediccion del mercado.

## ML supervisado - Algoritmos

Algoritmos | Regresion | Clasificacion
-----------|-----------|---------------
Regresion Lineal | X | 
Regresion Logistica |  | X
Naive Bayes |  | X
K-nearest neighbors | X | X
Decision Tree | X | X
Random Forest | X | X

## Metodo de Minimos Cuadrados: Ecuacion

x | y | x - X | y - Y | (x - X)^2 | (x - X)(y - Y)
--|---|-------|-------|-----------|-----------------
1 | 2 |
2 | 3 |
3 | 5 |
4 | 6 |
5 | 5 |

`y = b0 + b1(x)`

Formula de minimos cuadrados:
```
sum(x - X)(y - Y)
-----------------      = b1
sum(x - X)^2
```
- **Proceso**

1. Sacar el promedio de 'x' y 'y':

`X = 3`
`Y = 4.2`

2. Llenar las columnas:

X | Y | x - X | y - Y | (x - X)^2 | (x - X)(y - Y)
--|---|-------|-------|-----------|-----------------
1 | 2 | -2 | -2.2 | 4 | 4.4
2 | 3 | -1 | -1.2 | 1 | 1.2
3 | 5 | 0 | .8 | 0 | 0
4 | 6 | 1 | 1.8 | 1 | 1.8
5 | 5 | 2 | .8 | 4 | 1.6

3. Con los datos de la tabla encontramos b1 con la formula de minimos cuadrados:

Formula de minimos cuadrados:
```
sum(x - X)(y - Y)
-----------------      = b1
sum(x - X)^2
```
```
 9
----    = b1
 10
```
4. Identificar coordenada principal

Como regla en la linea de regresion siempre debe de pasar por los componentes en 'x' y los componentes es 'y' del promedio.

`X = 3`
`Y = 4.2`

Las coordenadas serian:
`(3, 4.2)`

5. Remplazar valores con formula:

`y = b0 + b1(x)`

`4.2 = b0 + .9(3)`

`b0 = 1.5`

`y = 1.5 + .9(x)`

6. graficar

## Regresion en python

```py
import numpy as np
import matplotlib.pyplot as plt 

def estimate_b0_b1(x,y):
  # size nos ayuda a contar el tam;o de x
  n = np.size(x)

  # obtenemos los promedios de 'x' y de 'y'
  # np.mean saca el promedio
  m_x, m_y = np.mean(x), np.mean(y)

  # calcular sumatoria de XY y mi sumatoria de XX
  sumatoria_xy = np.sum((x - m_x)*(y - m_y))
  sumatoria_xx = np.sum(x * (x - m_x))

  # coeficientes de regresion
  b_1 = sumatoria_xy / sumatoria_xx
  b_0 = m_y - (b_1 * m_x)

  return (b_0, b_1)
```
```py
# funcion de graficado

def plot_regresion(x, y, b):
  plt.scatter(x, y, color='g', marker = 'o', s=30)

  y_pred = b[0] + (b[1] * x)
  # linea de codigo que se va a encargar de graficar
  plt.plot(x, y_pred, color = 'b')
  # etiquetado
  plt.xlabel('x-Independiente')
  plt.ylabel('y-Dependiente')

  plt.show()
```
```py
# codigo main

def main():
  # dataset
  x = np.array([1,2,3,4,5])
  y = np.array([2,3,5,6,5])

  # obtenemos b0 y b1
  b = estimate_b0_b1(x, y)
  print('los valores b0 = {}, b1 = {}'.format(b[0], b[1]))

  plot_regresion(x,y,b)

if __name__ == "__main__":
  main()
```
