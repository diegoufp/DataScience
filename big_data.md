# Manejo de Big Data

## Data Warehouse

Un **Data Warehouse** es un repositorio unificado de datos que almacena informacion de distintas fuentes de datos en la organizacion.

Estos repositorios unificados tienen un fin analitico, de manera que su estrucura debe responder a estas necesidades.

El proceso de **ETL** permite llevar los datos de multiples fuentes a un **Data warehouse**

**ETL** por sus siglas en ingles representa:
- Extracion: Se van a extraer los datos de todas las funtes.
- Transformacion: Se eliminaran duplicados, valores nulos, se crearan agrupaciones , se crearan nuevas columnas, etc.
- Carga: Se cargara el Data Warehouse.

### Arquitectura del data warehouse

- **Tablas de hechos**
Contienen la infomacion que queremos medir/ analizar.
- **Tablas de dimensiones**
Contienen la informacion del "como" lo quiero medir.

### Modelo de datos de ejemplo

- **Tablas de hechos**
    - SALES
    - LISTING
- **Tablas de dimensiones**
    - EVENT
    - CATEGORY
    - VENUE
    - DATE
    - USERS

## Bases de datos columnares

Una **Base de datos columnar** es una base de datos optimizada para lograr una recuperacion rapida de columnas de datos, normalmente en aplicaciones analiticas, esto permite procesar queries complejos de una manera optima.

- Excelente para aplicaciones de analitica.
- En redshift cada columna se almacena en bloques de 1 MB.
- Una consulta a una tabla de 10 columnas de las cuales requiero 2, leeria unicamente las 2 necesarias.

## Bases de datos basadas en filas
Enfocados en la transaccionalidad y en la lectura y escritura rapida de filas unicas.

- Excelentes para aplicaciones OLTP.
- Un registro a cada bloque de datos(pueden ser mas).
- Una cosulta a una tabla de 10 columnas de las cuales solo requiero 2, leeria las 8 innecesarias tambien.

## AWS REDSHIFT

