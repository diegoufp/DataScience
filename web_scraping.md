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

Para hacer un scraper debemos hacer un programa que replique este flujo de forma automatica y sistematica para luego extraer la informacion deseada de la respuesta. Utilizaremos `requests` para realizar peticiones y recibir las respuestas y `bs4` para parsear la respuesta y extraer la informacion.

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

## Unificado el scraper

- Intento:
```python
import requests
from bs4 import BeautifulSoup

def extractor(link):

    try:
        nota = requests.get(link)
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
            # Extraer imagen
            media = s_nota.find('div', attrs={'class':'article-main-media-image'}).find_all('img')

            if len(media) == 0:
                print('no se encontraron imagenes')
            else:
                imagen = media[-1]
                img_src = imagen.get('data-src')
                print(img_src)
    except Exception as e:
        print('Error:')
        print(e)
        print('\n')
```

- Verdadero:

```python
import requests
from bs4 import BeautifulSoup

def obtener_info(s_nota):

    #Creamos un diccionario vacio para poblarlo con la informacion
    ret_dict = {}

    # Extraemos la fecha
    fecha = s_nota.find('span', attrs={'pubdate':'pubdate'})
    if fecha:
        ret_dict['fecha'] = fecha.get('datetime')
    else:
        ret_dict['fecha'] = None

    # Extraemos el titulo
    titulo = s_nota.find('h1', attrs={'class':'article-title'})
    if titulo:
        ret_dict['titulo'] = titulo.text
    else:
        ret_dict['titulo'] = None

    # Extraemos la volanta
    volanta = s_nota.find('h2', attrs={'class':'article-prefix'})
    if volanta:
        ret_dict['volanta'] = volanta.get_text()
    else:
        ret_dict['volanta'] = None

    # Extraemos el copete 
    copete = s_nota.find('div', attrs={'class':'article-summary'})
    if copete:
        ret_dict['copete'] = copete.get_text()
    else:
        ret_dict['copete'] = None

    # Extraemos el autor
    autor = s_nota.find('div', attrs={'class':'article-author'})
    if autor:
        ret_dict['autor'] = autor.a.get_text()
    else:
        ret_dict['autor'] = None

    # Extraemos la imagen
    media = s_nota.find('div', attrs={'class':'article-main-media-image'})
    if media:
        imagenes = media.find_all('img')
        if len(imagenes) == 0:
            print('no se encontraron imagenes')
        else:
            imagen = imagen[-1]
            img_src = imagen.get('data-src')
            try:
                img_req = requests.get(img_src)
                if img_req.status_code == 200:
                    ret_dict['imagen'] = img_req.content
                else:
                    ret_dict['imagen'] = None
            except:
                print('No se pudo obtener la imagem')

    else:
        print('No se encontro media')

    # Extraemos el cuerpo de la nota
    cuerpo = s_nota.find('div', attrs={'article-text'})
    if cuerpo:
        ret_dict['texto'] = cuerpo.get_text()
    else:
        ret_dict['texto'] = None

    return ret_dict
```
```python
def scrape_nota(url):
    try:
        nota = requests.get(url)
    except Exception as e:
        print('Error scrapeando URL', url)
        print(e)
        return None

    if nota.status_Code != 200:
        print(f'Error obteniendo nota {url}')
        print(f'stuts Code = {nota.status_code}')
        return None

    s_nota = BeautifulSoup(nota.text, 'lxml')

    ret_dict = obtener_info(s_nota)
    ret_dict['url'] = url

    return ret_dict
```
```python
    notas = []
    for link in links_secciones:
        try:
            r = requests.get(link)
            if r.status_code == 200:
                soup = Beaurifulsoup(r.text, 'lxml')
                notas.extend(obtener_notas(soup))
            else:
                print('No se pudo obtener la seccion: ', link)
        except:
            print('No se pudo obtener la seccion: ', link )
```
```python
data = []
for i, nota in enumerate(notas)
    print(f'Scrapeando nota{i}/{len(notas)}')
    data.append(scrape_nota(nota))
```

Despues de ejecutar el codigo vamos a crear un DataFrame
```python
import pandas as pd

df = pd.DataFrame(data)
df.head()
```

Lo ultimo seria guardar el DataFrame en un archivo
```python
df.to_csv('Notas_Pagina12.csv')
```

## Sitios dinamicos y Selenium

## LATAM Airlines

Vamos a scrapear el sitio de Latam para averiguar datos de vuelos en funcion el origen y destino, fecha y cabina. La informacion que esperamos obtener de cada vuelo es:

- Precio(s) disponibles
- Horas de salida y llegada (duracion)
- Informacion de las escalas

```python
import requests
from bs4 import BeautifulSoup

url ='https://www.edestinos.com.mx/flights/select/roundtrip/ap/mex/ap/cun?departureDate=2020-08-28&returnDate=2020-09-30&pa=1&py=0&pc=0&pi=0&sc=economy'

r = requests.get(url)

r.status_code

s = BeautifulSoup(r.text, 'lxml')

print(s.prettify()) # Imprimir mas lindo el HTML

# Python no sabe como procesar JS, asi que esta estrategia de descargar el HTML no va a funcionar.
# Es por ello que usaremos Selenium
```

### Selenium

Selenium es una herramienta que nos permitira controlar un navegador y podremos utilizar las funcionalidades del motor de JavaScript para cargar el contenido que no viene en el HTML de la pagina. Para esto necesitamos el modulo webdriver.

```python
from selenium import webdriver
```
#### Instanciar un diver del navegador

