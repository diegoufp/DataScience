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