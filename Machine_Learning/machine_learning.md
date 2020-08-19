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

## Pytorch

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

