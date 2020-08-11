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