```python
# instanciar un dirver
driver = webdriver.Chrome(executable_path='./selenium/chromedriver')
# Al instanciar el driver se abre una pesta;a de chrom que nosotros lo vamos a poder ir controlando desde el codigo

url ='https://www.edestinos.com.mx/flights/select/roundtrip/ap/mex/ap/cun?departureDate=2020-08-28&returnDate=2020-09-30&pa=1&py=0&pc=0&pi=0&sc=economy'
```

#### Hacer que el navegador carge la pagina web.

```python
driver.get(url)
```

#### Cerrar el navegador

```python
driver.close()
```

#### Abrir navegador en modo incognito

```python
options = webdriver.ChromeOptions()
options.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='./selenium/chromedriver', options=options)
```

## Seleccion de elementos con selenium

En este tema veremos como seleccionar los elementos que estan en este navegador automatizado que generamos utilizando selenium.

para hacer eso vamos a utilizar algo que se llama xpath(la ruta xml), que nos va a permitir identificar donde se encuentran cada uno de los elementos que necesitamops extraer atavez de los tags y sus atributos.

A diferencia de como se hacia en BeautifulSoup, que lo que haciamos era buscar directamente el nombre del tag y filtrar por algun atributo, aqui lo que vamos a hacer directamente es generar una ruta que apunte a ese elemento en particular y en esa ruta va a estar toda la informacion necesaria para identificar ese elemento, armando un unico xpath.

En la pagina que vamos a utilizar presionamos `F12` (inspeccionar elementos).
Estas paginas reconocen cual es la resolucion del navegador que estamos utilizando y acomodan el contenido en funcion de esto.
La recomendacion es **separar** el inspecto de elementos para que la navegacion tenga el mismo tama;o que uno esperaria normalmente

### Extraer la informacion de la pagina

```python
from selenium import webdriver 
driver = webdriver.Chrome(executable_path='./selenium/chromedriver')
url ='https://www.edestinos.com.mx/flights/select/roundtrip/ap/mex/ap/cun?departureDate=2020-08-28&returnDate=2020-09-30&pa=1&py=0&pc=0&pi=0&sc=economy'
driver.get(url)

# Hay find_element y find_elements en este caso usaremos el plural ya que queremos seleccionar varios a la vez
# con la doble barra '//' en el xpath significa que tiene que buscar elementos en todo el arbol independientemente si son hijos directos o hijos de sus hijos
vuelos = driver.find_elements_by_xpath('//li[@class="ng-star-inserted"]')

vuelo = vuelos[5]

vuelo
# <selenium.webdriver.remote.webelement.WebElement (session="20271800ded395bee0774c025840bc39", element="d575aa92-d7ab-4fdf-aaa7-f7bd0ecd26cf")>

# con el punto '.' en el xpath lo que indicamos es que tenemos que buscar de esta rama en aprticular hacia abajo, si no ponemos el punto va a buscar en todo el arbol de l apgina web
# con una sola barra '/' en el xpath indicamos que es un hijo directo
vuelo.find_element_by_xpath('.//div[@class="leg-info"]/span[1]').text
```

### Interactuando con los elementos con selenium

obtendremos el numero de escalas haciando click en los detalles del vuelo.

```python
boton_escalas = vuelo.find_element_by_xpath('.//div[@class="leg-info"]//a[1]')
boton_escalas.click()

segmentos = vuelo.find_elements_by_xpath('.//div[@class="content"]/leg-details/segment')
escalas = len(segmentos) - 1
escalas
```

## Scrapeando escalas y tarifas

```python
from selenium import webdriver 
driver = webdriver.Chrome(executable_path='./selenium/chromedriver')
url ='https://www.edestinos.com.mx/flights/select/roundtrip/ap/mex/mp/tyo?departureDate=2020-08-28&returnDate=2020-09-30&pa=1&py=0&pc=0&pi=0&sc=economy'
driver.get(url)

# Hay find_element y find_elements en este caso usaremos el plural ya que queremos seleccionar varios a la vez
# con la doble barra '//' en el xpath significa que tiene que buscar elementos en todo el arbol independientemente si son hijos directos o hijos de sus hijos
vuelos = driver.find_elements_by_xpath('//li[@class="ng-star-inserted"]')

vuelo = vuelos[5]

vuelo
# <selenium.webdriver.remote.webelement.WebElement (session="20271800ded395bee0774c025840bc39", element="d575aa92-d7ab-4fdf-aaa7-f7bd0ecd26cf")>

# con el punto '.' en el xpath lo que indicamos es que tenemos que buscar de esta rama en aprticular hacia abajo, si no ponemos el punto va a buscar en todo el arbol de l apgina web
# con una sola barra '/' en el xpath indicamos que es un hijo directo
vuelo.find_element_by_xpath('.//div[@class="leg-info"]/span[1]').text

boton_escalas = vuelo.find_element_by_xpath('.//div[@class="leg-info"]//a[1]')
boton_escalas.click()

segmentos = vuelo.find_elements_by_xpath('.//div[@class="content"]/leg-details/segment')
escalas = len(segmentos) - 1
escalas

# scrapeando escalas y tarifas


segmento = segmentos[0]
segmento

inicial = segmento.find_element_by_xpath('.//p[@class="airport"]/span[@class="airport-name"]/span[@class="airport-title"]').text

inicial_salida = segmento.find_element_by_xpath('.//p[@class="airport"]/span[@class="time"]/span[2]').text

llegada_escala = segmento.find_element_by_xpath('./div[@class="segment"]/p[@class="airport"]/span[@class="airport-name"]')
llegada_escala.text

hora_llegada_escala = segmento.find_element_by_xpath('./div[@class="segment"]/p[@class="airport"]/span[@class="time"]')
hora_llegada_escala.text

segmento = segmentos[1]
segmento

salida_escala = segmento.find_element_by_xpath('.//p[@class="airport"]/span[@class="airport-name"]/span[@class="airport-title"]')
salida_escala.text

hora_salida_escala = segmento.find_element_by_xpath('.//p[@class="airport"]/span[@class="time"]/span[2]')
hora_salida_escala.text

destino_final = segmento.find_element_by_xpath('./div[@class="segment"]/p[@class="airport"]/span[@class="airport-name"]')
destino_final.text

hora_destino_final = segmento.find_element_by_xpath('./div[@class="segment"]/p[@class="airport"]/span[@class="time"]')
hora_destino_final.text

# Cerrar el modal 
driver.find_element_by_xpath('//div[@class="custom-dialog"]/div[1]').click()

# Elegir el vuelo(ver tarifas)
elegir = vuelo.find_element_by_xpath('.//span[@class="transaction-text"]')
elegir.click()

# con contains() se puede agregar una palabra que sea contante en multiples direcciones xpath
tarifas = driver.find_elements_by_xpath('//div[@class="insurance-options"]/div[contains(@class, "insurance-")]')

tarifas # del 0 al 3 son las tarifas

tarifa_1 = tarifas[0]
tarifa_2 = tarifas[1]
tarifa_3 = tarifas[2]
tarifa_4 = tarifas[3]

precio_1 = tarifa_1.find_element_by_xpath('./div[contains(@class, "wrapper")]/div[@class="details"]//span[@class="price "]')
precio_1.text

precio_2 = tarifa_2.find_element_by_xpath('./div[contains(@class, "wrapper")]/div[@class="details"]//span[@class="price "]')
precio_2.text

precio_3 = tarifa_3.find_element_by_xpath('./div[contains(@class, "wrapper")]/div[@class="details"]//span[@class="price "]')
precio_3.text
```

