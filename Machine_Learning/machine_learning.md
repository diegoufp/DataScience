# Machine Learning

## Introducción a la terminología de Machine Learning

### AI(Inteligencia Artificial)
Se refiere a la capacidad de una maquina de realizar tareas que requieren de la inteligencia de un ser humano, cumpliendolas al mismo nivel o siendo mejor que una persona.

### ML(Aprendizaje automatico)
Subcampo de AI que involucra brindar a maquinas, la habilidad de realizar una tarea especifica, sin necidad de que este programada explicitamente para realizarla.

- **Principales tipo de ML**

    - Supervised learning(Aprendizaje supervisado)
    Este tipo requiere etiquetas, los datos tendrás etiquetas de sí o no.

    - Unsupervised learning(Aprendizaje sin supervision)
    Nuestras variables de entrada tendrán un peso para luego sumar esas variables y tendremos un resultado. Esto no es más que una regresión lineal.

    - Reinforcement learning(Aprendizaje por refuerzo autonomo)
    Si solo tengo las variables de entradas. Se puede agrupar y buscar patrones. Tomar acciones para maximizar la recompensa en una situación específica.

### DL(Aprendizaje profundo)
Deep Learning es un tipo de ML que utiliza redes neuronales (artificial neuronal networks) que pueden aprender asociaciones entre sus entradas y salidas. Es ML con redes neuronales de muchas capas que pueden aprender asociaciones entre entrada y salidas. Estas redes con diferentes nodos y se asemejan a como funciona una neurona del cuerpo humano.

**Artificial Neural Network**
Sistema de software contruido por nodos interconectados. Puede ser una transformacion lineal(peso + bias) o no-linea(funcion de activacion)

## Terminología y regresión lineal

La regresión lineal nos va a dar justo lo que queremos como resolución de un problema de ML. Partimos de una ecuación

- Label (y)
Etiqueta de lo que estamos prediciendo. Variable de salida

- Feature(x)
Una variable de entrada

- Modelo
Define una relacion entre features y labels

- Training
Darle una dataset al modelo y permitirle aprender de datos con label

- Inference
Usar el modelo para realizar predicciones

Para construir un modelo usamos las variables de entrada siendo necesario normalizar una para tener una representación numérica y construimos una ecuación.

La diferencia que puede haber entre el resultado y el valor real debemos tratar de que no exista para que la predicción sea lo más cercana posible al valor real, no será al 100%, pero la diferencia o pérdida debe ser baja. Para llegar a eso debemos escoger el peso correcto.

## Training &amp; Loss
Hablaremos del proceso de entrenamiento y cómo minimizar la pérdida. Queremos que nuestro modelo quede de la mejor forma posible.

Nuestro objetivo es minimizar la pérdida.

Para calcular el error usamos una fórmula llamada MSE(Mean Squared Error). Para minimizar la diferencia usamos el **gradiente**, el gradiente es un vector por lo tanto tiene direccion y magnitud, y se va a calcular con una **derivada parcial**.

La derivada parcial nos va a servir para entontrar el gradiente que nos va a decir en que direccion y cuanto debemos movernos. Eventualmente eso me va a dar un siguiente punto y se va a repetir el proceso hasta llegar al punto minimo. Cada paso va a tener un tama;o eso va a depender mucho de a algo llamado **learning rate**, la taza a la que el modelo va  aprender es un hiperparametro y ese hiperpasamegro va a decir que tan peque;os o grandes son los pasos que estamso dando. Este learning rate lo tenemos que definir de tal forma que llegemos de forma eficiente al minimo.

**Stochastic Gradient Descent(SGD)**: Es estocástico porque será aleatorio y tenemos opciones para realizar el gradiente en busca del mínimo. ¿Deberíamos calcular el gradiente de todo el dataset? Puede ser más eficiente elegir ejemplos aleatorios. Un solo ejemplo es muy poco, trabajamos con un batch.

**El proceso de aprendizaje** requiere iniciar los pesos de los valores para calcular la pérdida que estamos teniendo, con la ecuación vista tendremos una idea de qué tan lejos está nuestra predicción de lo real y así evaluar el desempeño de nuestro modelo. Repetimos utilizando el gradiente como referencia para acércanos al peso donde podemos minimizar la pérdida.

