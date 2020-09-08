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

### ¿Cómo funciona AWS Redshift?

El secreto es repartir el trabajo, no se instala en un único servidor sino que se instala en un clúster(arreglos de varios servidores conectados {NODOS})

**Nos conectamos a un nodo líder.**
El cual organiza y asigna las tareas a los otros nodos. (Tareas en paralelos)
El nodo seguidor
Y cada nodo seguidor reparte su tarea entre sus Slides. Para trabajar la tarea asignada por el nodo lider en paralelo.

La base de redshift es PostgreSQL.

### Beneficios de usar Redshift

- Integracion total con AWS.
- Las bases de datos mas rapidas en la nube.
- Los costos mas bajos en la nube.
- Alta escalabilidad.
- Clientes SQL.

### Creando entorno de trabajo en AWS

Al entrar a [AWS](https://us-east-2.console.aws.amazon.com/console/home?region=us-east-2 "AWS") se busca la opcion `IAM` en `All services`.

Nos iresmos a `Roles` en la pesta;a de `Administacion del acceso` y le damos en el boton de `Crear un rol`.

En `Or select a service to view its use cases` buscamos `Redshift` y despues en `Redshift - Customizable` y despues en el boton `Nexr: Permissions`.

En el Search buscamos `S3` y se;alamos la opcion de `AmazonS3FullAccess` y en el boton `Next: Tags`.

En esta opcacion no crearemos etiquetas si se le damos en el boton `Next` y le ponemos un nombre al rol y le damos en el boton `Crear rol`.

Si ya tenemos un rol de permisos para acceso a AWS y a S3 entonces ahora se creara un buket de datos en S3.

Volvemos al incio de [AWS](https://us-east-2.console.aws.amazon.com/console/home?region=us-east-2 "AWS") se busca la opcion `s3` en `All services`.

Y le damos en `crear bucket` y le asignamos un nombre y le damos en `Crear`.

Un **bucket** es simplemente un espacio de almacenamiento de datos en donde se pueden agregar carpetas y archivos de mucha capacidad. Este es un servicio que te empieza a acobrar a partir de terabyts de informacion.

### Configura cluster

Para este caso se usara la version gratuita de amazon redshift

Al entrar a [AWS](https://us-east-2.console.aws.amazon.com/console/home?region=us-east-2 "AWS") se busca la opcion `Amazon Redshift` en `All services`.

Le damos a la pesta;a de [CLUSTERS](https://us-east-2.console.aws.amazon.com/redshiftv2/home?region=us-east-2#clusters "CLUSTERS") y despues en el boton `crear clusters`.

Tenemos un identificador de cluster, en esta ocacion en `Node type` seleccionamos `DC2` opcion `dc2.large` y le agregaremos 2 nodos.

Le podemos cambiar el nombre de la base de datos, tenemos que agregar un nombre de usuario con contrase;a.

En `Cluster permissions (optional)` en `Available IAM roles` le agregamos el rol que creamos y le damos en el boton de `crear cluster`.