## Construyendo funciones

```python
def obtener_precios(vuelo):
    '''
    Funcion que retorna una lista de diccionarios con las distintas tarifas
    '''
    tarifas = driver.find_elements_by_xpath('//div[@class="insurance-options"]/div[contains(@class, "insurance-")]')
    tarifas = tarifas[0:3]
    precios = []
    for tarifa in tarifas:
        nombre = tarifa.find_element_by_xpath('./div[contains(@class, "wrapper")]/div[@class="content"]/div[@class="description"]/span[@class="unchecked"]').text
        valor = tarifa.find_element_by_xpath('./div[contains(@class, "wrapper")]/div[@class="details"]//span[@class="price "]').text
        dict_tarifa = {nombre:valor}
        precios.append(dict_tarifa)
        print(dict_tarifa)
    return precios
```

```python
def obtener_datos_escalas(vuelo):
    '''
    Funcion que retorna una lista de diccionarios con la informacion de las escalas de cada vuelo
    '''
    segmentos = vuelo.find_elements_by_xpath('.//div[@class="content"]/leg-details/segment')
    info_escalas = []
    for segmento in segmentos:
        # Origen
        origen = segmento.find_element_by_xpath('.//p[@class="airport"]/span[@class="airport-name"]/span[@class="airport-title"]').text
        # Hora de salida
        dep_time = segmento.find_element_by_xpath('.//p[@class="airport"]/span[@class="time"]/span[2]').text
        # Destino
        destino = segmento.find_element_by_xpath('./div[@class="segment"]/p[@class="airport"]/span[@class="airport-name"]').text
        # Hora de llegada
        arr_time = segmento.find_element_by_xpath('.//p[@class="airport"]/span[@class="time"]/span[2]').text
        # Duracion total del vuelo
        duracion_vuelo = vuelo.find_element_by_xpath('.//div[@class="content"]/leg-details/leg-details/div[@class="connections-wrapper"]/div[@class="connection-attributes"]/div[1]/div[2]/span[1]').text
        # Numero del vuelo
        numero_vuelo = segmento.find_element_by_xpath('.//div[@class="flight-info"]/strong[@class="flight-number"]').text
        # Modelo del avion
        modelo_avion = segmento.find_element_by_xpath('.//div[@class="info-header"]//span[@class="name"]').text
        # Duracion de la escala
        duracion_escala = segmento.find_element_by_xpath('.//div[@class="info-header"]//span[@class="time"]').text
        data_dict = {
            'origen': origen,
            'dep_time': dep_time,
            'destino': destino,
            'arr_time': arr_time,
            'numero del vuelo': numero_vuelo,
            'modelo del avion': modelo_avion,
            'duracion de cada escala': duracion_escala,
            'duracion total del viaje': duracion_vuelo
        }
        info_escalas.append(data_dict)
    return info_escalas
```

## Demoras dinamicas

Se le tiene que dar tiempo al navegador para pargar toda la informacion.

Veremos como introducir peque;as demoras que el den tiempo al navegador a cargar la informacion.

La forma mas facil de poner demoras es:
```python
# Esta funcion introduce una demora estatica, es decir, para cada pagina que cargemos vamos a esperar 10 segundos(algunas veces no son suficientes o necesarios)
# Introducir una demora
import time
time.sleep(10) 
# Se hara un demora de 10 segundos antes de empezar a obtener la informacion con nuestra funcion
```

Selenium nos da algunas herramientas para generar demoras dinamicas que son un poco mas inteligentes que esperan antes de seguir avanzando con el resto del codigo.
```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# Este delay es un maximo de timepo, si se umple la condicion (until) se inicia antes.
delay = 10
# Introducir demora inteligente
try:
    vuelo = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, '//li[@class="flight])))
    print('La pagina termino de cargar')
except TimeoutException
    print('La pagina tardo demasiado en cargar')
driver.close()
```

## Introduccion a APIs

