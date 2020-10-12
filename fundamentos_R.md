# Fundamentos de R

## Programación y Data Science

La ciencia de datos es muy útil para cualquier área laboral. Actualmente estamos viviendo la **cuarta revolución industrial** gracias a la masiva cantidad de datos que generamos día a día, las empresas con estos datos buscan satisfacer de mejor forma nuestras necesidades, aquí nace el **Big Data**.

Big Data se compone de tres componentes claves:

- **Volumen**: tiene una cantidad de datos mucho mayor a la soportada dentro de un Excel.
- **Velocidad**: mayor a la acostumbrada con anterioridad.
- **Variedad**: se manejan datos estructurados y no estructurados como fotos, mensajes, etc.

Un científico de datos necesita tener los conocimientos de:

- Matemáticas y estadística.
- Programación.
- Conocimiento del negocio o contexto.
- Habilidad para visualizar los datos y capacidad para comunicarlos.

## R y proyecto economía naranja.

Para la ciencia de datos es común utilizar dos lenguajes: R y Python.
En este curso veremos R, un lenguaje especializado en manejar datos de manera estadística creado en 1993 en la universidad de Auckland Nueva Zelanda.

Se dice que python es mejor para manejar datos no estructurados y que R es mejor para data estructurada.

A lo largo del curso veremos:

- Estructuras, tipos de datos y sintaxis.
- EDA: Exploratory data analysis.
- Estadística descriptiva.
- Ajuste de datos.
- Visualización de datos.
- Organización de información con R Markdown.

**¿Qué es la economía naranja?**

Es donde se mezclan las industrias culturales con las áreas de soporte como el desarrollo de aplicaciones o software.

Buscaremos responder a la pregunta:
Si tienes un startup que hace software, ¿en qué país abrirías una oficina?

El dataset de economía naranja fue creado por la profesora con las siguientes variables:

- Aporte de servicios a PIB.
- Aporte de economía naranja a PIB.
- Penetración de internet.
- Inflación.
- Tasa de desempleo.
- Población debajo de la línea de pobreza.
- Edad mediana de la población.
- Porcentaje de la población entre 25-54 años.
- Inversión en educación %PIB.

## Instalacion 

