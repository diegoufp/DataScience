# Web Scraping


## Extracción de Datos en la Web

### Web Scraping
Proceso de extraccion de datos en la web.

- Objetivos:
Recopilar informacion almacenada en un servidor web.

### Web Crawling
Proceso de mapeo e indexacion de paginas web para conocer su contenido.

- Objertivos:
Conocer la estructura de la web. 

## Es legal scrapear un sitio?

Hay preguntas que nos tenemos que hacer a la hora de scrapear un sitio que nos van a ayudar a definir si lo que estamos haciendo esta bien o esta mal.

- Estoy violando alguna reglamentacion local?
- Estoy violando los "Terminos y Condiciones" del sitio?
- EStoy accediendo a lugares no autorizados?
- Es legal el uso que le voy a dar a los datos?

La corte de los estados unidos lo define como:
" Quienquiera que acceda a una computadora sin autorizacion o exceda la autorizacion otorgada y de este modo obtenga informacion protegida. "

### Robots.txt

Robots.txt es un archivo que lo tienen casi todas las paginas web, que realmente lo que hacen es definir buenas practicas de scraping con ese sitio en particulas.

Robots.txt no es vinculante, es decir, que no hay nada que nos prohiba violar lo que esta escrito en robots.txt

- **Crawl-delay**:
Es la demora que tenemos que setear en segundos entre cada solucitud que le hagamos al sitio.

## Descargando una página web

