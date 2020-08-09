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