- [R](https://cran.r-project.org/ "R")
```
apt-get update
apt-get install r-base r-base-dev
apt-get install libatlas3-base
apt-get install libclang-dev
```

- [RStudio](https://rstudio.com/products/rstudio/download/ "RStudio")
```
sudo dpkg -i rst
udio-1.3.1093-amd64.deb
```

- Dataset
```
Country,GDP PC,GDP US bill,GDP Growth %,Services % GDP,Creat Ind % GDP,Inflation,Unemployment,% pop below poverty line,Internet penetration % population,Median age,% pop 25-54,Education invest % GDP
Argentina,20900,637.7,2.9,60.9,3.8,25.7,8.1,25.7,93.1,31.7,39.38,5.9
Belize,8300,1854,0.8,62.2,,1.1,10.1,41,52.3,22.7,36.62,7.4
Bolivia,7500,37.1,4.2,50,,2.8,4,38.6,78.6,24.3,37.48,7.3
Brazil,15600,2055000,1,72.8,2.6,3.4,11.8,4.2,70.7,32,43.86,5.9
Chile,24500,277,1.5,64.3,2.2,2.2,7,14.4,77.5,34.4,43.08,4.9
Colombia,14500,309.2,1.8,61.4,3.3,4.3,10.5,28,63.2,30,41.91,4.5
Costa Rica,16900,58.1,3.2,73.5,2,1.6,8.1,21.7,86.7,31.3,44.03,7.1
Ecuador,11500,102.3,2.7,56.9,2,0.4,4.6,21.5,79.9,27.7,39.59,5
El Salvador,8900,28,2.4,64.9,,1,7,32.7,57.7,27.1,39.23,3.5
Guatemala,8100,75.7,2.8,63.2,,4.4,2.3,59.3,42.1,22.1,34.12,2.8
Honduras,5600,22.9,4.8,57.8,,3.9,5.9,29.6,38.2,23,36.63,5.9
Mexico,19900,1149000,2,64,7.4,6,3.6,46.2,65,28.3,40.81,5.3
Nicaragua,5800,13.7,4.9,50.8,,3.9,6.5,29.6,43,25.7,40.24,4.5
Panama,25400,61.8,5.4,82,6.3,0.9,5.5,23,69.7,29.2,40.35,3.2
Paraguay,9800,29.6,4.3,54.5,4.1,3.6,6.5,22.2,89.6,28.2,41.08,5
Peru,13300,215.2,2.5,56.8,1.5,2.8,6.7,22.7,67.6,28,40.19,3.8
Uruguay,22400,58.4,3.1,68.8,1,6.2,7.3,9.7,88.2,35,39.34,4.4
```

## R y variables

Para **abrir R** escribimos en una terminal de comandos
```
rstudio
```
Ya en R estudio oprimimos las teclas `CTRL + SHIFT + N` para crear un **nuevo script** en R.
En el podemos hacer desde operaciones simples como `4 + 8` y marcamos la operacion y despues oprimimos las teclas `CTRL + ENTER` para que nos muestre el resultado.

Para abrir nuestro **dataset** en R en rstudio presionamos la opcion `File`/`import Dataset`/`From text (base)` y al momento de cargar el dataset eligiendo la opcion “yes” en **heading**.
```r
# otra manera de abrir el dataset es ingresar en la consola de rstudio:

> orangeec <- read.csv("~/Documents/Data Science/orangeec.csv")
> View(orangeec)
```
La función **View** nos muestra nuestro dataset en forma de tabla.

Asignar un valor a una **variable** dentro de R se hace mediante el par de signos <- quedando, por ejemplo:
```r
x <- 10
```

## Tipos de datos

Además de trabajar con el dataset de Orange Economy vamos a necesitar el dataset de **mtcars**.

Dentro de la consola de R Studio, la función install.packages nos va a ayudar a instalar paquetes, como su nombre lo indica, en este caso intentaremos instalar mtcars.

```
install.packages("mtcars")
```
En esta ocacion el paquete no se encuentra en esta version de r asi que este seria el dataset:
```
model,mpg,cyl,disp,hp,drat,wt,qsec,vs,am,gear,carb
Mazda RX4,21,6,160,110,3.9,2.62,16.46,0,1,4,4
Mazda RX4 Wag,21,6,160,110,3.9,2.875,17.02,0,1,4,4
Datsun 710,22.8,4,108,93,3.85,2.32,18.61,1,1,4,1
Hornet 4 Drive,21.4,6,258,110,3.08,3.215,19.44,1,0,3,1
Hornet Sportabout,18.7,8,360,175,3.15,3.44,17.02,0,0,3,2
Valiant,18.1,6,225,105,2.76,3.46,20.22,1,0,3,1
Duster 360,14.3,8,360,245,3.21,3.57,15.84,0,0,3,4
Merc 240D,24.4,4,146.7,62,3.69,3.19,20,1,0,4,2
Merc 230,22.8,4,140.8,95,3.92,3.15,22.9,1,0,4,2
Merc 280,19.2,6,167.6,123,3.92,3.44,18.3,1,0,4,4
Merc 280C,17.8,6,167.6,123,3.92,3.44,18.9,1,0,4,4
Merc 450SE,16.4,8,275.8,180,3.07,4.07,17.4,0,0,3,3
Merc 450SL,17.3,8,275.8,180,3.07,3.73,17.6,0,0,3,3
Merc 450SLC,15.2,8,275.8,180,3.07,3.78,18,0,0,3,3
Cadillac Fleetwood,10.4,8,472,205,2.93,5.25,17.98,0,0,3,4
Lincoln Continental,10.4,8,460,215,3,5.424,17.82,0,0,3,4
Chrysler Imperial,14.7,8,440,230,3.23,5.345,17.42,0,0,3,4
Fiat 128,32.4,4,78.7,66,4.08,2.2,19.47,1,1,4,1
Honda Civic,30.4,4,75.7,52,4.93,1.615,18.52,1,1,4,2
Toyota Corolla,33.9,4,71.1,65,4.22,1.835,19.9,1,1,4,1
Toyota Corona,21.5,4,120.1,97,3.7,2.465,20.01,1,0,3,1
Dodge Challenger,15.5,8,318,150,2.76,3.52,16.87,0,0,3,2
AMC Javelin,15.2,8,304,150,3.15,3.435,17.3,0,0,3,2
Camaro Z28,13.3,8,350,245,3.73,3.84,15.41,0,0,3,4
Pontiac Firebird,19.2,8,400,175,3.08,3.845,17.05,0,0,3,2
Fiat X1-9,27.3,4,79,66,4.08,1.935,18.9,1,1,4,1
Porsche 914-2,26,4,120.3,91,4.43,2.14,16.7,0,1,5,2
Lotus Europa,30.4,4,95.1,113,3.77,1.513,16.9,1,1,5,2
Ford Pantera L,15.8,8,351,264,4.22,3.17,14.5,0,1,5,4
Ferrari Dino,19.7,6,145,175,3.62,2.77,15.5,0,1,5,6
Maserati Bora,15,8,301,335,3.54,3.57,14.6,0,1,5,8
Volvo 142E,21.4,4,121,109,4.11,2.78,18.6,1,1,4,2
```

La función **str** nos va a mostrar la estructura que tiene el dataset que le pasemos. Esto se puede hacer en una hoja de script R:
```r
str(mtcars)
```

Dentro de la consola podemos obtener **más información** sobre nuestro dataset anteponiendo el signo ? quedando `?mtcars`

En el dataset mtcars podemos ver que hay datos de tipo int y num, la diferencia es que num son números con decimal mientras que int son enteros.

Podemos ver que las variables vs y am dentro de mtcars aunque están marcadas con int su función es de tipo boolean, para convertir estos datos utilizaremos la función as.logical

```r
#Clase de la variable vs
class(mtcars$vs)

#Convertir el tipo de la variable
mtcars$vs = as.logical(mtcars$vs)
mtcars$am = as.logical(mtcars$am)
class(mtcars$vs)
class(mtcars$am)
```


**summary**: función que nos va a mostrar un resumen del dataset que le mandemos.
```r
summary(orangeec)
```
**transform**: función para modificar los valores de un dataset.
```r
# esto es para convertir los valores de libas a kilos
# se tiene que crear un nuevo datasets con el cambio que queremos hacer
mtcars.new <- transform(mtcars,wt=wt*1000/2)
```

## Vectores

Un **vector** es un ente matemático que se usa para guardar información de un mismo tipo, dentro de R se crean los vectores con la función c.
```r
tiempo_estudio <- c(25,5,10,15,10)
tiempo_lecturas <- c(30,10,5,10,15)
tiempo_aprendizaje <- tiempo_estudio + tiempo_lecturas
tiempo_aprendizaje

# Vector con caracteres
dias_aprendizaje <- c("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")
dias_aprendizaje

# Vector booleano
dias_mas_20min <- c(TRUE, FALSE,TRUE,FALSE, TRUE)
dias_mas_20min

```

**sum** es una función que como su nombre lo indica, retorna la suma de los valores que le indiquemos.
```r
total_tiempo_lecturas <-sum(tiempo_lecturas)
total_tiempo_lecturas

total_tiempo_estudio <-sum(tiempo_estudio)
total_tiempo_estudio

total_tiempo_adicional <- total_tiempo_lecturas + total_tiempo_estudio

total_tiempo_adicional
```
## Matrices

Una **matriz** debe tener mismo tipo de datos, por otro lado, un **dataframe** puede tener diferentes.
Para crear una matriz en R utilizaremos la función matrix cuyos argumentos son:

la información de los elementos:
- **nrow**: número de filas.
- **ncol**: número de columnas.
- **byrow**: booleano para indicar si llenar la matriz por filas.

```r
tiempo <- matrix(c(tiempo_estudio,tiempo_lecturas), nrow = 2,byrow=TRUE )
```
```r
dias <- c("Lunes", "Martes", "Miercoles", "Jueves", "Viernes")
Tiempo <- c("tiempo_estudio", "tiempo lecturas")
```
```r
colnames(tiempo) <- dias
rownames(tiempo) <- Tiempo

tiempo
```

**colSums** es una función que por argumento recibe una matriz y te retorna la suma de los valores de sus columnas.

```r
colSums(tiempo)
```