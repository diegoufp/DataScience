# PostgreSQL Aplicado a Ciencia de Datos

## Installacion

[**PostgreSQL**](https://www.postgresql.org/download/ "PostgreSQL")
**Linux distribucion debian**
```

apt-get install postgresql postgresql-contrib phppgadmin
```
**Para ver la version**
```
psql --version
```
**Iniciar postgresql**
```
sudo -u postgres psql
```
**Saber puerto de postgres**
```
sudo netstat -plunt |grep postgres
```

**Estatus del servicio**
```
sudo service postgresql status 
```
[**PgAdmin 4**](https://www.pgadmin.org/download/ "PgAdmin 4")
Herramienta grafica para la base de datos.

```
sudo apt install pgadmin4  
```
```
https://www.youtube.com/watch?v=b1wDX2SfVv4
```

## ¿Qué es Postgresql?
Postgresql es un motor de bases de datos. Permite estructurar toda la informaciond entro de una servidor. Es una base de datos relacionar.

Cuenta con:
- **PL/PgSQL**: Lenguaje backend interno del moto de base de datos.

- **PostGIS**: Plugin para recibir informacion de sistemas informacion geografica.

Cumple el estandar **ACID**:
- **A**: Atomicity – Atomicidad -> Separar las funciones desarrolladas en la BD como pequeñas tareas y ejecutarlas como un todo. Si alguna tarea falla se hace un rollback(Se deshacen los cambios)
- **C**: Consistency – Consistencia -> Todo lo que se desarrolló en base al objeto relacional. Los datos tienen congruencia
- **I**: Isolation – Aislamiento -> Varias tareas ejecutándose al mismo tiempo dentro de la BD
- **D**: Durability – Durabilidad -> Puedes tener seguridad que la información no se perderá por un fallo catastrófico. PostgreSQL guarda la información en una Bitácora

## Conceptos importantes de las bases de datos relacionales

- **Entidades/Tablas**
Cualquier conjunto de objetos representable del mundo real en una base de datos.

- **Atributos**
Son propiedades que estan ligadas al objeto.

- **Relaciones**
Nos permiten ligar una entidad con otra entidad para saber la relacion que existe entre ellas.

Hay dos conceptos imporantes que se abordaron con postgrestsql:

- **Trigger**
Son otro tipo de funciones, que nos permite unir los stored procedures con un evento, por ejemplo, si añades un registro a una tabla, si cambias uno o borras uno, puedes indicar que antes, durante o después, juntar una serie de instrucciones almacenadas en un stored procedures. 

- **Stored procedure**
Son funciones o procedimientos que nos permite almacenar el manejador de bases de datos que nos permite ejecutar repetidas veces de manera util sin tener que repetir el mismo codigo.

## Comandos de Postgres

- Entrar a posgrest
```
sudo -u postgres psql
```

- Ver los comandos de '\' en postgres
```
\?
```

- Listar todas las bases de datos
```
\l
```

- Ver las tablas de una base de datos
```
\dt
```

- Listar los esquemas de la base de datos actual
```
\dn
```

- Listar las funciones disponibles de la base de datos actual
```
\df
```

- Listar las vistas de la base de datos actual
```
\dv
```

- Listar los usuarios y sus roles de la base de datos actual
```
\du
```

- Cambiar de base de datos
```
\c nombre_BD
```

- Describir una table
```
\d nombre_tabla
```

- Ver todos los comando de sql
```
\h
```

- Ver como se ejecuta un comando sql
```
\h nombre_de_la_funcion
```

- Cncelar todo lo que hay en pantalla
```
Ctrl + c
```

- Ver la version de postgres instalada
```
SELECT version();
```

- Volver a ejecutar la funcion realizada anteriormente
```
\g
```

- Ver el historial de comandos ejecutados
```
\s 
```

- Si se quiere guardar la lista de comandos ejecutados en un archivo de texto plano
```
\s <nombre_archivo>
```

- Ejecutar los comandos desde un archivo
```
\i <nombre_archivo>
```

- Permite abrir un editor de texto plano, escribir comandos y ejecutar en lote. \e abre el editor de texto, escribir allí todos los comandos, luego guardar los cambios y cerrar, al cerrar se ejecutarán todos los comandos guardados.
```
\e
```

- Equivalente al comando anterior pero permite editar también funciones en PostgreSQL
```
\ef
```

- Inicializar el contador de tiempo para que la consola te diga en cada ejecucion cuando temoro en ejecutar esa funcion.Activar / Desactivar el contador de tiempo por consulta
```
\timing
```

- Cerrar la consola
```
\q
```


- Crear base de datos
```
CREATE DATABASE nombre_de_la_BD;
```

- Cambiar contrase;a de un usuaio de la base de datos
```
ALTER USER postgres PASSWORD 'newPassword';
```

- Sentrencias de sql
**SELECT**
**FROM**
**WHERE**
**GROUP BY**
**ORDER BY**

## Archivos de Configuración

- **postgresql.conf**:
Configuración general de postgres, múltiples opciones referentes a direcciones de conexión de entrada, memoria, cantidad de hilos de pocesamiento, replica, etc.

- **pg_hba.conf**:
Muestra los roles así como los tipos de acceso a la base de datos(IP's).

- **pg_ident.conf**:
Permite realizar el mapeo de usuarios. Permite definir roles a usuarios del sistema operativo donde se ejecuta postgres.

Para encontrar los **archivos de configuracion** tenemos que ejecutar en pgAdmin o en la terminarl de comando pero ya iniciado postgres:
```
SHOW config_file;
```

## Aplicación de la ciencia de datos

- **Data Driven**: Toma de decisiones basadas en datos e informada
- **Información significativa**: Entender de que manera podemos aprovechar siertos datos para decir que cosa y cómo la vamos a presentar
- **Mostrar y presentar los datos** en el formato y estructura adecuada. Tabla, tendencias, Dashboards
- **Discriminación de datos** para realizar modelos de ML
- **Contar una historia** con los datos

## Equipos orientados a datos


- **DBA** (Dabta Base Administrator) Mantener y administrar el motor de base de datos
- **Data Warehouse** (Almacén de datos). Guardar datos pensando a futuro para poder trabajarse
- **ETL/ Data Pipelines** Llevar datos de un lado a otro
- **BI** (Business Intelligence) Precursores del DataScience, empezar a extraer datos y entender los datos y sus repercusiones, encontrar patrones
- **Data Science** Entender a la organización e impactarla de forma positiva
- **ML** (Machine Learning) Técnica para clasificar información o realizar predicciones con datos historicos

## Data science vs. Machine Learning

**ML** es un conjunto de ciencias, estrategias, disciplinas y algoritmos que nos van ayudar a tomar la capacidad de computo de las maquinas para resolver problemas de clasificación, de forma que se haga de forma automática, otro punto es realizar predicciones con base a patrones para generar tendencias acorde al comportamiento historico para predecir el futuro

**Data Science** Conoce a la organización y empresa a detalle para poder hacer algo al respecto. Toma todas las variables de la organización y herramientas disponibles para causar el mejor impacto

**ML** Es una herramienta más que complementa al Data Science y a la organización

## Diferencias entre otros manejadores y PostgreSQL


1. Código libre y orientado a la comunidad.
2. Base de datos adaptable: soporta documentos JSON y orientadas a estadísticas.
3. PL/pgSQL (procedural languaje).
4. Manejador de objetos: objetos clave/valor.
5. Particiones: permite ejercer una estrategia de particionado para Big Data.
6. Common table expressions: usa tablas virtuales y dinámicas en tiempo de ejecución.
7. Window functions: encontrar la relación entre un row particular y su relación con toda la tabla.

## PLPGSQL: Stored procedures

- **Funciones** → Son más avanzadas. Regresan tipos de datos. Tienen más flexibilidad. No son estándar de SQL, se tiene que usar el lenguaje PLPGSQL.
- **Procedures** → Integran lógica a la sentencias SQL. Se han ido incluyendo en el estándar SQL. No regresan ningún valor.

**Funciones estandar de SQL**:
```sql
-- 'OR REPLACE' nos permite remplazarla cada vez que la vamos a ejecutar
-- 'PROCEDURE' es una palabra reservada para crear una funcion
-- Lo que ira dentro de los signos '$$' es el codigo de la funcion que se va a ejecutar.

CREATE OR REPLACE PROCEDURE test_drpcreate_procedure()
LANGUAGE SQL 
AS $$ 
    DROP TABLE IF EXISTS aaa;
    CREATE TABLE aaa (bbb char(5) CONSTRAINT firstkey PRIMARY KEY)
$$;
```

En `pgAdmin` en `Schemas/public/Procedures` podemos ver la funcion creada. Para llamar a la funcion debemos usar:
```sql
CALL test_drpcreate_procedure();
```

**Lenguaje de Postgresql**:
```sql
-- Como estas funciones siempre regresan un valor que tenemos que indicarle que no regrese con 'RETURNS VOID'.

-- Para las funciones de 'plpgsql' necesitamos dos palabras reservadas a parte de los signos '$$' que son 'BEGIN' que va a indicar donde la funcion empieza y 'END' que indicara donde la funcion termina.

-- FORMA 1:
CREATE OR REPLACE FUNCTION test_dropcreate_function()
RETURNS VOID
AS $$
    BEGIN
        DROP TABLE IF EXISTS aaa;
        CREATE TABLE aaab (bbba char(5) CONSTRAINT firstkey PRIMARY KEY, ccca char(5));
    END;
$$ LANGUAGE plpgsql;

-- FORMA 2:
CREATE OR REPLACE FUNCTION test_dropcreate_function()
RETURNS VOID
LANGUAGE plpgsql;
AS $$
BEGIN
    DROP TABLE IF EXISTS aaa;
    CREATE TABLE aaab (bbba char(5) CONSTRAINT firstkey PRIMARY KEY, ccca char(5));
END
$$;
```

En `pgAdmin` en `Schemas/public/Functions` se deberia poder ver la nueva funcion creada. Y se ejecutaria:
```sql
SELECT test_dropcreate_function();
```

## PLPGSQL: conteo, registro y triggers

```sql
CREATE OR REPLACE FUNCTION count_total_movies()
RETURNS int
LANGUAGE plpgsql
AS $$
BEGIN
    RETURN COUNT(*) FROM peliculas;
END
$$;

SELECT count_total_movies();
```

**Triggers**(disparadores):
```sql
-- La idea de esta funcion es vamos a tomar el registro de una tabla y lo vamos a insertar igual o transformado en otra tabla. Esto es por que aveces necesitas tener tabla en sincronia

-- 'NEW' es us una variable que se encuentra en todas las funciones de trigger, en esta caso 'NEW' Inserta el nuevo valor que tiene el campo_b (a_tabla) en campo_a (ab_tabla).'RETURN NEW' Regresa los campos que tendrá la tabla modificada, en este caso los nuevos.

CREATE OR REPLACE FUNCTION duplicate_records()
RETURNS TRIGGER -- Función tipo trigger.
LANGUAGE plpgsql
AS $$
BEGIN
	INSERT INTO ab_tabla(campo_a, campo_b) --Inserta en los campos campo_a y campo_b de la tabla ab_tabla.
	VALUES (NEW.campo_b, NEW.campo_c); -- Inserta el nuevo valor que tiene el campo_b (a_tabla) en campo_a (ab_tabla).
	RETURN NEW; -- Regresa los campos que tendrá la tabla modificada, en este caso los nuevos.
END
$$;
```

En `pgAdmin` en `Schemas/public/Trigger Functions` se deberia poder ver la nueva funcion creada. El disparador del trigger es:
```sql
CREATE TRIGGER a_tabla_changes -- Trigger para inserciones en a_tabla.
	BEFORE INSERT -- Realiza el llamado antes de hacer el insert.
	ON a_tabla -- Tabla que al cambiar se llamará el trigger.
	FOR EACH ROW -- Para cada fila define que ejecutar.
	EXECUTE PROCEDURE duplicate_records(); -- Ejecuta la función tipo trigger para copiar los valores a la tabla ab_tabla.
```

## PLPGSQL: Aplicado a data science

```sql
-- 'AVG' nos va a servir para sacar el promedio
-- 'TRUNCATE TABLE' nos ayuda a borrar lo que habia en la tabla para guardar nuevos datos

CREATE OR REPLACE FUNCTION movies_stats()
RETURN VOID
LANGUAGE plpgsql
AS $$
DECLARE -- sirve para declarar las variables
    total_rated_r REAL := 0.0;
    total_large_than_100 REAL := 0.0;
    total_published_2006 REAL := 0.0;
    average_duracion REAL := 0.0;
    average_rental_price REAL := 0.0;
BEGIN
    total_rated_r := COUNT(*) FROM peliculas WHERE clasificacion = 'R';
    total_large_than_100 := COUNT(*) FROM peliculas WHERE duracion >100;
    total_published_2006 := COUNT(*) FROM peliculas WHERE anio_publicacion = 2006;
    average_duracion := AVG(duracion) FROM peliculas;
    average_rental_price := AVG(precio_renta) FROM peliculas;

    TRUNCATE TABLE peliculas_estadisticas;

    INSERT INTO peliculas_estadisticas (tipo_estadisticas, total)
    VALUES 
        ('Peliculas con clasificacion R', total_rated_r),
        ('Peliculas de mas de 100 minutos', total_large_than_100),
        ('Peliculas publicadas en 2006', total_published_2006),
        ('Promedio de duracion en minutos', average_duracion),
        ('Precio promedio de venta', average_rental_price);
END
$$;
```

## Integración con otros lenguajes

**Conectores**

Como la mayoría de las bases de datos, PostgreSQL cuenta con conectores para diferentes lenguajes de programación, de tal forma que si trabajas con Python, PHP, Java, JavaScript y todos sus frameworks, exista una forma de extraer datos de PostgreSQL y posteriormente utilizar las propiedades de los lenguajes procedurales para transformar y utilizar los datos.

El lenguaje estándar utilizado en bases de datos relacionales es SQL (Structured Query Language), un lenguaje que tiene una estructura sumamente útil para hacer solicitudes de datos, en especial tomando como abstracción un diseño tabular de datos. Sin embargo, carece de estructuras de control y otras abstracciones que hacen poderosos a los lenguajes procedurales de programación.

**PL/pgSQL**

Como respuesta a los puntos débiles de SQL como estándar, PostgreSQL respondió originalmente creando un lenguaje propio llamado PL/pgSQL (Procedural Language/PostgreSQL Structured Query Language) que es literalmente un superset de SQL que incluye propiedades de un lenguaje estructurado que, por un lado, nos permite crear funciones complejas y triggers; y, por el otro lado, agrega estructuras de control, cursores, manejo de errores, etc.

**Otros lenguajes**

Sin embargo, en muchos sentidos, aunque PL/pgSQL ayuda en los casos más genéricos para generar estructuras y funcionalidades más complejas, no se compara con lenguajes completamente independientes y no ligados directamente a una base de datos.

La respuesta sin embargo tampoco es los conectores normales que, si bien resuelven la parte de un lenguaje más complejo, añaden por otro lado una separación de la base de datos, ya que debe correr en un servidor separado y hacer llamadas entre ellos con la latencia como un colateral.

Para mitigar estos problemas tomando lo mejor de ambos mundos, los desarrolladores de PostgreSQL se dedicaron a hacer implementaciones de diversos lenguajes a manera de plugin.

- **C**

La biblioteca que permite al lenguaje C ejecutarse en PostgreSQL es llamada [libpq](https://www.postgresql.org/docs/11/libpq.html "libpq") y es una interfaz de programación que permite extender y hacer de interfaz para permitir a otros lenguajes ejecutarse en esta base de datos.

- **PL/Tcl**

[Tcl](https://www.postgresql.org/docs/11/pltcl.html "Tcl") (Tool Command Language) es un lenguaje diseñado con la simpleza en mente y su paradigma consiste en que todo en él es un comando, incluyendo la estructura del lenguaje que, sin embargo, son suficientemente flexibles para poderse sobreescribir, haciéndolo un lenguaje sumamente extensible.

Todo lo anterior es ideal para la integración con el manejador de PostgreSQL ya que permite elaborar comandos para ejecutar las sentencias SQL y extenderlas facilmente.

- **PL/Perl**

[Perl](https://www.postgresql.org/docs/11/plperl.html "Perl") es un lenguaje de programación que implementa una estructura de bloques de código y que toma inspiración de programas como C, sh, AWK, entre otros. Y es especialmente bueno para el tratamiento de cadenas de texto. Sin embargo, no se encuentra limitado como un lenguaje de script.

Dada la propiedad de englobar funcionalidad en forma de bloque y de la rapidez y facilidad con la que trabaja con datos tipo cadena, este lenguaje es ideal para el tratamiento de información de una base de datos relacional.

- **PL/Python**

[Python](https://www.postgresql.org/docs/11/plpython.html "Python"), al ser de los lenguajes de programación más extendidos entre programadores de servicios Backend, es una implementación particularmente interesante para PostgreSQL.

Python es un lenguaje de programación fuerte en tratamiento de estructura de datos y tiene un paradigma múltiple con fuertes componentes orientados a objetos, estructurados y una fuerte influencia del paradigma funcional.

Parte de sus fortalezas son sus implementaciones de funciones map, reduce y filter en conjunto con list comprehensions, sets, diccionarios y generadores.

Dadas las propiedades nativas para manejar estructuras de datos complejas, es un lenguaje ideal para manejar la salida de un query SQL.

La implementación de Python para PostgreSQL te permite crear funciones complejas en un lenguaje completo y popular sin tener que utilizar PL/pgSQL. Puedes ver un ejemplo a continuación de la misma función en PL/pgSQL y PL/Python.

```sql
-- PL/pgSQL
CREATE FUNCTION pgmax (a integer, b integer)
RETURNS integer
AS $$
BEGIN
   IF a > b THEN
       RETURN a;
   ELSE
       RETURN b;
   END IF;
END
$$ LANGUAGE plpgsql;

-- PL/Python
CREATE FUNCTION pymax (a integer, b integer)
RETURNS integer
AS $$
   if a > b:
       return a
   return b
$$ LANGUAGE plpythonu;
 
CREATE EXTENSION plpythonu;
SELECT pgmax(200,9);
```

Para **instalar el lenguaje Python en PostgreSQL**, una vez instaladas las bibliotecas apropiadas para cada Sistema Operativo, es necesario ejecutar el siguiente query:
```sql
CREATE EXTENSION plpythonu
```

## Tipos de Datos Personalizados

**ENUM** sirve para definir una lista de posibbilidades entre las cules se puede elegir, de tal forma si tratamos de seleccionar un dato que no esta ahi no se podra y dara un error como resultado.

Hacer un nuevo tipo de dato:
```sql
-- 'ENUM' es una clase de lista que se puede usar como diccionario
CREATE TYPE humor AS ENUM ('triste', 'normal', 'feliz');

CREATE TABLE persona_prueba(
    nombre text, humor_actual humor
);


INSERT INTO persona_prueba VALUES ('Pablo', 'feliz');
-- si en lugar de feliz ponemos un dato como 'enojado' que no existe entonces dara un error como resultado.
```

## Agregación de datos

La agregacion de datos es el encontrar formas en las que podamos juntar lso datos y sacar  totales para poder entregarse en reportes.

```sql
-- 'MAX' nos ayuda a sacar el maximo de cualquier tabla
-- 'MIN' nos ayuda a sacar el minimo de cualquier tabla
-- Para agrupar los datos usamos 'GROUP BY'
--  Los valores de una tabla los ordenamos con 'ORDER BY'
SELECT titulo, MAX(precio_renta)
FROM peliculas
GROUP BY titulo
ORDER BY MAX(precio_renta) ASC;

-- 'SUM' hace la suma de los valores en una tabla, sirve en la mayoria de ocaciones para suma monetarias.
SELECT SUM(precio_renta)
FROM peliculas;

-- 'COUNT' coonteo
SELECT clasificacion, COUNT(*)
FROM peliculas
GROUP BY clasificacion;

-- 'AVG' se usa para sacar el promedio
SELECT AVG(precio_renta)
FROM peliculas;

SELECT clasificacion, AVG(precio_renta) AS precio_promedio
FROM peliculas
GROUP BY clasificacion
ORDER BY precio_promedio DESC;
```

## Trabajando con objetos

Una caracteristica muy importante de PostgreSQL es su capacidad de trabajar con estructuras JSON.

- JSON Texto plano - Es unicamente un string de texto.
- JSON Binary - Es más rápido de procesar ya que se guarda como un archivo binario. Es una manejo mas eficiente que JSON Texto plano.

El uso de objetos nos dará más flexibilidad en el trabajo.
```sql
-- 'serial' nos ayuda a que el id vaya aumentando de uno en uno para enumerar los valores de la tabla.
-- si queremos trabajar con json binario tenemos que poner 'jsonb'
CREATE TABLE ordenes (
    ID serial NOT NULL PRIMARY KEY,
    info json NOT NULL
);

-- insertamos 'info' para que el id se genere de manera automatica.
INSERT INTO ordenes(info)
VALUES 
    (
        '{"cliente": "David Sanchez", "items": {"producto":"Biberon", "cantidad":"24"}}'
    )
    (
        '{"cliente": "Edna Cardenas", "items": {"producto":"Carro juguete", "cantidad":"1"}}'
    )
    (
        '{"cliente": "Israel Vazquez", "items": {"producto":"Tren juguete", "cantidad":"2"}}'
    )

-- Para extraer datos en formato json;
SELECT
    info -> 'cliente' AS cliente
FROM ordenes;

-- Extraer los datos en formato cadena(string)
SELECT
    info ->> 'cliente' AS cliente
FROM ordenes;


SELECT
    info ->> 'cliente' AS cliente
FROM ordenes
WHERE info -> 'items' ->> 'producto' = 'Biberon';
```

Hacer **operaciones** con tipo de dato json:

```sql
-- 'CAST' lo que hace es transformar un tipo de dato en otro
SELECT 
    MIN(
        CAST(
            info -> 'items' ->> 'cantidad' AS INTEGER
        )
    ),
    MAX(
        CAST(
            info -> 'items' ->> 'cantidad' AS INTEGER
        )
    ),
    SUM(
        CAST(
            info -> 'items' ->> 'cantidad' AS INTEGER
        )
    ),
    AVG(
        CAST(
            info -> 'items' ->> 'cantidad' AS INTEGER
        )
    )
FROM ordenes;

```

## [Common table expressions](https://www.postgresql.org/docs/12/queries-with.html#QUERIES-WITH-SELECT "Common table expressions")

Las **Common table expression** pueden usar para simplificar el código, con ellas puede crear tablas temporales de un query determinado y luego poder hacer un query sobre el resultado final.
por ejemplo generar una tabla resumen y luego hacer un query de esa tabla, de esta forma puede evitar hacer sub-queries o queries anidados que son difíciles de leer.

en la clase se enseño solo una version de las common tables expressions “recursiva”, que hace exactamente lo mismo que lo que dije anteriormente pero en lugar de crear varias tablas temporales, usa los resultados de ella misma hasta que tenga una condición de parada.

```sql
WITH RECURSIVE tabla_recursiva(n) AS (
    VALUES(1)
    UNION ALL
    SELECT n+1 FROM tabla_recursiva WHERE n <100
) SELECT SUM(n) FROM tabla_recursiva;
```

- Es una herramienta que usa expresiones de tablas para agilizar en postgres cálculos en casos de uso específicos.

- Ofrecen una mayor aplicabilidad a casos de usos **iterantes**, casos en los cuales su estructura bajo lenguaje SQL es dispendiosa tanto en su construcción como su ejecución para el servidor.

- Es necesario ahondar más en este tema ya que su versatilidad es interesante.

## [Window functions](https://www.postgresql.org/docs/12/functions-window.html "Window functions")

Las window function se ocupan para entender la **relación que guarda un registro** en particular con respecto al resto del dataset, ya sea una tabla, una partición o un query. Generalmente se encargan de hacer **rankings**.

## Particiones

**Particionado** - Dividir una tabla en segmentos lógicos. Es una practica común de los manejadores, pero no todos ofrecen la opción para los usuarios de administrar estas particiones. Resulta útil para optimizar las consultas de datos.

**Observaciones:**

- No todas las tablas deben de ser particionadas, vale la pena hacerlo unicamente cuando hay muchos registros.
- Permite optimizar algunas consultas al no tener que buscar dentro de toda una tabla sino unicamente en un segmento especifico.
- El particionado altera la consistencia de la tablas
    - No existen los indices (llaves primarias) en las particiones, o mejor dicho, estos indices cambian basándose en la partición. e.g Si particionas una tabla por fechas, al buscar un dato especifico el primer criterio de búsqueda será la fecha
    - En una tabla de usuario o tabla de productos donde es importante tener un ID no es recomendable hacer particiones.


## Presentación del proyecto

### Top 10
Se hara un top 10 peliculas que se an rentado mas

sudo netstat -plunt |grep postgres