- La fase de entrenamiento es un proceso iterativo
- Al calcular el error(loss), el gradiente nos ayuda a buscar el mínimo
- Es necesario calibrar el valor de learning rate

## [Pytorch](https://pytorch.org/tutorials/beginner/pytorch_with_examples.html "Pythorch")

PyTorch es un framework, va a ser nuestro apoyo con características importantes como múltiples funciones que nos ayudan en la construcción de nuestro modelo. Implementaremos una regresión lineal y otras aproximaciones de modelos de clasificación, para cada uno de estos casos utilizaremos módulos del framework.

Al trabajar con PyTorch o algún framework de ML nuestra herramienta principal son los tensores.

Un tensor no es más que una generalización, no es más que una estructura de datos que nos permite representarlo de manera genérica

[Google Collaboratory](https://colab.research.google.com/notebooks/intro.ipynb "Google Collaboratory") es una implementación de Jupyter Notebooks que esta en la nube. No requerimos configurar nada.

**Proceso de aprendizaje**

- Forward pass(prediccion)
- Backpropagation(iterarcion)
- Optimización

## Trabajando con tensores

[Google Collaboratory](https://colab.research.google.com/notebooks/intro.ipynb "Google Collaboratory") es una implementación de Jupyter Notebooks que esta en la nube. No requerimos configurar nada.

Creamos una 'new notebook'

```python
import torch
```
```
torch.__version__
```
```python
tensor_a = torch.ones(2, 2)
# V a dar de resultado un tensor de dimencion 2 x 2 que tiene unicamnete 1's
tensor_a
```
```python
# Podemos llamarlo tambien con un metodo llamato Tensor
tensor_b = touch.Tensor(2, 2)
# V a tener dos valores aleatorios
print(tensor_b)
# Vamos a hacer un metodo que uniforme de tal manera que los valores sean entre 0 y 1
tensor_b.uniform_(0, 1)
```
```python
# Podemos crear un tensor con valores aleatorios de otra amnera
tensor_c = torch.rand(2, 2)
# El metodo rand si lo genera entre 0 y 1
tensor_c
```
```python
# Tambien se pueden hacer operaciones
result = tensor_b + tensor_c
result
```
```python
# Con el metodo shape se puede imprimir
result.shape
reshaped = result.view(4, 1)
```
```python
# Vamos a crear un numero tensor ahora no sera aleatorio se creara con el metodo tensor con 't' minuscula
points = torch.tensor([1.0, 2.0],[3.0, 4.0])
print(points)
# Para imprimir un solo valor se puede hacer lo mismo que una matriz
points[0][1]
# Y para modificar 
points[0][1] = 2.5
print(points)
#Como se tienen multiples dimenciones esto se puede guardar de diferentes maneras
# Si quieres sabe de que forma esta guardado se utiliza el metodo storage
points.storage()
```
```python
points, points.stride()
```
```python
# SI lo trasponemos cambiara el stride
p_t = points.t()
p_t, p_t.stride()
```
```python
# Podemos agregar dimeciones
tensor_x = torch.tensor([1, 2, 3, 4])
# Con el metodo unsqueeze se pueden agregar dimenciones
torch.unsqueeze(tensor_x, 0)
# Si en lugar de un 0 ponemos un 1 la forma en que se agrega la dimecion es vertical, esto nos va a servir cuando estemos manipulando imagenes
torch.unsqueeze(tensor_x, 1)
```

- Interaccion con numpy

```python
import numpy as np
numpyArray = np.random.randn(2,2)
# Se puede crear un tensor nuevo apartir de este arreglo
torch.from_numpy(numpyArray)
```

## Representando datasets con tensores

Para entender mas sobre las dimecionalidades leer este [articulo](https://towardsdatascience.com/understanding-dimensions-in-pytorch-6edf9972d3be "articulo")

```python
import torch
import numpy as np
numpyArray = np.random.randn(2,2)
# Se puede crear un tensor nuevo apartir de este arreglo
from_numpy = torch.from_numpy(numpyArray)
```

- Media
```python
# El resultado sera la media del tensor pero sera un solo numero.
torch.mean(from_numpy)
# Tambien se puede calcular atravez de dimenciones
torch.mean(from_numpy, dim=0) # dimencion 0
torch.mean(from_numpy, dim=1) # dimencion 1
```

- Desviacion estandar
```python
torch.std(from_numpy, dim=1)
```

- Guardar el tensor
```python
torch.save(from_numpy, 'tensor.t')
```

- Cargar tensor
```python
load = torch.load('tensor.t')
```

En este [url](https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv 'url') es un dataset.

Usaremos un metodo de pandas para que todo ese contenido se carge a una variable.

```python
import pandas as pd
# DataFrame es una representacion de filas y columnas
url = 'https://raw.githubusercontent.com/amanthedorkknight/fifa18-all-player-statistics/master/2019/data.csv'
dataframe = pd.read_csv(url)
dataframe
```
```python
# Para ver cuales son las columnas
dataframe.columns
```
```python
subset = dataframe[['Overall', 'Age', 'International Reputation', 'Weak Foot', 'Skill Moves']]
columns = subset.columns[1:]
# La informacion de los jugadores se pasa a un tensor 
# Especificando de este subset los valores y convertirlo a flotante para que sea mas facil es calculo de operaciones
players = torch.tensor(subset.values).float()
# El shape me va a dar el tama;o
players.shape, players.type()
```
```python
# Vamos a mostrar las columnas de interes
data = players[:, 1:]
data, data.shape
```
```python
# Vamos a mostrar la primera columna
target = players[:, 0]
target, target.shape
```
En esta ocacion pueden existir jugadores que no tengan cierta informacion, para evitar que en las operaciones te pueda salir un 'Nan' vamos a utilizar [dropna](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.dropna.html?highlight=dropna#pandas.DataFrame.dropna "dropna")
```python
# Vamos a regresar a donde creamos el subset
# Agregamos que elimine los valores en el eje de las filas cuando cualquiera sea null o no exista
# Esto se hace con dropna que es un metodo de pandas
# axis recibe cómo parametro un 1 y un 0.
# 0 indica que se borrará la fila donde encontremos valores faltantes
# 1 se borrará la columna donde se encuentre un valor faltante.
# how recibe cómo parametro ‘any’ y ‘all’
# ‘any’ significa que si encuentra al menos una columna con dato faltante, la elimine (en este caso, lo que haría sería ver el parametro axis para ver que acción debe tomar)
# ‘all’  significa que debe eliminar la fila donde todos sus datos estén vacíos. además puede recibir otros parámetros.
subset = dataframe[['Overall', 'Age', 'International Reputation', 'Weak Foot', 'Skill Moves']].dropna(axis=0, how='any')
```
Ahora si calculamos la media y desviacion estandar todos los valores estaran llenos
```python
mean= torch.mean(data, dim=0)
std = torch.std(data, dim=0)
```
- Normalizar los datos
```python
# Los datos lo vamos a normalizar restandole a la media a cada elemento y luego dividiendo por el cuadrado de la desviacion estandar.
# la funcion de cuadrado tambien esta presente en la biblioteca pytorch
norm = (data - mean)/torch.sqrt(std)
norm
# Ahora ya todo estan en un mismo rango 
```

- Aproximaciones intuitivas
```python
# vamos a traer los buenos jugadores
# torch.ge() --> ge = GreaterEqual (>=)
godd = data[torch.ge(target, 85)]
average = data[torch.gt(target, 70) & torch.lt(target, 85)]
notSoGood = data[torch.le(target, 70)]

goodMean = torch.mean(good, dim=0)
averageMean = torch.mean(average, dim=0)
notSoGoodMean = torch.mean(notSoGood, dim=0)
```
```python
# vamos a imprimirlo mas bonito con esta funcion
# El zip une multiples variables y va a ser un argumento para enumerate(para iterar)
# Vamos a iterar un indice y los argumentos
for i, args in enumerate(zip(columns, goodMean, averageMean, notSoGoodMean)):
    print('{:25} {:6.2f} {:6.2f} {:6.2f}'.format(*args))
```

## Implementación de regresión lineal
```python
import torch
import numpy as np
import torch.nn as nn # para implementar la regresion lineal(de redes neuronales)
import torch.optim as optim # es de optimizaciones para calculas los gradientes y hacer un Backpropagation
import matplotlib.pyplot as plt # para graficar
```
```python
car_prices = [5, 6, 7, 8, 9, 10]
units_sold = [5.5, 8, 7.5, 7.0, 6.5, 6.0]
# lo graficamos
plt.scatter(car_prices, units_sold)
```
```python
# Convertiremos este arreglo de python a un arreglo de numpy
# la intencion de esta conversion (python -> numpy -> tensor) es que se aclare el proceso de conversion de datos
prices_array = np.array(car_prices).reshape(-1, 1)
# el arreglo que se tenia antes ahora tiene un formato distinto 
prices_array
# Esto va a servir para cuando se envia a pytorch y convertirlo en un tensor
```
```python
# Se convertiran en tensores los dos casos
# del metodo requires_grad_(True) el ultimo guiob bajo '_' va a modificar el arreglo que vamos a usar para convertir a un tensor
# y el tensor es el que sufre esta modificacion, por lo tanto va quedar de una vez con los gradientes activados 
prices = torch.from_numpy(prices_array).float().requires_grad_(True)
# Las units no necesitan los gradientes por que son el target a explicar
units = torch.from_numpy(units_array).float()
prices, prices.shape
```
```python
# Nuestro modelo es un modelo lineal
model = nn.Linear(1, 1)
# luego se tiene que definir la perdida
loss_function = nn.MSELoss()
# y por ultimo definir el optimizador
# Stochastic Gradient Descent(SGD) es decir que no se trabajo con el dataset completo ni con un solo dato, se ultiliza un puto intermedio
# El learning rate (lr) son los pasos que se ban dando en busca de minimizar el loss atravez des gradiente(es uno de los hiperparametros que se pueden calibrar)
optimizer = optim.SGD(model.parameters(), lr=0.015)
losses = []
iterations = 2000 #es algo que puede calibrarse
# Se graficaran los loss vs numero de iteraciones
for i in range(iterations):
  pred = model(prices)
  # en el loss se le envia la prediccion junto con el taget(cuanto estoy adivinando y cuanto es en realidad)
  loss = loss_function(pred, units)
  losses.append(loss.data)
  # se van a reiniciar los gradientes 
  # La razon es que pytorch acumula, si no hacemos esto el resultado no va a ser el que buscamos por que los gradientes se siguen acumulando por cada iteracion
  optimizer.zero_grad()
  # backpropagation
  loss.backward()
  # Despues vamos a ahcer un step, es decir, en base a los gradientes que se calcularon me muevo un poco en direccion del minimo
  optimizer.step()
  # Esto seria nuestro tranding loop (estamos entrenado el modelo)

print(float(loss))
plt.plot(range(iterations), losses)
```
```
# Cuando un modelo ya a sido entrenado ahora deberia de poder predecir 
x = torch.Tensor([[4.0]])
p = model(x)
p
```

## Regresion logica

**Regresion logistica**
Son un mecanismo eficiente para calcular probabilidades. El resultado puede utilizarse tal cual o convertirlo a una categoria binaria(para clasificar).

**Garantizando resultado[0,1] entre cero y uno**
Para una clasificacion bunaria, nos apoyamos en una funcion matematica llamada **Sigmoide**. Si en caso la clasificacion tuviera mas parametros, hariamos uso de la funcion **Softmax**.

**Funcion Sigmoid**: y = 1/(1+(e)**-z)

A la relacion lineal se le va  agregar este sigmoide que va a dar una probabilidad y asi se resuelve el problema de pasar de una regresion lineal(que esta en el dominio continuo) a una regresion(logistica que esta en el dominio discreto).

Por este cambio el **MSE** ya no va a ser la mejor forma de calcular el **Loss**, asi que el loss function tambien debe cambiar. La aproximacion intuitiva es castigar cuando el valor es 0 y la prediccion resulta en 1 (o viceversa).  Esto se logra con el logaritmo porque nos permite modelarlo perfectamente y ahora nuestra función de pérdida o LOSS va a incluir logaritmos **Binary Cross Entropy** o **Log Loss**.

- Para problemas de probabilidad, utilizamos una regresión logística
- Para calcular el error(loss), nos basamos en la entropía pero el gradiente sigue siendo útil



