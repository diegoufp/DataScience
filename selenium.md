# Selenium

Selenium es una suite de distintos software para automatizacion del navegador.

Selenium no es una herramienta de testing ni web scraping, si bien podemos utilizarlo para estas tareas no fue diseñado para ellas y por lo tanto su desempeño puede que no sea el optimo.

## Caracteristicas

### Selenium IDE
- Pros:
    - Excelente para iniciar
    - No requiere saber programar
    - Exporta scripts para Selenium Rc y Selenium WebDriver
    - Genera reportes

- Contras:
    - Disponible solo para Firefox y Chrome
    - No soporta DDT(no podemos colocar datos para que realize multiples pruebas)

### Selenium RC
- Pros:
    - Soporte para: * Varias plataformas, navegadores y lenguajes.
                    * Operaciones logicas y condicionales.
                    * DDT
    - Posee una API madura

- Contras:
    - Complejo de instalar
    - Necesita de un servidor corriendo
    - Comandos redundantes en su API
    - Navegacion no tan realista

### Selenium WebDriver
- Pros:
    - Soporte para multiples lenguajes
    - Facil de instalar
    - Comunicacion directa con el navegador
    - Interaccion mas realista

- Contras:
    - No soporta nuevos navegadores tan rapido
    - No genera reportes o resultados de pruebas
    - Requiere de saber programar

### Selenium Grid
Este servicio es un complemento.

- Se utiliza junto a Selenium RC
- Permite correr pruebas en paralelo
- Conveniente para ahorrar tiempo


## Otras herramientas de testing y automatizacion

### Puppeteer
- Pros:
    - Soporte por parte de Goople
    - Datos del Performance Analysis de Chrome
    - Mayor control de Chorme
    - No requiere de drivers externos

- Contras:
    - Funciona solo en Chrome y con JavaScript
    - Comunidad pequeña

### Cypress.io
- Pros:
    - Comunidad emergente
    - Buena documentacion con ejemplos
    - Bastante agil en pruebas E2E
    - Orientado a desarrolladores
    - Excelente manejo de asincronismo

- Contras:
    - Funciona solo en Chrome y con JavaScript
    - Pruebas en paralelo solo en version pago

### Cual es la mejor opcion?
Para responder esta pregunta se tienen que tomar en cuenta factores como el lenguaje de programacion que conoces tu y tu equipo de trabajo, el proyecto en el que se va a trabajar require de grandes llamadas de asincronismo o no, si solo quieres automatizar una tarea que es repetitiva.

## Instalacion 

```
sudo apt update
apt install python3-pip
pip3 --version
pip3 install selenium
pip3 install pyunitreport
```

## Conceptos

### Unittest (PyTest)
Una libreria de python con la cual vamos a realizar pruebas unitarias para obtener la informacion de lo que ocurre con nuestras automatizaciones. En otras palabras va a preparar el entorno de nuestra automatizacion y despues realizara una serie de acciones para cuando termine el caso de prueba que se esta realizando.

**El caso de prueba** Es una unidad de codigo con el cual estaremos indicando a selenium que queremos que haga o en su defecto alguna funcion que queramos probar.

- **Test Fixture**: preparaciones para antes y despues de la prueba.
- **Test Case**: unidad de codigo a provar.
- **Test Suite**: coleccion de Test Cases.
- **Test Runner**: orquestador de la ejecucion.
- **Test Report**: resumen de resultados.