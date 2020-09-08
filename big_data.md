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

