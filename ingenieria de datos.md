# INGENIERIA DE DATOS

Casi siempre estos datos vienen en un formato o estructura que no esta lista para el análisis adecuado.

La ingeniería de datos se preocupan principalmente por implementar los **pipelines** que permiten automatizar la obtención de datos y su posterior limpieza para que otros profesionales de los datos(científicos de datos o expertos en machine learning) puedan realizar su labor. Son la primera parte de la cadena.

Aprenderas como crear y automatizar un flujo **ETL** para extraer, transformar y guardar nuestros datos.

## ¿Qué es la Ciencia e Ingeniería de Datos?


La **Ciencia de Datos** es la disciplina que se encarga de extraer conocimiento de los datos disponible. Casi siempre cuando te realizas una pregunta sobre datos estas fuentes se encuentran escondidas, ocultas o de difícil acceso. A nuestro alrededor hay datos en tu computadora, mesa, reloj, etc.

**Los datos están por todas partes.**

La Ciencia de datos es multidisciplinaria. A diferencia de muchos otros ámbitos profesionales dentro del mundo de la tecnología cuando hablamos de un científico de datos es una persona que sabe de matemáticas, ingeniería de software y sabe de negocios.

Se apoya en la Computer science, Matemáticas(Regresiones e Inferencias).

También se auxilia de:

- Bases de Datos
- Análisis de texto y procesamiento de lenguaje natural
- Análisis de redes
- Visualización de datos
- Machine learning e Inteligencia Artificial
- Análisis de señales digitales
- Análisis de datos en la nube(Big Data)

## Roles

Existen por lo menos tres diferentes roles para tener un pipeline completo de ciencia de datos. Este post trata sobre el primer rol:

- **Data engineer**: Se encarga de obtener los datos, Limpiarlos y estructurarlos para posterior análisis, crear pipelines de análisis automatizado, utilización de herramientas en la nube, análisis descriptivo de los datos.

- **Data scientist**: Una vez tiene los datos se encarga de generar el análisis matemático de ellos, encontrar las relaciones entre las variables, las correlaciones, las causas y por último genera los modelos predictivos y prescriptivos.

- **Machine Learning engineer**: Se encarga de llevar las predicciones a escala, de subirlos a la nube y allí generar muchas predicciones. Se encarga de mantener la calidad del modelo.

## Librerias

### beautifulsoup4 
Sirve para parsear y manipular HTML.

### requests
Sirve para generar solicitudes a la web.

### numpy
Sirve para un análisis numéricos de datos.

### pandas
Sirve para analizar, modificar, transformar datos y generar análisis descriptivos sobre los mismos.

### matplotlib
Permite generar visualizaciones de los datos.

### yaml
Permite generar algunas configuraciones, es un archivo similar a Json.

## [Anaconda](https://docs.anaconda.com/ "Documentacion")

[**Anaconda**](https://www.anaconda.com/products/individual "Instalacion") es una instalación de Python que ya trae preinstalado todos los paquetes necesarios para tu labor en la Ciencia de Datos, tiene más de 1400 paquetes. Nos permite configurar ambientes virtuales para poder utilizar diferentes versiones de nuestros paquetes.

Una buena práctica es generar un ambiente virtual por cada proyecto, los ambientes virtuales nos permiten generar varios proyectos con diferentes versiones de la librería sin generarnos errores de compatibilidad. Tradicionalmente en Python se utiliza virtualenv

- Crear un entorno en anaconda
```
conda create --name [nombre-del-proyecto] [librerías-a-usar]
```

### Comandos

#### Crear un ambiente en anaconda
```
conda create --name nombre-del-proyecto librerías-a-usar
```

#### Activar el ambiente de anaconda
```
source activate nombre-del-proyecto
```

#### Salir del ambiente de anaconda
```
source deactivate
```

#### Ver los ambientes virtuales
```
conda env list
```

#### Eliminar un entorno virtual con todos sus paquetes
```
coda remove --name nombre-del-proyecto --all
```

#### Activar anaconda (base)
```
source ~/.bashrc
```
```
conda activate
```

#### Desactivar anaconda (base)
```
conda deactivate
```

#### Version de anaconda
```
conda --version
```

#### Todos los comandos de anaconda
```
conda --help
```

#### Ver los paquetes que anaconda instaló
```
conda list
```