En este modulo veremos como utilizar las bibliotecas `requests` y `bs4` para programar scrapers de sitios HTML. Nos propondremos armar un scraper de noticias del diario [**Pagina12**](https://www.pagina12.com.ar/ "Pagina12").

Supongamos que queremos leer el diario por internet. Lo primero que hacemos es abrir el navegador, escribir la URL del diario y apretar Enter para que aparezca la pagina del diario. Lo que ocurre en el momento en el que apretamos Enter es lo siguiente:

1. El navegador envia una solicitud a la URL pidiendole informacion.
2. El servidor recibe la peticion y procesa la respuesta.
3. El servidor envia la espuesta a la IP de la cual recibio la solicitud.
4. Nuestro navegador recibe la espuesta y muestra **formateada** en pantalla.

Para hacer un scraper debemos hacer un programa que replique este flujo de forma automatica y sistematica para luego extraer la informacion deseada de la respuesta. Utilizaremos `requests` para realizar peticiones y recibir las espuestas y `bs4` para parsear la espuesta y extraer la informacion.

```python
import requests

# Guardamos la url en un string
url = 'https://www.pagina12.com.ar/'

# El metodo get hace la solucitud 
p12 = requests.get(url)

# Para saber si salio bien hay que mirar el atributo con status_code
# Si sale 200 significa que todo salio bien
p12.status_code

# Para ver el contenido
print(p12.text)

# Hay caso en los que el contenido que vamos a descargar no va a ser texto si no que puede ser una imagen, audio o video
# En ese caso es muy util acceder al atributo content
p12.content
# Va aparecer lo mismo pero al inicio se encuentra una b' que indica que esta imprimiendo como texto pero son byts

# Para ver el encabezado de la respuesta
# En este podemos ver datos como 'fecha', 'tipo de contendio', 'set de caracteres', 'informacion sobre el servidor', 'cookies', etc.
p12.headers

# Encabezado de cuando sale la solicitud
# en 'User-Agent' se puede ver que el servidor sabe que la solicitud proviene de una solicitud de python, esto se puede cambiar.
p12.request.headers

# Muestra que utilizamos un 'get' para hacer la solicitud
# Existen otros metodos aparte de get
p12.request.method

# Volver a consultar la url a la que hicimos la solicitud
# Esto es util a la hora de redireccionamientos
p12.request.url
```

## Parseando HTML con BeautifulSoup

Extraer de todo ese codigo HTML la informacion que para nosotros es importante.

```python
# Esto nos va a permitir parsear el codigo HTML
# Es decir que nos va a permitir tomar todo ese texto y poder indentificar distintas partes en las que va a estar la informacion de nuestro interes
from bs4 import BeautifulSoup

#beatifulsoup no pide que indiquemos un parser
# El parser es el pedazo de codigo que corre detras de esta funcion y separa el texto largo en partes mas cortas que sean ams faciles de indentificar y manejar
s = BeautifulSoup(p12.text, 'lxml')

# Si vemos el tipo podremos ver que es una BeautifulSoup
type(s)

# Te lo muestra mas ordenado que con 'print(p12.text)'
print(s.prettify())

# Obtener el tag o etiqueta
# En este caso estamos buscnado un el tag "ul class='hot-sections'"
# si solo lo buscamos por ul saldra el primero con ese tag y puede no ser el que buscamos
s.find('ul')

#podemos ser mas especificos agregandole atributos 'attrs'
s.find('ul', attrs={'class':'hot-sections'})

# Dentro de este nuevo tag lo que debemos obtener son todos los nombres de las secciones
# como esta vez queremos buscar varios tags usamos '.find_all'
#Esto nos dara una lista
secciones = s.find('ul', attrs={'class':'hot-sections'}).find_all('li')
secciones
```

## Extrayendo informacion

```python
# Para demostrar como funciona nos quedaremos solo con el primer elemento
seccion = secciones[0]
seccion

# Una manera equivalente de usar el metodo '.find' es:
seccion.find('a')
# Otra manera que tiene bs4 de acceder al primer tag hijo
seccion.a
#En los dos el resultado es el mismo : <a href="https://www.pagina12.com.ar/secciones/el-pais">El país</a>

# Con cualquiera de estos dos podemos obtener en forma de staring el texto del atributo href
seccion.find('a').get('href')
seccion.a.get('href')
# El resultado de cualquiera de los dos es este: 'https://www.pagina12.com.ar/secciones/el-pais'

# Para obtener el texto del tag a : >El país</a>
seccion.a.get_text()
# El resultado es este: 'El país'

# Este proceso lo replicaremos para todas la paginas
links_secciones = [seccion.a.get('href') for seccion in secciones]
links_secciones

# Ahora con estos links podemos hacer un nuevo requests.get
sec = requests.get(links_secciones[0])

# 200 nos indica que todo salio bien
sec.status_code

# A esto se le llama ahcer una sopa
s_seccion = BeautifulSoup(sec.text, 'lxml')
print(s_seccion.prettify())

featureds_article = s_seccion.find('div', attrs={'class':'featured-article__container'})
featureds_article

# Link del articulo promocionado
primotion = featureds_article.a.get('href')

article_list = s_seccion.find('ul', attrs={'class':'article-list'})

# Funcion para encontrar los otros links
def links_the_article(article_lists):
    
    count = len(article_lists)
    i = 0
    list_articles = []
    while i < count:
        article_list = article_lists[i]
        if len(article_list) != 0:
            link_article = article_list.a.get('href')
            list_articles.append(link_article)
            i += 1
        else:
            i += 1
    return list_articles

list_articles = links_the_article(article_lists)
#Lista con todos los links menos el promocionado
list_articles.append(promotion)
#Lista con todos los links junto con el promocionado
list_articles
```

## Manejo de errores

Funcion que recibe un objeto de BeautifulSoup de una pagina de una seccion y devuelve una lista de URLs a las notas de esa seccion.

```python
def obtener_notas(soup):
    lista_nota = []

    # Obtengo el articulo promocionado
    # En este caso usamos find en lugar de get
    # si find no encuentra lo que estamos buscando retorna un None y no produce ningun error
    featured_article = soup.find('div', attrs={'class':'featured-article__container'})
    if featured_article:
        lista_nota.append(featured_article.a.get('href'))

    # Obtengo el listado de articulos
    article_list = soup.find('ul', attrs={'class':'article-list'})
    for article in article_list.find_all('li'):
        if article.a:
            lista_nota.append(article.a.get('href'))
    
    return lista_nota
```
- **Manejo de errores**
```python
# Cuando hacemos los request
r = requests.get(url)
# Una cosa que podemos verificar simplemente es status code
r.status_code
# 200 significa que salio todo bien
# Una forma muy simple de verificar si estamos listos para parsear el contenido de la respuesta es siemplemente verificar si el status es 200

if r.status_code == 200:
    # Procesamos la respuesta
else:
    # informamos el error
```

Para notros obtener un status code distinto de 200 tiene que haber un servidor web que haya recibido nuestra solicitud, la haya procesado, haya encontrado algun error en ese procesamiento entonces nos devuelve el codigo de error.

Puede pasar que en funciones como la que hicimos anteriormente nos encontremos con algun link que conduzca a una pagina que este caida o siemplemente que el servidos estaba fuera de servicio en ese momento entonces no podemos procesar la respuesta.

En este caso cuando hagamos un request a una url mala va a arrojar un error.

```python
url_mala = 'https://www.pagina13.com.ar/'
requests.get(url_mala)
```
- **Que es lo que podemos hacer?**

```python
# Lo podemos encapzular dentro de un bloque try , except
try:
    requests.get(url_mala)
# Podemos guardar la excepcion e imprimirla para saber que typo de error fue
except Exception as e :
    print('error en la request')
    print(e)
    print('\n')
# y asi no interrumpe la ejecucion de condigo
```

## Descargando contenido

En este tema vamos a descargar el contenido de cada nota(titulo, texto, volanta, fecha, autor, etc.)

```python
url_nota = 'https://www.pagina12.com.ar/281448-causa-peajes-procesaron-al-ex-ministro-nicolas-dujovne'

try:
    nota = requests.get(url_nota)
    if nota.status_code == 200:
        s_nota = BeautifulSoup(nota.text, 'lxml')
        # Extraer el titulo
        titulo = s_nota.find('h1', attrs={'class':'article-title'})
        print(titulo.text)
        # Extraer la fecha del articulo
        fecha = s_nota.find('span', attrs={'pubdate':'pubdate'}).get('datetime')
        print(fecha)
        # Extraer el cuerpo
        cuerpo = s_nota.find('div', attrs={'article-text'})
        print(cuerpo.text)
        # Extraer la volanta 
        volanta = s_nota.find('h2', attrs={'class':'article-prefix'})
        print(volanta.text)
        # Extraer el copete
        copete = s_nota.find('div', attrs={'class':'article-summary'})
        print(copete.text)
        # Extraer autor
        autor = s_nota.find('div', attrs={'class':'article-author'}).a
        print(autor.text)
except Exception as e:
    print('Error:')
    print(e)
    print('\n')
```

## Contenido multimedia
 
Para descargar contenido multimedia
```python
media = s_nota.find('div', attrs={'class':'article-main-media-image'}).find_all('img')

if len(media) == 0:
    print('no se encontraron imagenes')
else:
    imagen = media[-1]
    img_src = imagen.get('data-src')
    print(img_src)

img_req = requests.get(img_src)
img_req.status_code

#Para poder visualizar la imagen:
from IPython.display import Image
Image(img_req.content)
 ```