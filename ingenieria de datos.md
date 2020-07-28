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
BeautifulSoup nos ayuda a organizar gramaticalmente(parsear) el documento HTML para que tengamos una estructura con la cual podamos manejar y extraer información. BeautifulSoup convierte el string de HTML en un árbol de nodos para poder manipularlo.

#### requests
Sirve para generar solicitudes a la web.

#### numpy
Sirve para un análisis numéricos de datos.

#### pandas
Sirve para analizar, modificar, transformar datos y generar análisis descriptivos sobre los mismos.

#### matplotlib
Permite generar visualizaciones de los datos.

#### argparse

#### logging

#### yaml
Permite generar algunas configuraciones, es un archivo similar a **Json**.

#### requests
Permite generar solicitudes a la web dentro de python y nos permite utilizar todos los diferentes verbos HTTP
- GET, POST, PUT, DELETE, PATCH, OPTIONS

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

### HTML: 
**HTML** nos da la estructura de la información. Es un lenguaje para anotar pedazos de información para que el navegador o otros tipos de programa puedan interpretar que tipo de información se encuentra ahí.

[**Web Scraping**](https://en.wikipedia.org/wiki/Web_scraping "Web Scraping")

### CSS:
**CSS** nos permite darle colores, arreglar el texto y añadir diferentes elementos de presentación.

### Javascript: 
**Javascript** nos permite añadir interactividad y cómputo a nuestra web.

[**Single Page Web Applications**](https://es.wikipedia.org/wiki/Single-page_application "Single Page Web Applications"): Son apliaciones que su motor basico es el javascript y si no corremos javascript no se pueden renderizar (no podemos ver que hay adentro).
Existen mecanismos como [**Puppeteer**](https://www.npmjs.com/package/puppeteer "Puppeteer") que me permite manipular programaticamente un web browser para que podamos renderizar la pagina y poder saber que hay ahi adentro

### JSON: 
**JSON** simplemente es una forma de transmitir datos entre servidores y clientes. Es la forma estándar en las que en la web y las aplicaciones se comunican con los servidores backend.


## Solicitudes a la web

Para poder experimentar con la web necesitamos un método programático para solicitar URLs y obtener HTML

**Requests**: Nos permite generar solicitudes a la web dentro de Python y utilizar los diferentes verbos HTTP, normalmente utilizaremos el método GET porque vamos a traer datos.

requests.get('url') para hacer una solicitud a la web y nos devolverá un objeto response

### Ejemplo en jupyter

```python
import requests

response = requests.get('https://www.platzi.com')
```
Toda la documentacion esta dentro de "response" y la podemos ver de dos maneras:

1. En este nos dara el codigo fuente del objeto response
```python
response??
```
2. En este nos dara todo los metodos que podermos utilizar con este objeto.
```python
print(dir(response))
```

Todas las solicitudes HTTP tienen metadatos para que los diferentes sistemas y computadoras puedan entender de qué va la solicitud.

#### Ver el HTML
```python
print(response.text)
```

#### Ver los headers
```python
print(response.headers)
print(response.headers['Date'])
```

#### Codigos de estado del protocolo http
- Los mas comunes son:
    - 200 : OK - Petición correcta.
    - 400 : Bad request - Petición incorrecta.
    - 404 : Not found - Recurso no encontrado.

- Estos códigos estan categorizados en los siguientes grupos:

    - 1xx : Respuestas informativas (Ej: 100, 101, 102, etc.)
    - 2xx : Peticiones correctas (Ej: 200, 201, 202, etc.)
    - 3xx : Redirecciones (Ej: 300, 301, 302, etc.)
    - 4xx : Errores en el lado del cliente (Ej: 400, 401, 402, etc.)
    - 5xx : Errores en el lado del servidor (Ej: 500, 501, 502, etc.)

```python
print(response.status_code)
```

## Extraccion de informacion del HTML

Para poder desarrollar scrapers debemos entender los datos semi estructurados dados por el HTML para determinar qué tipo de selectores CSS necesitamos para sacar información.

En el caso de Python la librería estándar para manipular los documentos HTML se llama **BeautifulSoup**.

**BeautifulSoup** nos ayuda a organizar gramaticalmente(parsear) el documento HTML para que tengamos una estructura con la cual podamos manejar y extraer información. BeautifulSoup convierte el string de HTML en un árbol de nodos para poder manipularlo.

Para manipularlo podemos usar los selectores CSS con:
```python
soup.select()
```

### Ejemplo en jupyter
Apoyarse del [anterior ejemplo](https://github.com/diegoufp/DataScience/blob/master/ingenieria%20de%20datos.md#ejemplo-en-jupyter "anterior ejemplo") para desarrollar el ejemplo siguiente.

```python
import bs4

soup = bs4.BeautifulSoup(response.text, 'html.parser')
```

De segundo parametro elegimos el tipo de parser a utilizar, se define porque BeautifulSoup tambien nos puede ayudar a manipular documentos de tipo xml.

- Ver los vinculos a la url.Agregar este codigo al anterior:

```python
courses_links = soup.select('.HomeCategories-item > a')
courses = [course['href'] for course in courses_links]

for course in courses:
    print(course)
```


## Page Object Patter

Un buen **Data engineer** utiliza los conceptos de la ingeniería de software para poder desarrollar sus programa. En nuestro caso para poder desarrollar nos apoyaremos de un patrón.

**Page Object Patter**: Es un patrón que consiste en esconder los queries especificos que se utilizan para manipular un documento HTML detrás de un objeto que representa la página web.

Si estos queries se añaden directamente al código principal, el código se vuelve frágil y va a depender mucho de la modificación que hagan a la web otras personas y arreglarlo se vuelve muy complicado.


## Implementando un web scapper

### Configuración
Se creeara una carpeta y dentro de ella se crearan 3 archivos. Los nombres pueden ser distintos.

```
mkdir web_scrapper
cd web_scrapper
touch config.yaml
touch common.py
touch main.py
```

En el archivo "config.yalm" siemplemente se generara un mapa de mapas y las propiedades de los mapas que se encuentran dentro del mapa inicial van a ser las que vamos  autilizar.

```
vim config.yaml
```
```yaml
news_sites:
    eluniversal:
        url: https://www.eluniversal.com.mx/
    elpais:
        url: https://elpais.com/mexico/
```
---------------------------------------------------
```
vim common.py
```
```python
import yaml

# Esta variable ___config nos va a servir para poder cahear nuestra configuracion.
# Es importante hacer esto por que estamos leyendo a disco
# Y si queremos utilizar nuetsra configuracion en varias partes de nuestro codigo, 
# no queremos leer a dsico cada vez que tengamos que utilizar la configuracion.
__config = None

# Con esto vamos a leer el archivo una sola vez
# Y si ya tenemos la configuracion cargada no tenemos que volver a leer el archivo
# simplemente vamos a regresarlo 
def config():
    global __config
    if not __config:
        with open('config.yaml', mode='r') as f:
            __config = yaml.load(f)

    return __config
```
------------------------------------------------------
```
vim main.py
```
```python
import argparse
import logging
logging.basicConfig(level=logging.INFO)

from common import config

logger = logging.getLogger(__name__)

def _new_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logging.info('Beginning scraper for {}'.format(host))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    news_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site', 
                        help='The news site that you want to scrape', 
                        type=str, choices=news_site_choices)

    args = parsert.parse_args()
    _news_scraper(args.news_site)
```

### Obteniendo enlaces del front page

Hora que ya tenemos el esqueleto de nuestra aplicacion lista, lo siguiente que tenemos que hacer es ir a la pagina principal del sitio de noticias e identificar todos los vinculos dentro de esa pagina que nos llevaran a los articulos de noticia.

Para esto crearemos un nuevo archivo:
```
touch news_page_objects.py
```
```
vim news_page_objects.py
```
```python
import bs4
import requests

from common import config

class HomePage:

    def __init__(self,news_site_uid, url):
        self._config = config()['new_sites'[news_site_uid]
        self._queries = self.__config['queries']
        self._html = None

        self._visit(url)

    @property
    def article_links(self):
        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)

        return set(link['href'] for link in link_list)

    def _select(self, query_string):
        return self._html.select(query_string)

    def _visit(self, url):
        response = requests.get(url)

        response.raise_for_status()
        
        self._html = bs4.BeautifulSoup(response.text, 'html.parser')
```

Ahora se editara el archivo de configuracion para agregar nuestros queries
```
vim config.yaml
```
```yaml
news_sites:
    eluniversal:
        url: https://www.eluniversal.com.mx/
        queries:
            homepage_article_links: '.field-content a'
    elpais:
        url: https://elpais.com/mexico/
        queries:
            homepage_article_links: '.articulo-titulo a'
```

Ahora se modificara el archivo principal
```
vim main.py
```
```python
import argparse
import logging
logging.basicConfig(level=logging.INFO)

import news_page_objects as news
from common import config

logger = logging.getLogger(__name__)

def _new_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logging.info('Beginning scraper for {}'.format(host))
    homepage = news.HomePage(news_site_uid, host)

    for link in homepage,article_links:
        print(link)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    news_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site', 
                        help='The news site that you want to scrape', 
                        type=str, choices=news_site_choices)

    args = parsert.parse_args()
    _news_scraper(args.news_site)
```

### Obteniendo artículos

Ya tenemos una forma de extraer vinculos de la pagina principal de una pagina, ahora lo que tenemos que hacer es validar que estos vinculos se encuentren en el formato correcto que necesitamos, si no estan en este formato, tenemos que converitlos. Y una vez que tengamos nuestra lista de vinculos que queremos visitar, tenemos que ir visitando cada una de estas paginas y extraer el titulo y el cuerpo del articulo para ir contruyendo nuestro data set.

Primero vamos abrir nuestro archivo de configuracion:
```
vim config.yaml
```
```yaml
news_sites:
    eluniversal:
        url: https://www.eluniversal.com.mx/
        queries:
            homepage_article_links: '.field-content a'
            article_body: '.field-name-body'
            article_title: '.pane-content h1'
    elpais:
        url: https://elpais.com/mexico/
        queries:
            homepage_article_links: '.articulo-titulo a'
            article_body: ''
            article_title: ''
```

Ahora modificaremos el archivo page_objects para incluir el articulo:
```
vim news_page_objects.py
```
```python
import bs4
import requests

from common import config

class NewsPage:

    def __init__(self, news_site_uid, url):
        self._config = config()['new_sites'[news_site_uid]
        self._queries = self._config['queries']
        self._html = None

        self._visit(url)

    def _select(self, query_string):
        return self._html.select(query_string)

    def _visit(self, url):
        response = requests.get(url)

        response.raise_for_status()
        
        self._html = bs4.BeautifulSoup(response.text, 'html.parser')

class HomePage(NewsPage):

    def __init__(self,news_site_uid, url):
        super().__init__(news_site_uid, url)


    @property
    def article_links(self):
        link_list = []
        for link in self._select(self._queries['homepage_article_links']):
            if link and link.has_attr('href'):
                link_list.append(link)

        return set(link['href'] for link in link_list)

class ArticlePage(NewsPage):

    def __init__(Self, news_Site_uid, url):
        super().__init__(news_site_uid, url)

    @property
    def body(self):
        result = self._select(self.queries['article_body'])
        return result[0].text if len(result) else ''

    @property
    def title(self):
        result = self._select(self.queries['article_title'])
        return result[0].text if len(result) else ''
```

Modificaremos ahora nuestro archivo main
```
vim main.py
```
```python
import argparse
import logging
logging.basicConfig(level=logging.INFO)

import news_page_objects as news
from common import config

logger = logging.getLogger(__name__)

def _new_scraper(news_site_uid):
    host = config()['news_sites'][news_site_uid]['url']

    logging.info('Beginning scraper for {}'.format(host))
    homepage = news.HomePage(news_site_uid, host)

    for link in homepage,article_links:
        print(link)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    news_site_choices = list(config()['news_sites'].keys())
    parser.add_argument('news_site', 
                        help='The news site that you want to scrape', 
                        type=str, choices=news_site_choices)

    args = parsert.parse_args()
    _news_scraper(args.news_site)
```

## Pandas

[**PANDAS**](https://github.com/diegoufp/DataScience/blob/master/pandas.md#pandas "PANDAS")

## Introducción a los sistemas de datos

Los sistemas de datos vienen en muchos sabores y colores, SQL, NoSQL, especializados en procesamiento en bloque, chorro y streaming. Este tipo de sistema nos permite realizar queries sofisticadas y compartir nuestro trabajo con otros miembros del equipo.

- **Procesamiento de bloque**: Estamos hablando de datos históricos, qué sucedió ayer, en el trimestre pasado, cuáles fueron las ventas del año anterior o de los últimos cinco años. Nos permite realizar el procesamiento de manera eficiente.

- **Procesamiento en chorro**: Significa que estamos procesando los datos conforme van llegando, las transformaciones se realizan en tiempo real, Este tipo de sistema nos sirven para cuando queremos realizar decisiones en donde la importancia del tiempo es fundamental.

El criterio principal a tener en cuenta: El tiempo que tienes. Si bien los sistemas open source son gratis, para poderlos implementar necesitas tener conocimientos de cloud, debes poder saber trabajar y mantener máquinas.

**SQL vs NoSQL**

- La discusión más relevante en el mundo de las aplicaciones web y móvil, donde dependiendo de la aplicación, la decisión puede ser fundamental para el crecimiento de la app.
- La verdad es que para los profesionales de los datos, especialmente los profesionales de los datos. Es necesario saber ambos.

```
touch base.py
vim base.py
```
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///newspaper.db')

Session = sessionmaker(bind=engine)

Base = declarative_base()
```
---------------------------------------------------------
```
touch article.py
vim article.py
```
```python
from sqlalchemy import Column, String, Integer

from base import Base

class Article(Base):
    __tablename__ = 'articles'

    id = Column(String, primary_key=True)
    body = Column(String)
    host = Column(String)
    title = Column(String)
    newspaper_uid = Column(String)
    n_tokens_body = Column(Integer)
    n_tokens_title = Column(Integer)
    url = Column(String, unique=True)

    def __init__(self,
                uid,
                body,
                host,
                newspaper_uid,
                n_tokens_body,
                n_tokens_title,
                title,
                url
                ):
        self.id = uid
        self.body = body
        self.host = host
        self.newspaper_uid = newspaper_uid
        self.n_tokens_body = n_tokens_body
        self.n_tokens_title = n_tokens_title
        self.title = title
        self.url = url
```
-----------------------------------------------------
```
touch main.py
vim main.py
```
```python
import argparse
import logging
logging.basicConfig(level=logging.INFO)

import pandas as pd

from article import Article
from base import Base, engine, Session

logger = logging.getLogger(__name__)

def main(filename):
    Base.metadata.create_all(engine) #<- Genera nuestro esquema(como en sql)
    session = Session()
    articles = pd.read_csv(filename)
    # iterrows nos permite generar un loop adentro de cada una de nuestras filas de nuestro dataframe
    for index, row in articles.iterrows():
        logger.info('Loading article uid {} into DB'.format(row['uid']))
        article = Article(row['uid'],
                            row['body'],
                            row['host'],
                            row['newspaper_uid'],
                            row['n_tokens_body'],
                            row['n_tokens_title'],
                            row['title'],
                            row['url'])

        session.add(article) #<- Estro ya nos estaria poniendo nuestro articulo dentro de la base de datos

    session.commit()
    session.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The file you want to load into the db',
                        type=str)

    args = parser.parse_args()

    main(args.filename)
```