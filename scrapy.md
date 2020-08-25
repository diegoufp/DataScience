# [Scrapy](https://docs.scrapy.org/en/latest/ "Documentacion de scrapy")

Scrapy es el framework mas utilizado en internet de alto nivel para realizar web scraping y web web crawling.

web crawling es similar al web scraping sin embargo este en lugar de extraer la informacion lo que hace es capturar los links que hay dentro de una pagina e indexarlos para ir link por link para llegar a nuevos sitios(como lo hacen los motores de busqueda).

Scrapy nos permite es extraer la informacion de manera extructurada.
Otra particularidad de scrapy es que e sun framework asincrono. Cada peticion que hacemos al servidor no necesita esperar a la siguiente para completarse, es decir, scrapy puede enviar varias requests a la vez y seguir enviandolas sin necesidad de que las otras terminen para continuar, no realiza las requests de manera secuencial.

- Herramientas de scrapy
    - Procesador de xpath.
    - Interactive Shell.
    - Exportar archivos en el formato que sea (JSON, CSV, etc.)
    - Respera el archivo robots.txt 

En las ocaciones en que no encuentre la informacion no generara error ya que al encontrar un error sigue con las siguientes paginas, no se trava sin que nosotros tengamos que decirle explicitamente como es que queremos que procese los errores.

- Instalacion

```
sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev python3-venv
```

Crea una carpeta en donde trabajarás tu proyecto: esto lo haces con el comando `mkdir nombre_proyecto`. Luego, con `cd nombre_proyecto` te ubicas dentro del directorio.

Una vez ahí, creas tu entorno virtual con `python3 -m venv venv`. Este último comando creará una carpeta de nombre “venv” donde estarán los archivos internos de Python que usará tu proyecto. Verifica con ls que exista.

Ingresa dentro de tu entorno virtual con el comando `source venv/bin/activate`. Esto te permitirá descargar las dependencias necesarias sin interferir con el entorno global de tu sistema operativo.

