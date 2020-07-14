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

## Tipos de datos

Los datos vienen en muchas formas y estas formas las podemos clasificar de diferentes maneras, permitiéndonos poder aplicar técnicas distintas a cada uno de los tipos de datos.

### Primitivos 

- int , str , bool, float, hex, oct, datetime, objetos especiales(clases).

### Estructurados

Los **estructurados** son los más fáciles de acceder a su información.

- Bases de datos
- Data warehouses

### Semi estructurados

Los **semi estructurados** son donde podemos usar las APIs.

- **Json** APIs
- Datos tabulares(csv, excel)
- HTML

### No estructurados

Los **no estructurados** son la mayoría de los datos que te vas a encontrar en tu desarrollo profesional.

- Texto libre
- Curriculum vitaes
- Imagenes, audios, social media
- Datos cientificos


## Fuentes de datos

De donde obtener datos.

- **Web**

    - Es una mina enorme con datos financieros, de startups, del clima, precipitación fluvial, astronómicos, de negocios, etc.

    
- **APIs**

    - Endpoints que viven en la web y nos devuelven **JSON**. Por ejemplo, la API de twitter, google, facebook.

    
- **User Analytics**

    - Son el comportamiento del usuario dentro de nuestra aplicaciones, algo similar a los que nos ofrece Google Analytics.

- **IoT**

    - Se ha vuelto una mina espectacular en los últimos años. Como automóviles.
   

### Links de fuentes de datos

- [Data.world](https://data.world/ "Data.world")

- [API Library](https://console.cloud.google.com/apis/library?pli=1 "API Library")

- [Kaggle](https://www.kaggle.com/ "Kaggle")

- [Informacion del gobierno](https://datos.gob.mx/ "Informacion del gobierno")

- [Google Dataset](https://datasetsearch.research.google.com/ "Google Dataset")


## Roles

Existen por lo menos tres diferentes roles para tener un pipeline completo de ciencia de datos. Este post trata sobre el primer rol:

- **Data engineer**: Se encarga de obtener los datos, Limpiarlos y estructurarlos para posterior análisis, crear pipelines de análisis automatizado, utilización de herramientas en la nube, análisis descriptivo de los datos.

- **Data scientist**: Una vez tiene los datos se encarga de generar el análisis matemático de ellos, encontrar las relaciones entre las variables, las correlaciones, las causas y por último genera los modelos predictivos y prescriptivos.

- **Machine Learning engineer**: Se encarga de llevar las predicciones a escala, de subirlos a la nube y allí generar muchas predicciones. Se encarga de mantener la calidad del modelo.

## ETL

**ETL** = Extract Transform Load

**Extract**: Es el proceso de lectura de datos de diversas fuentes

- Base de datos
- CRM
- Archivos CSV
- Datasets públicos

**Transform:** En este momento cuando nosotros tenemos que transformar los datos, tenemos que identificar datos faltantes o datos erróneos o una edad negativa. En esta etapa donde tenemos que identificar todos los problemas y solucionarlos.

- Limpieza
- Estructurado
- Enriquecimiento.

**Load**: Una vez transformados debemos insertarlos en el data warehouse

- Depende del tipo de solución que se haya escogido


## Librerias

#### beautifulsoup4 
Sirve para parsear y manipular HTML.

#### requests
Sirve para generar solicitudes a la web.

#### numpy
Sirve para un análisis numéricos de datos.

#### pandas
Sirve para analizar, modificar, transformar datos y generar análisis descriptivos sobre los mismos.

#### matplotlib
Permite generar visualizaciones de los datos.

#### yaml
Permite generar algunas configuraciones, es un archivo similar a **Json**.

## [Anaconda](https://docs.anaconda.com/ "Documentacion")

[**Anaconda**](https://www.anaconda.com/products/individual "Instalacion") es una instalación de Python que ya trae preinstalado todos los paquetes necesarios para tu labor en la Ciencia de Datos, tiene más de 1400 paquetes. Nos permite configurar ambientes virtuales para poder utilizar diferentes versiones de nuestros paquetes.

Una buena práctica es generar un ambiente virtual por cada proyecto, los ambientes virtuales nos permiten generar varios proyectos con diferentes versiones de la librería sin generarnos errores de compatibilidad. Tradicionalmente en Python se utiliza virtualenv

- Crear un entorno en anaconda
```
conda create --name [nombre-del-proyecto] [librerías-a-usar]
```

### Comandos de anaconda

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
concomda remove --name nombre-del-proyecto --all
```

#### Instalar jupyter en un entorno virtual ya creado
```
conda install -c anaconda jupyter
```

#### Abrir el navegador de anaconda
```
conda activate
anaconda-navigator
```

#### Inicializar el servidor de jupyter
```
conda activate
jupyter notebook
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

## Jupyter Notebooks

Algo interesante que tenemos con Anaconda es que nos trae Jupyter Notebooks.

Jupyter Notebooks es un entorno de programación en el cual podemos mezclar ejecución de código en vivo, visualizaciones y añadir **markdown**.

Markdown es un tipo de formato para escribir texto de manera sencilla, en donde podemos agrega pedazos de formato como headers, etc.

### Comandos de jupyter notebooks

- Inicializar el servidor de jupyter
```
conda activate
jupyter notebook
```
#### Atajos de teclado

- Ver todos los comando que tiene jupyter
```
p
```

- Modo edicion (celda color verde)
```
enter
```

- Modo navegacion (celda color azul)
```
esc
```

- Ejecutar el codigo
```
ctrl + enter
```

- Ejecutar el codigo y añadir una nueva celda
```
shift + enter
```

- Agregar celda
```
b
```

- Moverse entre celdas
```
k
```
```
j
```

- Convertir a markdown (texto)
```
m
```

- Cortar celda
```
x
```

- Pegar celda 
```
v
```

- Eliminar celda
```
dd
```


## Tecnologías web

Las tecnologías web en principio podemos pensarlas como el internet, pero el internet es mucho más grande, es la red de redes, la forma en la que millones de computadores se conectan entre ellas para transferirse información.

El internet también se compone de otros pedazos como **telefonía**(voip), **mail**(pop3, imap), **compartir archivos**(ftp). El internet es una red que une varias redes públicas, privadas, académicas, de negocios, de gobiernos, etc.

La **web** específicamente es un espacio de información en el cual varios documentos(y otros recursos web) se pueden acceder a través de URLs y vínculos(links). La comunicación se da a través del protocolo **HTTP**.

Elementos básicos de la web:

- **HTML**: nos da la estructura de la información. Es un lenguaje para anotar pedazos de información para que el navegador o otros tipos de programa puedan interpretar que tipo de información se encuentra ahí.

[**Web Scraping**](https://en.wikipedia.org/wiki/Web_scraping "Web Scraping")

- **CSS**: nos permite darle colores, arreglar el texto y añadir diferentes elementos de presentación.

- **Javascript**: nos permite añadir interactividad y cómputo a nuestra web.

[**Single Page Web Applications**](https://es.wikipedia.org/wiki/Single-page_application "Single Page Web Applications"): Son apliaciones que su motor basico es el javascript y si no corremos javascript no se pueden renderizar (no podemos ver que hay adentro).
Existen mecanismos como [**Puppeteer**](https://www.npmjs.com/package/puppeteer "Puppeteer") que me permite manipular programaticamente un web browser para que podamos renderizar la pagina y poder saber que hay ahi adentro

- **JSON**: Simplemente es una forma de transmitir datos entre servidores y clientes. Es la forma estándar en las que en la web y las aplicaciones se comunican con los servidores backend.



