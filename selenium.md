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
