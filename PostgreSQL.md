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

- Inicializar el contador de tiempo para que la consola te diga en cada ejecucion cuando temoro en ejecutar esa funcion.
```
\timing
```

- Crear base de datos
```
CREATE DATABASE nombre_de_la_BD;
```

- Cambiar contrase;a de un usuaio de la base de datos
```
ALTER USER postgres PASSWORD 'newPassword';
```

## Archivos de Configuración

- postgresql.conf

- pg_hba.conf

- pg_ident.conf