Ahora, podemos instalar Scrapy sin ningún problema. Otro paquete que instalaremos en el camino es **autopep8**, que nos servirá para formatear automáticamente nuestro código Python siguiendo los lineamientos de [PEP 8](https://www.python.org/dev/peps/pep-0008/ "PEP 8"), la guía de estilos oficial del lenguaje. Ambos paquetes los instalamos con el comando `pip3 install autopep8 scrapy`

Si todo salió bien, con el comando `scrapy version` y `pip freeze` tu terminal debería devolverte la versión del framework que acaba de instalarse. 

## [Web Scraping Sandboox](http://toscrape.com/ "Web Scraping Sandboox")

En Web Scraping Sandboox hay dos paginas para hacer practicas en esta ocacion iniciaremos con la de **Quotes**.

El objetivo es crear un peque;o scrit que obtenga estas citas pero en su totalidad.

Estando en nuestra carpeta de scrapy ejecutamos el siguiente comando en la terminal

```
scrapy startproject tutorial
```

y seguimos la instrucciones que nos da scrapy, en esta ocacion nos dice que entramos en la carpeta tutorial

```
You can start your first spider with:
    cd tutorial
    scrapy genspider example example.com

```

Y dentro de la carpeta buscamos otra carpeta que se llame spiders y entramos en ella para crear un archivo con el nombre que queramos. Y despues entramos en el para escribir el script.
```
cd spider/
touch quotes_spider.py
vim spider.py
```
```python
import scrapy

# Se creara una clase
# En esta clase se define la logica para traer toda la informacion que queremos desde internet
class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls =[
        'http://quotes.toscrape.com/'
    ]

    # self hace referencia a la instancia posterior de la clase
    # response hace referencia a la respuesta http 
    def parse(self, response):
        # Este metodo es el que define la logica apartir de la cual nosotros extraemos informacion
        # con with open abrimos un archivo 
        # w -> modo escritura
        with open('resultados.html', 'w', encoding='utf-8') as f:
            # Escribir en esta archivo el contenido de la respuesta html
            f.write(response.text)
```

Para ejecutar se ingresa en comando especial de scrapy
```
scrapy crawl quotes
```
Para salir del entorno virtual se ejecuta el codigo 
```
deactivate
```

## Generadores e iteradores

- Iteradores
```python

my_list = [1,2,3,4,5]
# Esta variable lo que va hacer es contener a esta lista my_list(es un iterable convertido en iterador que es lo que python pude recorrer por debajo)
my_iter = iter(my_list)
# Si inprimimos my_iter con type nos mostrara que es un list_iterator y no una lista 
#print(type(my_iter))
# Extraer los elementos
print(next(my_iter)) # Como respuesta sale 1
# Si imprimimos 3 veces
print(next(my_iter)) # Como respuesta sale 1
print(next(my_iter)) # Como respuesta sale 2
print(next(my_iter)) # Como respuesta sale 3
# esto es lo que hace un siclo for por dentro
# Cuando encuentra el error StopIteration es ciclo para
```

- Generadores 
En python existen formas faciles de crear iteradores las cuales son llamadas generadores.

Una **funcion** normal cuando hacer `return` de un elemento corta la ejecucion de la funcion. En un **generador** cuando hacer un return python guarda el estado de la funcion y continua la ejecucion donde lo dejaste para que cuando vuelvas a llamar a a funcion ese estado lo tengas disponible otra vez

```python
def my_func():
    a = 1
    return a

    a = 2
    return a

    a = 3
    return a

print(my_func())
print(my_func())
print(my_func())
```
Si imprimimos esta script de resultado imprimiran solo el numero 1. Por que cuando python encuentra un `return` dentro de la funcion significa que ahi termina y todo lo que hay debajo no importa.

UN generador es una funcion que puede recordar estados. Este seria un ejemplo de un generador:

```python
def my_gen():

    # yield lo que hace es hacer un return parcial.
    a = 1
    yield a

    a = 2
    yield a

    a = 3
    yield a

    # Un generador es una manera facil de crear un iterador 
    # Cuando asignamos la funcion a una variable lo que estamos indicandole a python es que
    # retorne un iterador y que lo guarde dentro de la variable 
    my_first_gen = my_gen()
    # Si nosotros ejecutamos con el metodo next 3  veces saldran 1 , 2, 3 por que guarda los estados.
    print(next(my_firsr_gen))
    print(next(my_firsr_gen))
    print(next(my_firsr_gen))
```

## Scrapy Shell

Usar la consola interactiva de scrapy
Entramos al entorno virtual y ejecutamos en la terminal de comandos
```
scrapy shell "http://quotes.toscrape.com/"
```
Si no ocurrio ningun error abrira una cosola de python y ya podemos empezar a usar una serie de objetos que nos provee scrapy.

E esta ocacion llamaremos al metodo response.xpath
```python
# get da la indicacion a python de traer un solo elemento
response.xpath('//h1/a/text()').get()
```
```python
# getall nos permite traer una lista con los elementos buscados
response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
```

## Primer proyecto

### Estructura de carpetas

Entrar al entorno virtual y crear un anueva carpeta
```
source venv/bin/activate
mkdir quotes_scraper
cd quotes_scraper/
```

Inicializar proyecto de scrapy
```
scrapy startproject quotes_scraper
```

Moverse a la carpeta del proyecto
```
cd quotes_scraper
```

Dentro de esta capteta hay varios archivos.

- pipelines.py
Es un archivo que nos permite modificar nuestros datos desde que entran a nuestros **spiders** hasta llegar al final.

- middlewares.py
Es un archivo que nos permite trabajar con un concepto denominado **señales**, es decir, podemos controlar eventos que suceden en algun momento de ese tiempo en el cual nosotros hacemos la requests, obtenemos la informacion y la traemos a nuestro programa.

- items.py
Dentro de este archivo tenemos una manera complejo de transformar y jugar con estos datos que a nostros nos envia la respuesta HTML para guardarlos de una manera estandar.

- __init__.py
Es el archivo que define que todo esto es una modulo de python 

- settings.py
Dentro de este achivo tenemos un monton de configuraciones interesantes.
En **BOT_NAME** nosotro podemos definir el nombre del robot que va a usar scrapy para referirse a si mismo dentro de estas requests, en este caso es quotes_scraper.
**ROBOTSTXT_OBEY** puedes habiliar o deshabilitar la opcion para obedecer al archivo robots.txt.
**CONCURRENT_REQUESTS** cuantas peticiones puede hacer al mismo tiempo, por default son 16.
**DOWNLOAD_DELAY** que tiempo espera scrapy entre descarga y descarga de el resultado de las requests
**CONCURRENT_REQUESTS_PER_IP** las requests consecutivas que se pueden hacer por direccion IP.
**DEFAULT_REQUEST_HEADERS** cambiar los header que va a tener esta peticion (las cabeceras http)
**COOKIES_ENABLED** habilitar los cookies.

- spider/
Donde podremos nuestros scrips de python

### Spiders

Un spider es una clase de python en la cual nosotros definimos la logica necesaria para extraer informacion.

Para crear un spider entramos a la carpeta spiders y creamos un archivo
```
cd spiders
touch quotes.py
vim quotes.py
```
```python
import scrapy

class QuotesSpider(scrapy.Spider):
    # name es el nombre unico con el que scrapy se va a referir a este spider dentro del proyecto
    # Es un nombre que no es repetible 
    # Es decir si nosotros tenemos en el futuro otros spider no podemos ponerle el mismo nombre 
    name = 'quotes'
    # lista de urls a las cuales vamos a hacer la peticion http
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    # Metodo obligatorio dentro del spider
    # parse significa analizar un archivo para extraer informacion valiosa a partir de el
    # el metodo parse analizara las respuestas http que nos envia la peticion de esta pagina
    # y apartir de esa respuesta traer toda la informacion.
    # respose es la respuesta http que surge despues de hacer una peticion
    def parse(self, response):
        print('*' * 10)
        print('\n\n')
        print(response.status, response.headers)
        print('*' * 10)
        print('\n\n')
```

Para ejecutar el spider ejecutamos `scrapy crawl quotes`, en este caso `quotes` es el name que se le puso dentro del script
```
scrapy crawl quotes
```

### Usando Xpath para extraer datos

Recuerda siempre verificar que el entorno virtual este activado y que estemos dentro de la carpeta del proyecto

```
scrapy shell 'http://quotes.toscrape.com/'
```
```python
response.xpath('//div[@class="row"]/div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').getall()
```
Cerramos scrapy
```
exit()
```

Abrimos el archivo del anterior subtema
```
vim quotes.py
```
```python
import scrapy

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[@class="row"]/div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()

class QuotesSpider(scrapy.Spider):
    # name es el nombre unico con el que scrapy se va a referir a este spider dentro del proyecto
    # Es un nombre que no es repetible 
    # Es decir si nosotros tenemos en el futuro otros spider no podemos ponerle el mismo nombre 
    name = 'quotes'
    # lista de urls a las cuales vamos a hacer la peticion http
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    # Metodo obligatorio dentro del spider
    # parse significa analizar un archivo para extraer informacion valiosa a partir de el
    # el metodo parse analizara las respuestas http que nos envia la peticion de esta pagina
    # y apartir de esa respuesta traer toda la informacion.
    # respose es la respuesta http que surge despues de hacer una peticion
    def parse(self, response):
        print('*' * 10)
        print('\n\n')
        
        title = response.xpath('//h1/a/text()').get()
        print(f'Titulo: {title}')
        print('\n\n')

        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        print('Citas: ')
        for quote in quotes:
            print(f'- {quote}')
        print('\n\n')

        top_ten_tags = response.xpath('//div[@class="row"]/div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').getall()
        for tag in top_ten_tags:
            print(f'- {tag}')
        print('\n\n')

        print('*' * 10)
        print('\n\n')
```

Y lo ejecutamos 
```
scrapy crawl quotes
```

## [Guardando los datos](https://translate.googleusercontent.com/translate_c?depth=1&hl=es&prev=search&pto=aue&rurl=translate.google.com&sl=en&sp=nmt4&u=https://docs.scrapy.org/en/latest/topics/feed-exports.html&usg=ALkJrhiBLXna-9v0gpyPNZg3zq9qvPgBeA#settings "Guardando los datos") 

Para guardar los datos ya sea en formato csv, json u otro debo convertir al metodo parse en un generador haciendolo de la siguiente manera:
```python
import scrapy

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[@class="row"]/div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        top_ten_tags = response.xpath('//div[@class="row"]/div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').getall()
    # con yield convertiremos esta funcion en un gerador 
        yield {
            'title': title,
            'quotes': quotes,
            'top_ten_tags': top_ten_tags
        }
```
En la consola de comandos utilizaremos el mismo comando para llamar  auna spider `scrapy crawl quotes` pero esta vez se le hagregaran parametros adicionales para guardar la informacion en el formato que queramos:
```
scrapy crawl quotes -o quotes.json
```
Si quisieramos que el archivo se genere en csv:
```
scrapy crawl quotes -o quotes.csv
```

Si vuelvo a ejecutar el comando anterior ya existiendo ese archivo lo que realizara scrapy es un append al archivo existente, para solucionar este problema y no tener datos duplicados unicamente debo borrar el archivo antes de ejecutar el comando.

## Seguir links: response.follow

Si alguien busca una herramienta con la cual puedan dar “clicks” de forma automática o ingresar labels para enviar formularios, puede investigar la herramienta SELENIUM de Python.
Es muy útil para extraer datos de esta manera. Tiene algunas cuantas limitaciones como la resolución de Captchas, por ejemplo.

Aunque para mi, selenium es solo recomendable si se cumplen estas dos condiciones:

- No existe el atributo href que te permita ir a la siguiente pagina.
- La url es un desastre, es decir que tenemos que renegar mucho con expresiones regulares como para tener una lista de todas las urls.

### Presionar botones con scrapy
En la terminald e comandos
```
scrapy shell "http://quotes.toscrape.com/"
```
Cuando carge buscamos el boton con xpath
```
response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
```
Si todo resulto de manera correcta este deberia ser el resultado `'/page/2/'` lo cual infica que cambio de pagina.

### Escribiendo el spider
```python
import scrapy

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[@class="row"]/div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()
# Next page button = //ul[@class="pager"]/li[@class="next"]/a/@href

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # En esta ocacion modificaremos el metodo parse para inticarle a python que siga el link de next

        title = response.xpath('//h1/a/text()').get()
        quotes = response.xpath('//span[@class="text" and @itemprop="text"]/text()').getall()
        top_ten_tags = response.xpath('//div[@class="row"]/div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').getall()
    # con yield convertiremos esta funcion en un gerador 
        yield {
            'title': title,
            'quotes': quotes,
            'top_ten_tags': top_ten_tags
        }

        next_page_button_link = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()
        # Agregaremos un if para saber si el boton existe
        if next_page_button_link:
            # el metodo follow del objeto response lo que hace es tomar la url absoluta
            # y automaticamente a;adir lo que tenemos despues.
            # este metodo follow lleva dos parametros
            # 1.El link que nosotros vamos a seguir 
            # 2.callback el cual es una funcion que se va a ejecutar luego de hacer la requests a ese link en esta ocacion es la misma que tenemos escrita 'parse'
            yield response.follow(next_page_button_link, callback=self.parse)
```
Y finalmete lo ejecutamos
```
scrapy crawl quotes -o quotes.json
```

## Miltiples callbacks

Se solucionara el error donde se repide informacion modificando el codigo del tema anterior.

```python
import scrapy

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[@class="row"]/div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()
# Next page button = //ul[@class="pager"]/li[@class="next"]/a/@href

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    # Se creara un nuevo metodo de tipo parse
    # Este metodo va a extraer exclusivamente las sitas no va a extraer los titulos no va a extraer las tags
    # Se recibiran los kwars que se estan enviando al metodo response.follow

    def parse_only_quotes(self, response, **kwargs):
        new_quotes = response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall()
        kwargs["quotes"].extend(new_quotes)

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(
                next_page_button_link,
                callback=self.parse_only_quotes,
                cb_kwargs=kwargs
            )
        else:
            yield kwargs

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()

        quotes = response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall()

        tags = response.xpath(
            '//div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').getall()

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]//li[@class="next"]/a/@href').get()
         # el metodo follow del objeto response lo que hace es tomar la url absoluta
            # y automaticamente a;adir lo que tenemos despues.
            # este metodo follow lleva dos parametros
            # 1.El link que nosotros vamos a seguir 
            # 2.callback el cual es una funcion que se va a ejecutar luego de hacer la requests a ese link en esta ocacion es la misma que tenemos escrita 'parse'
            # En esta ocacion se le puede agregar un nuevo metodo 
            # A este nuevo argumento se le enviaran las citas de las primera pagina y se hace con el atributo cb_kwargs
        if next_page_button_link:
            yield response.follow(
                next_page_button_link,
                callback=self.parse_only_quotes,
                cb_kwargs={
                    "title": title,
                    "quotes": quotes,
                    "top_ten_tags": tags,
                }
            )
```

## Pasando argumentos a nuestro spider

Para pasar un argumento en un spaider y controlar el numero de tags se modificara el codigo
```python
import scrapy

# Titulo = //h1/a/text()
# Citas = //span[@class="text" and @itemprop="text"]/text()
# Top ten tags = //div[@class="row"]/div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()
# Next page button = //ul[@class="pager"]/li[@class="next"]/a/@href

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    # Se creara un nuevo metodo de tipo parse
    # Este metodo va a extraer exclusivamente las sitas no va a extraer los titulos no va a extraer las tags
    # Se recibiran los kwars que se estan enviando al metodo response.follow

    def parse_only_quotes(self, response, **kwargs):
        new_quotes = response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall()
        kwargs["quotes"].extend(new_quotes)

        next_page_button_link = response.xpath(
            '//ul[@class="pager"]//li[@class="next"]/a/@href').get()
        if next_page_button_link:
            yield response.follow(
                next_page_button_link,
                callback=self.parse_only_quotes,
                cb_kwargs=kwargs
            )
        else:
            yield kwargs

    def parse(self, response):
        title = response.xpath('//h1/a/text()').get()

        quotes = response.xpath(
            '//span[@class="text" and @itemprop="text"]/text()').getall()

        tags = response.xpath(
            '//div[contains(@class, "tags-box")]/span[@class="tag-item"]/a/text()').getall()

        # getattr es una funcion que viene en el cor de python y en esta ocacion lo que se espera es un numero
        # Si existe dentro de la ejecucion de este spider un atributo de nombre top se guardara el resultado dentro de la variable top si no existe el resultado sera None
        top = getattr(self, 'top', None)
        if top:
            top = int(top)
            tags = tags[:top]


        next_page_button_link = response.xpath(
            '//ul[@class="pager"]//li[@class="next"]/a/@href').get()
         # el metodo follow del objeto response lo que hace es tomar la url absoluta
            # y automaticamente a;adir lo que tenemos despues.
            # este metodo follow lleva dos parametros
            # 1.El link que nosotros vamos a seguir 
            # 2.callback el cual es una funcion que se va a ejecutar luego de hacer la requests a ese link en esta ocacion es la misma que tenemos escrita 'parse'
            # En esta ocacion se le puede agregar un nuevo metodo 
            # A este nuevo argumento se le enviaran las citas de las primera pagina y se hace con el atributo cb_kwargs
        if next_page_button_link:
            yield response.follow(
                next_page_button_link,
                callback=self.parse_only_quotes,
                cb_kwargs={
                    "title": title,
                    "quotes": quotes,
                    "top_ten_tags": tags,
                }
            )
```
Y en la terminar de comandos se agregara el argumento
```
rm quotes.json | scrapy crawl quotes -a top=3 -o quotes.json
```

## Configuraciones utiles

```python
# CONCURRENT_REQUESTS nos permite establecer un numero entero apartir delcual scrapy va a iniciar una serie de peticiones teniendo en cuenta ese numero, es decir en esta ocacion le estamos diciendo a scrapy que realize 24 peticiones a la vez como maximo.

# MEMUSAGE_LIMIT_MB La cantidad de memoria ram que le permitimos usar a scrapy para trabajar, muy util en servidores en la nube.

# MEMUSAGE_NOTIFY_MAIL una lista de mails a los cuales notificara si la memoria ram llega a su limite o se pasa de el

# ROBOTSTXT_OBEY Decirle si va a obedecer o no al archivo robots.txt True o False

# USER_AGENT la cabecera http que esta en la peticion a la que le indicamos a sitio web quieres somo nosotros 
custom_settings = {
    'FEED_URI': 'quotes.json',
    'FEED_FORMAT': 'json',
    'CONCURRENT_REQUESTS': 24
    'MEMUSAGE_LIMIT_MB': 2048, 
    'MEMUSAGE_NOTIFY_MAIL': ['notiene@gmail.com'],
    'ROBOTSTXT_OBEY': True,
    'USER_AGENT': 'PepitoMartinez',
    'FEED_EXPORT_ENCODING': 'utf-8'
}
```

## Intelligence Agency

[CIA](https://www.cia.gov/index.html "CIA")

En la pagina de la [CIA](https://www.cia.gov/index.html "CIA") no hay una clausula donde diga que no se puede hacer web scrapyng y tampoco existe un archivo robots.txt. Asi que nada impide extraer archivos [clasificados](https://www.cia.gov/library/readingroom/historical-collections "clasificados")

Inicias scapy en la terminal de comandos
```
scrapy shell 'https://www.cia.gov/library/readingroom/historical-collections'
```
```
response.xpath('//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href').getall()
```
Para cambiar a otra url cuando ya se inicio scrapy en la terminal de comandos 
```
fetch('https://www.cia.gov/library/readingroom/collection/lunik-loan-space-age-spy-story')
```
```
response.xpath('//h1[@class="documentFirstHeading"]/text()').get
```
```
response.xpath('//div[@class="field-item even"]//p[not(@class)]/text()').get()
```
### Se escribe el spider de la CIA

```python
import scrapy

# XPATH

# links = //a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href

# title = //h1[@class="documentFirstHeading"]/text()

# paragraph = //div[@class="field-item even"]//p[not(@class)]/text()

class SpiderCIA(scrapy.Spider):
    name = 'cia'
    start_urls = [
        'https://www.cia.gov/library/readingroom/historical-collections'
    ]

    custom_settings = {
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        links_desclassified = response.xpath('//a[starts-with(@href, "collection") and (parent::h3|parent::h2)]/@href').getall()
        for link in links_desclassified:
            # Lo que va a hacer response.urljoin es convinar la url absoluta de donde estaban los archivos desclasificados con la url relativa que nos da el 'link' del for
            yield response.follow(link, callback=self.parse_link, cb_kwargs={'url': response.urljoin(link)})

    def parse_link(self, response, **kwargs):
        link = kwargs['url']
        title = response.xpath('//h1[@class="documentFirstHeading"]/text()').get()
        paragraph = response.xpath('//div[@class="field-item even"]//p[not(@class)]/text()').get()

        yield{
            'url': link,
            'title': title,
            'body': paragraph
        }

```
```
scrapy crawl cia -o cia.json
```

## Deploy en [Scrapy Cloud](https://www.scrapinghub.com/scrapy-cloud/ "Scrapy Cloud")

Existe una nube hecha por las misma personas que trabajaron en scrapy para que los spider se puedan poner en internet para que los datos sean accesibles.

Lo primero es crearse una cuenta, puedes registrarte con una cuenta de google o github.

Ya cuando te hayas registrado tienes que `crear un nuevo proyecto`.
Y despues el sitio te dara las intrucciones que tiene que hacer en la terminal de comandos.

Tienes que estar en la carpeta del proyecto en la terminal de comandos.

Este paquete de python nos permite logearnos de manera remota en la nube de scrapy y hacer el deploy efectivo de nuestro proyecto.
```
pip install shub
```
Este comando nos va a pedir una API key despues que esta no la dara en las intrucciones.
```
shub login
```
```
shub deploy #####
```
Si no occurrio ningun error solo falta recargar la pagina del navegador y estaran los archivos subidos.

En la pesta;a de `Dashboard` se encontraran tus spiders junto con la informacion del codigo.

Para hacerlo accecible en la pesta;a de `Dashboard` , `Items`, boton `PUBLISH` y en la opcion de `publish dataset`. Despues es necesario el ingrear un logo para el dataset.

Para salir de la cuenta en la terminal de comandos logeada
```
shub logout
```
### automatizar procesos con la API

Tambien se pueden [automatizar procesos con la API de scrapy](https://doc.scrapinghub.com/scrapy-cloud.html "API de scrapy") por terminal.

curl verificara si esta revocado el certificado por este motivo puede dar error para evitarle se le agrega la bandera
```
--ssl-no-revoke
```
quedando asi para automatizar un proceso desde terminal.
```
curl -u KEY:https://app.scrapinghub.com/api/run.json -d project=PROJECT-d spider=cia --ssl-no-revoke
```
Para descargar la informacion capurada del spider
```
curl -u APIKEY: https://app.scrapinghub.com/items/PROYECT_ID/SPIDER_NUMER/JOB_NUMBER
```