En este módulo utilizaremos APIs para obtener información sobre artistas, discos y tracks disponibles en Spotify.

Es muy importante siempre leer la documentacion de las APIs que se vayan a usar.

### ¿Qué es una API?

Por sus siglas en inglés, una API es una interfaz para programar aplicaciones (Application Programming Interface). Es decir que es un conjunto de funciones, métodos, reglas y definiciones que nos permitirán desarrollar aplicaciones (en este caso un scraper) que se comuniquen con los servidores de Spotify. Las APIs son diseñadas y desarrolladas por las empresas que tienen interés en que se desarrollen aplicaciones (públicas o privadas) que utilicen sus servicios. Spotify tiene APIs públicas y bien documentadas que estaremos usando en el desarrollo de este proyecto.

### REST

Un término que seguramente te vas a encontrar cuando estés buscando información en internet es REST o RESTful. Significa representational state transfer y si una API es **REST** o RESTful, implica que respeta unos determinados principios de arquitectura, como por ejemplo un protocolo de comunicación cliente/servidor (que será HTTP) y (entre otras cosas) un conjunto de operaciones definidas que conocemos como métodos. Ya veníamos usando el **método** GET para hacer solicitudes a servidores web.

### Documentación

Como mencioné antes, las APIs son diseñadas por las mismas empresas que tienen interés en que se desarrollen aplicaciones (públicas o privadas) que consuman sus servicios o información. Es por eso que la forma de utilizar las APIs variará dependiendo del servicio que querramos consumir. No es lo mismo utilizar las APIs de Spotify que las APIs de Twitter. Por esta razón es de suma importancia leer la documentación disponible, generalmente en la sección de desarrolladores de cada sitio. Te dejo el [link a la de Spotify](https://developer.spotify.com/documentation/ "link a la de Spotify").

### JSON

Json significa JavaScript Object Notation y es un formato para describir objetos que ganó tanta popularidad en su uso que ahora se lo considera independiente del lenguaje. De hecho, lo utilizaremos en este proyecto por más que estemos trabajando en Python, porque es la forma en la que obtendremos las respuestas a las solicitudes que realicemos utilizando las APIs. Para nosotros, no será ni más ni menos que un diccionario con algunas particularidades que iremos viendo a lo largo del curso.

## Utilizando APIs

[Artists de spotify](https://developer.spotify.com/documentation/web-api/reference/artists/ "Artists de spotify")

### Construir una URL

Para empezar veamos que hay una `Base URL` que es la base de todas las URL que vamos a tener que usar para usar estas APIs.

Luego tenemos distindos `endpoints` en funcion de lo que querramos obtener, en este caso, como lo que nosotros queremos obtener es un artista vamos a estar trabajando con el primer endpoints (`/v1/artists/{id} `).

Un **endpoints** es un lugar de llegada (hacia donde queremos ir), dependiendo al lugar de llegada al que le hagamos la solicitud vamos a tener distintos timpos de informacion y por lo tanto la solicitud la vamos a tener que hacer de manera distinta.

- Primer paso:
Copiar la URL base y el endpoint

```python
url_base = 'https://api.spotify.com/v1'
# Como en el url base finaliza con 'v1' entonces en el endpoint no lo vamos a agregar
ep_artist = '/artists/{artist_id}'
```
- Paso 2:
Buscar el id del artista
```python
id_im = '6mdiAmATAx73kdxrNrnlao'
```

- Paso 3:
Constuir la url completa
```python
url_base+ep_artist.format(aritst_id = id_im)
```

- Paso 3:
Hacer la solicirud al servidor de spotify por medio de la url
```python
import requests

r = requests.get(url_base+ep_artist.format(aritst_id = id_im))
```

- Paso 4:
Revistar el status_code
```python
r.status_code
# Si sale 401 quiere decir que no estamos autorizados a acceder a ese recurso
```

- Paso 5:
Acceder a Json
Ya no estas trabajando con una pagina HTML asi que lo que nos entrego en un archivo Json
```python
r.json()
# si te salio 401 te saldra con error y te dira que no tenemos un token
```

### Tokens

Tuvimos un error de autorizacion al tratar de acceder a las APIs de spotify.
Esto es por que spotify necesita y nos pide que registremos una aplicacion para poder utilizar sus APIs.

Para resolver eso tenermos que ir a este [link](https://developer.spotify.com/dashboard/ "link") que nos mandara a la pgina para registar una aplicacion en spotify.

Tendremos que tener una cuenta y crear una aplicacion en el mismo enlace.

Vamos a tener un `Client ID` y un `Client Secret`.

Si volvemos a la documentacion de las [APIs de spotify](https://developer.spotify.com/documentation/web-api/reference/artists/ "APIs de spotify") y clickeamos sobre el endpoint `/v1/artists/{id}` nos va a decir que tenemos que agregarle el un *header* a la solicitud que es requerido y que necitamos un token de acceso que sea valido.

[Link Autorization Guide](https://developer.spotify.com/documentation/general/guides/authorization-guide/ "Link Autorization Guide")

En este caso vamos a tener que utilizar una autorizacion bastante simple y simplemente nos provee un access token para que podamos usarlo.

Vamos a tener que acceder a un token url
```python
token_url = 'https://accounts.spotify.com/api/token'
```
Luego nos pide que creemos unos parametros, que esos paramentros se los vamoa tener que pasar a la riquests en el momento en que la ejecutemos.
```python
params = {'grant_type':'client_credentials'}
```
Aparte de estos parametros vamos a tenr que ponerle un encabezado y ese encabezado va a ser otro diccionario donde vamos a poner `Authorization` y `Basic`.
Despues de eso pasarle nuestro `Client ID` y nuestro `Client Secret` codificados en `Bases64`, en este [link](https://www.base64encode.org/ "link") se puede hacer. Tiene que tener la siguiente estructura:
`Client ID`:`Client Secret` y despues todo junto lo tenemos que convertir a formato Base64.

```python
# Es Basic espacio y el string codificado
headers = {'Authorization': 'Basic NTUxNDMzN2ZlZWY4NGY4N2FjYjYxOGE5NjVmMzg3MGI6ZjU4YTZlMzg4MzA5NGNhMThkNDljMjFjMWY0N2U2MjM='}
```
#### Sacar el token
Ya despues haremos un requests pero con un post en lugar del get
```python
r = requests.post(token_url, data=params, headers=headers)
```

Despues de generar esta solicitud deberiamos tener un status_code de 200(osea que se ejecuto correctamente)
```
r.status_code
```

Si checamos ej Json podemos ver el token, el tipo de token y cuanto dura el token (los tokens tiene un vencimiento)
Para acceder al token podemos simplemente usar:
```python
token = r.json()['access_token']
```

Despues haremos creamos un nuevo encabezado y hacemos la solicitud con get
```python
header = {'Authorization': 'Bearer {}'.format(token)}
r = requests.get(url_base+ep_artist+id_im, headers=header)
```

y revisar si el status_code es igual a 200
```
r.status_code
```
y ver la infomacion en el Json
```
r.json()
```

### Busquedas

En esta pagina puedes encontrar el endpoint para hacer busquedas. [Link](https://developer.spotify.com/documentation/web-api/reference/search/search/ "Link")

Este endpoind de busquedas nos va a permitir hacer alguna query a la base de datos de spotify con algun string (en esta caso de iron maiden), para poder obtener el id de ese artista sin la necesidad de tener que cargar la url a mano.

```python
url_busqueda = 'https://api.spotify.com/v1/search'
```

La estructura es la siguiente:

```python
# De tercer parametro (market) es opcional
# Spotify dependiendo de en que lugar estamos haciando la solicitud o donde estemos usando la aplicacion vamos s tener resusltado diferentes por cuestiones de derechos.
search_params = {'q':"Iron+Maiden", 'type':'artist', 'market':'MX'}
```

Despues hacemos la solicitud
```python
busqueda = requests.get(url_busqueda, headers=header, params=search_params)
```
```
busqueda.status_code
```
```
busqueda.json()
```

Vamos a tener varias bandas que se llamen iron maiden.
Es por ello que crearemos un DataFrame.

```python
import pandas as pd
df = pd.DataFrame(busqueda.json()['artists']['items'])
df.head()
```

Como sabemos que la banda original tendra mas popularidad que las otras, lo que haremos es ordenar el dataframe por la popularidad y nos quedaremos solo con el primer resultado.

```python
df.sort_values(by='popularity', ascending=False).iloc[0]
```

Si queremos quedarnos solo con el id filtramos la columna id
```python
df.sort_values(by='popularity', ascending=False).iloc[0]['id']
```

### Obteniendo discografia

Para codificar a base64 en python usamos una libreria base64
```python
import base64
import requests

def get_token(client_id, client_secret):
    encoded = base64.b64encode(bytes(client_id+':'+client_secret, 'utf-8'))
    params = {'grant_type':'client_credentials'}
    header = {'Authorization':'Basic '+ str(encoded, 'utf-8')}
    r= requests.post('https://accounts.spotify.com/api/token', headers=header, data=params)
    if r.status_code != 200:
        print('Error en la request.', r.json())
        return None
    else:
        print('Token valido por {} segundos'.format(r.json()['expires_in']))
        return r.json()['access_token']
```

Guardamos los client_id y client_secret para usar la funcion.

```python
client_id = '5514337feef84f87acb618a965f3870b'
client_secret = 'f58a6e3883094ca18d49c21c1f47e623'

```

Y lo probamos
```python
token = get_token(client_id, client_secret)
```

Esto lo vamos a usar para generar un nuevo header

```python
header = {'Authorization': 'Bearer {}'.format(token)}
```

Con este y con id de airon maiden vamos a obtener los albumes
```python
id_im = '6mdiAmATAx73kdxrNrnlao'
url_base = 'https://api.spotify.com/v1'
params = {'country':'MX'}
```

Buscaremos los endpoints de [albums](https://developer.spotify.com/documentation/web-api/reference/albums/ "albums")

En la informacion dice que es necesario el id del album.

Apara esto volveremos al endpoint de [artists] el cual dice como obtenerlos.`/v1/artists/{id}/albums`

```python
ep_albums = 'artists/{}/albums'
```

y se tiene que contruir la url apartir de esto
```python
albums_im = requests.get(url+ep_albums.format(im_id), headers=header, params)
```
```python
albums_im.status_code
albums_im.json()['items']
```

### Obteniendo los albums


```python
albumes = albums_im.json()['items']
lista_albums = [(album['id'], album['name']) for album in albums_im.json()['items']]


def extract_id_albums(albums):
    albums_im_id = []
    for album in albums:
        albums_im_id.append(album['id'])
    return albums_im_id

albums_im_id = extract_id_albums(albumes)

get_album = requests.get('https://api.spotify.com/v1/albums/{album_id}'.format(album_id=albums_im_id[0]), headers=header, params=params)

get_album.status_code

get_album.json()
```
### Obteniendo los albums con tracks

```python
album_ep = '/albums/{album_id}/tracks'
album_params = {'market':'MX'}
bnw_id = '1hDF0QPIHVTnSJtxyQVguB'

bnw = requests.get('https://api.spotify.com/v1/albums/{album_id}/tracks'.format(album_id=bnw_id), headers=header, params=album_params)

bnw.json()['items']

tracks = [(track['id'], track['name']) for track in bnw.json()['items']]
```

### Funcion para obtener la discografia completa


Si ejecutamos:
```
albums_im.json()
```
y vamos hasta abajo nos muestra cierta informacion
```
'limit': 20,
'next': 'https://api.spotify.com/v1/artists/6mdiAmATAx73kdxrNrnlao/albums?offset=20&limit=20&include_groups=album,single,compilation,appears_on&market=MX',
'offset': 0,
'previous': None,
'total': 44}
```

En esta informacion dice que trajo un `limit` de 20 desde el inicio, pero en `total` aparecen 44, eso quiere decir que faltan mas albumes que no estamos viendo en esta respuesta.

Crearemos una funcion para obtener la discografia completa

```python
def obtener_discografia(artist_id, token, return_name = False, page_limit = 50, country = None):
    url = 'https://api.spotify.com/v1/artists/{artist_id}/albums'
    header = {'authorization': f'Bearer {token}'}
    params = {'limit': page_limit, 'offset': 0, 'country': country}
    lista = []
    r = requests.get(url.format(artist_id=artist_id), params=params, headers=header)

    if r.status_code != 200:
        print('Error en la request.', r.json())
        return None
    
    if return_name:
        lista += [(item['id'], item['name']) for item in r.json()['items']]
    else:
        lista += [(item['id']) for item in r.json()['items']]

    while r.json()['next']:
        r = requests.get(r.json()['next'], headers=header)
        if r.status_code != 200:
            print('Error en la request.', r.json())
            return None

        if return_name:
            lista += [(item['id'], item['name']) for item in r.json()['items']]
        else:
            lista += [(item['id']) for item in r.json()['items']]

    return lista
``` 

obtener el track de cada album

```python
def obtener_canciones(album_id, token, return_name = False, page_limit=50, market= None):
    url = 'https://api.spotify.com/v1/albums/{album_id}/tracks'
    header = {'authorization': f'Bearer {token}'}
    params = {'limit': page_limit, 'offset': 0, 'market': market}
    lista = []

    r = requests.get(url.format(album_id=album_id), headers=header, params=params)

    if r.status_code != 200:
        print('Error en la request.', r.json())
        return None

    if return_name:
        lista += [(item['id'], item['name']) for item in r.json()['items']]
    else:
        lista += [(item['id']) for item in r.json()['items']]

    while r.json()['next']:
        r = requests.get(r.json()['next'], headers=header)
        if r.status_code != 200:
            print('Error en la request.', r.json())
            return None

        if return_name:
            lista += [(item['id'], item['name']) for item in r.json()['items']]
        else:
            lista += [(item['id']) for item in r.json()['items']]

    return lista
```

### Utilizando las dos funciones

```python
for album in obtener_discografia(id_im, token, return_name=True, country='MX'):
    print(album[1])
    for track in obtener_tracks(album[0], token, return_name=True, market='MX'):
        print('\t', track[1])
```

### Escuchar la cancion

```python
import IPython.display as ipd

preview_url = 'https://p.scdn.co/mp3-preview/69c63a844f61f0073d8c37052cef53ce028e151d?cid=5514337feef84f87acb618a965f3870b'

preview = requests.get(preview_url)

ipd.Audio(preview.content)
```

## [Scrapy](https://docs.scrapy.org/en/latest/ "Documentacion de scrapy")

Scrapy es un framework de scraping y crawling de código abierto, escrito en Python. Con este framework nos permite generar requests en paralelo, podemos trabajar con xpath, limitar la cantidad de requests, setear demoras, limitar los dominios.

En las ocaciones en que no encuentre la informacion no generara error ya que al encontrar un error sigue con las siguientes paginas, no se trava sin que nosotros tengamos que decirle explicitamente como es que queremos que procese los errores.

- Intalar Scrapy

```python
pip3 install scrapy
conda install -c conda-forge scrapy
```

- clase para scrapear

```python
import scrapy
# Esta biblioteca permite hacer webcrolling de manera recursiva
from scrapy.crawler import CrawlerProcess

# scrapy nos pide que trabajemos definiciendo clases
class Spider12(scrapy.Spider):
    name = 'spider12'
    # Para definir que dominio queremos scrapear y cuales no.
    # Se le puede pasar una lista
    allowed_domains = ['pagina12.com.ar'] # Le estamos diciendo que solamente queremos scrapear dominios que esten dentro de pagina12.com.ar
    # Configurar el tipo de archivo de salida
    # DEPTH_LIMIT es el limite para scrapear
    custom_settings = {'FEED_FORMAT':'json',
                      'FEED_URI':'resultados.json',
                      'DEPTH_LIMIT': 2}
    start_url = ['https://www.pagina12.com.ar/281434-espinoza-lo-que-no-hicieron-en-4-anos-lo-hicimos-en-tres-mes',
 'https://www.pagina12.com.ar/281424-reforma-judicial-juntos-por-el-cambio-no-quiere-que-se-ampli',
 'https://www.pagina12.com.ar/281419-cinco-claves-sobre-el-flamante-registro-de-trabajadores-de-l',
 'https://www.pagina12.com.ar/281341-alberto-fernandez-inauguro-el-hospital-favaloro-en-la-matanz',
 'https://www.pagina12.com.ar/281127-plan-condor-argentina-es-el-pais-que-mas-avanzo-en-el-juzgam',
 'https://www.pagina12.com.ar/281289-se-viene-el-informe-en-diputados',
 'https://www.pagina12.com.ar/281132-causa-peajes-guillermo-dietrich-fue-procesado-por-administra',
 'https://www.pagina12.com.ar/281134-alberto-fernandez-inauguro-el-plenario-de-la-cta-y-convoco-a',
 'https://www.pagina12.com.ar/281139-daniel-gollan-si-se-disparan-los-casos-por-encima-de-un-nume',
 'https://www.pagina12.com.ar/281151-coronavirus-murieron-dos-represores-presos-contagiados',
 'https://www.pagina12.com.ar/281212-reforma-judicial-el-presidente-definio-los-11-nombres-que-in',
 'https://www.pagina12.com.ar/281243-alfredo-cornejo-lo-quiere-a-mauricio-macri-en-cambiemos-pero',
 'https://www.pagina12.com.ar/281266-la-crisis-del-poder-judicial-y-la-necesidad-de-su-reforma']
    
    # Definir un metodo que procese la respuesta de cada solicitud que se haga a cada una de las urls
    def parse(self, response):
        # Articulo promocionado
        nota_promocionada = response.xpath('//div[@class="article-title "]/a/@href').get()
        if nota_promocionada is not None:
            yield response.follow(nota_promocionada, callback=self.parse_nota)
    
        # Listado de notas
        notas = response.xpath('//div[@class="article-footer"]//div[@id="cxense-read-more-widget-283845"]//a/@href').getall()
        for nota in notas:
            yield response.follow(nota, callback=self.parse_nota)
        
        # Link a la sigueinte pagina
        # por si hay algun boton
        # next_page = response.xpath('')
        # if next_page is not None:
            # yield response.follow(next_page, callback=self.parse)
    
    def parse_nota(self, response):
        # Parseo de la nota
        titulo = response.xpath('//div[@class="article-titles"]/h1[@class="article-title"]/text()').get()
        cuerpo = ''.join(response.xpath('//div[@class="article-text"]/p/text()').getall())
        # guaradr la informacion en el json que habiamos definido
        yield {'url': response.url,
                'titulo': titulo,
                'cuerpo': cuerpo}      
```

- Ejecutando el scraper

```python
process = CrawlerProcess()
process.crawl(Spider12)
process.start()
```

## Proxies 

Hacer un scraper consiste en programar un programa que sistematice consultas a distintas paginas web o a una sola. 

Todas esas solicitudes que estan saliendo de manera automatica van a salir con la misma IP de origen. Un servidor web que detecte que todas estas solicitudes vienen todas juntas y bastante rapido una tras de la otra de la misma IP puede llegar a detectar que en realidad se trata de un scraper y no de una persona fisica, entonces puede tomar la desicion de bloquear esa IP para proteger su informacion y no saturar ni generar demaciado trafico.

Es por eso que muchas veces es util esconder o enmascarar la IP desde la cual hacemos este tipo de solicitudes y para esto es necesario usar un proxy.

un **Proxy** es como un intermediario entre nosotros y el servidor web que queremos scrapear, nosotros hariamos esta solicitud al servidor web pero en vez de que el trafico vaya directamente hacia el servidor pasaria primero por un proxy y del proxy seguiria hacia ese servidor, de esta manera logramos que el servidor web vea la IP del proxy y no la nuestra.

Nostros podemos configurar el programa para que utilice distintos proxies y los vaya alternando de manera que el servidor web vea que las solicitudes provienen de distintas direcciones IP y asi es una estrategia que podemos usar para evitar que nuestro scrapy sea bloqueado 

El sitio [mi ip](http://www.cualesmiip.com/ "mi ip") te permite ver cual es la IP saliente de tu red. Si estas en una LAN, seguramente tu IP local sea algo como 192.18.x.x, pero la IP con la que sales al mundo, la IP de tu router asignada por tu ISP, sera diferente.
Links utiles:
[Free Proxy List](https://free-proxy-list.net/ "proxy")
[PySocks](https://pypi.org/project/PySocks/ "PySocks")

- Funcion para scrapear ese sitio web para obtener la IP
```python
import requests
import re

def get_my_ip(url='http://www.cualesmiip.com/', proxies=None):
    try:
        r = requests.get(url=url, proxies=proxies)
    except Exception as e:
        print('Error haciendo la request', e)
        return None

    if r.status_code != 200:
        print("Status Code:", r.status_code)
        return None

    regex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    my_ip = regex.findall(r.text)
    return my_ip[0] if my_ip else None

if __name__ == "__main__":
    print(get_my_ip())
```

[Free Proxy List](https://free-proxy-list.net/ "proxy") es una web en la que tenemos distintas direcciones de servidores proxies que nosotros podemos utilizar de manera gratuita. Al ser gratuitos no estan garantizados su funcionamiento y puede ser un poco mas lento, incluso tampoco esta garantizado que el servidor proxy no este tratando se ver el trafico atravez del proxy.

La recomedacion es utilizar los proxies que tengas `https`.

Crearemos un diccionario en el que pondremos la direccion de los proxy
```python
proxy_dict = {
    'http': 'http://217.219.35.1:8080',
    'https': 'https://217.219.35.1:8080'
}
```

y lo ejecutamos
```
get_my_ip(proxies=proxy_dict)
```

Si queremos usar proxys socks que funcionan a mas bajo nivel(hacia nivel tcp) lo que tenemos que hacer es crear otro diccionario:

La biblioteca que tenemos que utilizar para poder hacer uso de proxies socks [PySocks](https://pypi.org/project/PySocks/ "PySocks"), solamente puede trabajar con proxies socks 4.

En esta ocacion usaremos socks 4 e iremos a la pagina de proxies [Free Socks Proxy List](https://www.socks-proxy.net/ "Free Socks Proxy List")
```python
# Hay varias versiones de socks, en este caso trabajaremos son socks 4 pero existe socks 5
socks_proxy_dict = {
    'http':'socks4':'//41.205.13.126:4145',
    'https':'socks4':'//41.205.13.126:4145'
}
```
y lo ejecutamos
```
get_my_ip(proxies=socks_proxy_dict)
```

## [Tesseract](https://pypi.org/project/tesserocr/ "Tesseract")

**OCR** reconocimiento optico de caracteres.
**Tesseract ocr** una bibleoteca que nos permite utilizar software que ya esta preentrenado para hacer este tipo de reconocimiento. Es decir que partiremos una imagen que tiene texto para extraer el texto en formato de string para que despues lo podamos trabajar mejor.

```python
import tesserocr # Para hacer OCR
import numpy as np # Para hacer manipulacion basica de imagenes
# Para trabajar mas a fondo con imagenes usar la bilbioteca open cb que ya esta preparada especificamente para eso
import matplotlib.pyplot # Para cambiar el formato de archivos
from PIL import Image # Para cambiar el formato de archivos
# Si estas en una jupyter notebook tienes que ejcutar el comando:
#%matplotlib inline
# que lo que hace es permitir que mostremos la imagenes dentro de la misma jupyter 

texto_largo = plt.imread('texto_largo.png')
plt.figure(figsize=(15,5))
plt.imshow(texto_largo)
plt.axis(False);
```
Te deberia aprecer una imagen. Despues usaremos la funciones de tesserocr para extraer el texto de esta imagen y pasarlo a un string
```python
# Se le va a pasar la ruta a la imagen y no la variable con la ruta
# usaremos spanish pero tiene soporte para varios idiomas
texto_ocr = tesserocr.file_to_text('texto_largo.png', lang='spa')
# Si vemos el tiempo de dato de texto_ocr deberia ser un str
type(texto_ocr)
# Y si lo imprimimos deberia de ser el texto de la iamgen
print(texto_ocr)
```

- Otro ejemplo
```python
img = plt.imread('imagen de prueba.png')
plt.imshow(img)

texto_ocr = tesserocr.file_to_text('imagen de prueba.png', lang='spa')
print(texto_ocr)
```
Si imprimimos este script lo mas probable es que falle, que el texto no sea el correcto.

Este error ocurre por que el fondo esta en oscuro y las letras estan en blanco y que aparte de eso estan difusos los bordes de las letras con el fondo. Ahi es cuando la bibleoteca empieza a tener algunos problemas para ahcer este reconocimiento. No lanza ningun error pero el resultado no es el esperado. 

Para resolver eso  se tiene que hacer una peque;a minipulacion sobre esta imagen antes de pasarla al osc.

Veamos primero cuales son las dimenciones de esta imagen 
```python
img.shape
# (62, 228, 4)
```
Al parecer esta imagen tiene 4 canales (r, g, b ,alfa(canal de transparencia)), que en este caso como no lo estamos utilizando simplemento lo vamos a descartar y generar una nueva imagen que sea solamente en rgb(los tres canales)
```python
img_rgb = img[:,:,:3]
```
Ahora el shape de esta imagen deberia ser con tres canales 
```python
img_rgb.shape
# (62, 228, 3)
```
Si visualizamos la imagen de nuevo no a cambiado nada
```
plt.imshow(img)
```
Y efectivamente no cambio nada por que al sacar el canal de transparencia que estabamos utilizando la imagen sigue siendo la misma.

Lo que debemos hacer ahora es invertir los tonos de la imagen para que queden las letras oscuras sobre un fondo claro.

Para esto tenemos que ver como esta codiciador los pixeles.
Nos quedaremos con el primer pixel
```python
# Nos quedaremos con el primer pixel
img_rgb[0,0,0]
# 0.1764706
```

Hay dos formatos posibles en los que pueden venir la informacion de los pixeles, uno de ellos es que se aun numero de numero flotante que vaya de 0 a 1(que es este caso), si no tambien existe la posibilidad de que sea un entero que va de 0 a 255 dependiendo de cual se la codificacion o en que formato vengan la imagen tenemos que realizar distintas operaciones.

En este caso si queremos invertir la imagen en este caso tenermos que:

```
img_inv = 1-img_rgb
``` 
Lo que logramos es invertir los colores de esta imagen
```
plt.imshow(img_inv)
```
Se invirtieron los colores. Tenemos un fondo mas claro con letras obscuras.

Otra cosa que podemos hacer es pasarla a escala de grises, por que en muchos casos tener demaciada informacion(tener las 3 escalas) no aporta deciado y con la imagen en escala de grises ya es suficiente.
```python
# calculamos la media de cada pixel con axis 2
img_gr = img_inv.mean(axis=2)
```
En esta imagen en escala de gruses lo que vamos a obtener es un unico pixel para cada canal y lo vamos a hacer es tener el promedio del canal rgb.

Si mostramos esta imagen en escala de grises.
```
plt.imshow(img_gr, cmap='Greys_r')
```
Vamos a pasar el formato de pixeles que va de 0 a 1 en punto flotante a 255 y como para representar una byt que va de 0 a 255 solo necesitamos 8bys vamos a utilizar uint8
```python
img_pil = Image.fromarray(np.uint8(img_gr*255))
```
Si vemos el tipo de dato de esta imagen deberia de ser de tipo image
```
type(img_pil)
```

Unar tesserocr
```python
# En esta ocacion usamos image_to_text en lugar de file_to_text por que le estamos pasando directamente el objeto de la imagen
print(tesserocr.image_to_text(img_pil, lang='spa'))
``` 

Si esta opcion sabe imperfecta podemos probar con 3 escalas
```
img_pil_inv = Image.fromarray(np.uint8(img_inv*255))
```
```python
print(tesserocr.image_to_text(img_pil_inv, lang='spa'))
``` 
