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