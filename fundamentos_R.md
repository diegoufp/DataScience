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
**rbind**: función para añadir una fila.
```r
final_matrix <- rbind(tiempo, c(10,15,30,5,0))
final_matrix
```

**cbind**: funcion para añadir una columna.
```r
final_sabado_matrix <- cbind(final_matrix, Sabado = c(40,20,30))
final_sabado_matrix
```

Identificar los elemenos de la matriz se usa la siguiente sintaxis `nombre_de_la_matriz[final,columna]`:
```
final_sabado_matrix[1,5]
```

## Operadores para comparar y ubicar datos

Operadores| Significado
----------|-------------
`==` | igual
`!=` | No igual (diferente)
`<` | Menor que
`<=` | Menor o igual que
`>` | Mayor que 
`>=` | Mayor o igual que
`!` | No
`%in%` | que este es el dataset
```
| significa o
```

```r
# Despues de que escribimos el signo '$' nos va a mostrar las variables que tenemos
orangeec[oraneec$GDP.PC>=15000,]
```

Para hacer una selección de elementos de un vector, matriz o data frame podemos usar la función `subset`.
```r
neworangeec <- subset(orangeec, Internet.penetration...population > 80 & Education.invest...GDP >= 4.5)
neworangeec
```
```r
# La informacion sobre la penetracion de intener y la ninversion en educacion la queremos ver pero en paises desde la variable de economia naranja.
# el 'select' lo usamos para seleccionar columnas(variables)
neworangeec <- subset(orangeec, Internet.penetration...population > 80 & Education.invest...GDP >= 4.5, select = Creat.Ind...GDP)
neworangeec
```

Podemos **renombrar una variable** de nuestro dataset orangeec, para ello debemos tener instalado el paquete `plyr.` En caso de no tener el paquete instalado solamente corremos en la consola el código `install.packages(“plyr”)`.

```r
rename(oraneec,c("Creat.Ind...GDP"="AporteEcNja"))
```
**Importante**
Para usar `rename` luego de instalar el paquete `plyr` deben cargarlo:
`library(“plyr”)`
ó
en el panel de Packages dar check a la casilla de `plyr`.

## Factores, listas , ver dataset

- **head**: es una función que nos retorna los primeros elementos de un dataset, por defecto nos retorna los primeros 6.
```r
head(mtcars)
# cuando usamos la función head() por defecto devuelve los 6 primeros valores, pero este puede ser configurable añadiendo un parámetro:
head(orangeec, n = 3)
```
- **tail**: función similar a head solamente que esta función nos retorna los últimos elementos.
```r
tail(mtcars)
# para añadimos mas valores
tail(orangeec, n = 2)
```

Además de poder visualizar un dataset con str podemos instalar el paquete **dplyr**: `install.packages(“dplyr”)`. Una vez instalado usamos la función **glimpse**.No olvidar `library(dplyr)`.
```r
# dbl son los numeros con decimales
glimpse(orangeec)
```

Una **lista** es un vector genérico que puede contener objetos de todo tipo, en R para crear una lista solamente debes llamar a la función `list` y pasarle como argumentos los elementos.

Las **listas** son un super objeto que nos permiten almacenar cualquier otro tipo de objetos, nos permite almacenar vectores, matrices, dataframe.

```r
my_vector <- 1:8
my_vector
#  se está indicando que la tabla se arme con 3 columnas, el que la secuencia se ordene por columnas es el método por defecto de R, no obstante, si a esta misma instrucción le agregamos el parámetro byrow = TRUE ahí estamos cambiando el comportamiento por defecto especificando que la secuencia se ordene por filas
my_matrix <- matrix(1:9, ncol=3)
my_matrix

my_df <- mtcars[1:4,]
my_df

my_list <- list(my_vector, my_matrix, my_df)
```

## EDA

**QUÉ ES EDA?**
Por sus siglas EXPLORATORY DATA ANALYSIS, es la visualizaciòn de los datos antes de aplicar las formulas estadísticas

Al momento de tener nuestro dataset es **importante** visualizarlos en alguna grafica antes de enfocarnos en las fórmulas estadísticas.
Pueden suceder casos donde datasets distintos muestran los mismos valores estadísticos, pero sus elementos en una gráfica son totalmente diferentes. Es por ello por lo que es **importante** visualizarlos antes.

El **cuarteto de Anscombe** nos habla de la importancia de visualizarlos en alguna grafica antes de enfocarnos en las fórmulas estadísticas.

## Gráficas de dispersión e histogramas

Existen varios tipos de gráficas para visualizar la información al momento de hacer EDA:

- **Histograma**: sirve para ver la distribución de las frecuencias de una variable, es diferente a la gráfica de barras.
- **Gráfica de dispersión(scatterplot)**: los ejes solamente pueden ser valores numéricos y los puntos no se pueden unir.
- **Box plot**: nos muestra elementos como el mínimo, el máximo, el primer cuartil, la mediana y el tercer cuartil.

## Box Plot

Los 5 puntos clave en estadística descriptiva se pueden visualizar en el box plot:

- Primer cuartil: es el piso de la caja o línea inferior.
- Tercer cuartil: es el techo de la caja o línea superior.
- Mediana: es la línea que se encuentra dentro de la caja.
- Mínimo: la extensión inferior de la caja.
- Máximo: la extensión superior de la caja.

## EDA con dataset proyecto - Gráficas de dispersión.

Para realizar EDA con una **gráfica de dispersión** dentro de R debemos utilizar la función plot, los argumentos que debemos pasarle son:

- la información en el eje X y Y.
- **xlab**: título para el eje x.
- **ylab**: título para el eje y.
- **main**: título de la gráfica.

```r
# EDA SCATTER PLOT MTCARS
plot(mtcars$mpg ~ mtcars$cyl, xlab="cilindros", ylab = "millas por galon", main = "Relacion cilindros y millas por galon")

# EDA SCATTER PLOT MTCARS
plot(mtcars$mpg ~ mtcars$hp, xlab="caballos de fuerza", ylab = "millas por galon", main = "Relacion caballos de fuerza y millas por galon")

# EDA orangeec
plot(orangeec$Unemployment ~ orangeec$Education.invest...GDP, xlab = "Inversion educacion (%PIB", ylab = "Desempleo", main = "Relacion inversion en eduacion y desempleo")

# EDA orangeec
plot(orangeec$GDP.PC ~ orangeec$Creat.Ind...GDP, xlab = "Aporte economia naranja al PIB(%)", ylab = "PIB per capita", main = "Relacion economia naranja y pib per capita")
```

## EDA con histogramas

Para realizar **EDA con un histograma** dentro de R debemos utilizar la función `qplot`, los argumentos que debemos pasarle son:

- la información en el eje X.
- **geom**: describir el tipo de gráfica que se va a imprimir.
- **xlab**: título para el eje x.
- **main**: título de la gráfica.
- **aes** : contenido estético del gráfico. Es decir, la función le dará indicios a ggplot2 sobre cómo dibujar las formas y tamaños
- **fill** : color de barra
- **color** : contorno de barra
- **binwidth** : ancho de barra
- **labs** : etiquetas del eje (x,y)
- **title** : nombre del histograma
- **xlim** : escalas en el eje x
- **theme** : color de fondo

Además, podemos crear histogramas con el paquete ggplot2 para ello debemos `instalarlo: install.packages(“ggplot2”)`.

```r
install.packages("ggplot2")
library(ggplot2)
```
```r
# histograma mtcars qplot
qplot(mtcars$hp, geom="histogram", xlab="caballos de fuerza", main="carros segun caballos de fuerza")

# histograma mtcars ggplot2
# 'aes' es la parte esteticas 
ggplot(mtcars, aes(x=hp))+geom_histogram()+labs(x="Caballos de fuerza", y="Cantidad de carros", title="Caballos de fuerza en carros seleccionados")

# agregando un fondo de color blanco con 'theme'
ggplot(mtcars, aes(x=hp))+geom_histogram()+labs(x="Caballos de fuerza", y="Cantidad de carros", title="Caballos de fuerza en carros seleccionados")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())

# modificando el grosor de la barra con 'binwidth'
ggplot(mtcars, aes(x=hp))+geom_histogram(binwidth = 30)+labs(x="Caballos de fuerza", y="Cantidad de carros", title="Caballos de fuerza en carros seleccionados")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())

# cambiar barras de color 
ggplot()+geom_histogram(data=mtcars, aes(x=hp), fill="blue", color="red", binwidth=20)+labs(x="Caballos de fuerza", y="Cantidad de carros", title="Caballos de fuerza en carros seleccionados")+xlim(c(80,280))+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())
```
```r
# histograma de orangeec
ggplot()+geom_histogram(data=orangeec, aes(x=GDP.PC), fill="blue", color="red", binwidth=2000)+labs(x="PIB per capita", y="Cantidad de paises", title="PIB per capita en paises latam")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())


# hist orangeec Contribucion economia naranja
ggplot()+geom_histogram(data=orangeec, aes(x=Creat.Ind...GDP), fill="blue", color="red", binwidth=1)+labs(x="Aporte economia naranja en PIB(%)", y="Cantidad de paises", title="Contribucion economia naranja al pib en paises latam")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())

# hist orangeec Penetracion de internet
ggplot()+geom_histogram(data=orangeec, aes(x=Internet.penetration...population), fill="red", color="yellow", binwidth=5)+labs(x="Penetracion internet (%)poblacion", y="Cantidad de paises", title="Penetracion de internet en paises latam")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())

# Para boder pones los labels a las barras se necesita agrega el siguiente codigo 
scale_x_continuous(breaks = seq(40, max(100), 5))
#y quedaria asi:
ggplot()+geom_histogram(data=orangeec, aes(x=Internet.penetration...population), fill="red", color="yellow", binwidth=5)+scale_x_continuous(breaks = seq(40, max(100), 5))+labs(x="Penetracion internet (%)poblacion", y="Cantidad de paises", title="Penetracion de internet en paises latam")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())

```

## EDA con box plot- ggplot2

Para realizar **EDA con un box plot** dentro de R debemos utilizar la función boxplot, los argumentos que debemos pasarle son:

- la información que vamos a explorar.
- **ylab**: título para el eje y.
- **main**: título de la gráfica.
- **as.factor()** : para indicar que el numero es una categoria. Se paso de ver con error la grafica a ver las tres categorias de 4, 6 y 8 cilindros en cada boxplot correspondiente
También podemos usar ggplot2 para crear un Box Plot.
- **alpha**:  para cambiar el color de un boxplot en la grafica.Se cambio un azul oscuro por un gris para ver la linea de la media.
```r
# boxplot
boxplot(mtcars$hp, ylab="caballos de fuerza", main="caballos de fuerza en carros mtcars")

# boxplot con ggplot2
ggplot(mtcars,aes(x=cyl,y=hp,fill=cyl))+geom_boxplot()+labs(x="cilindros", y="caballos de fuerza", title="caballos de fuerza segun cilindros en mtcars")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())
# si ejecutamos el codigo anterior ocurrira un error por que es necesario agrupar la variable. Ya que es numerica y es necesario cambiarlo a factor o etiqueta.
ggplot(mtcars,aes(x=as.factor(cyl),y=hp,fill=cyl))+geom_boxplot()+labs(x="cilindros", y="caballos de fuerza", title="caballos de fuerza segun cilindros en mtcars")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())

# si ocurre un error de icompatibilidad usar el comando 'dev.off()' en la consola de rstudio.
dev.off()

# cambiar el color de los box
ggplot(mtcars,aes(x=as.factor(cyl),y=hp,fill=cyl))+geom_boxplot(alpha=0.6)+labs(x="cilindros", y="caballos de fuerza", title="caballos de fuerza segun cilindros en mtcars")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())

#
ggplot(mtcars, aes(x=as.factor(am), y=mpg, fill=am))+geom_boxplot()+labs(x="Tipo de caja", y="millas por galon", title="Millas por galon segun tipo de caja-mtcars")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())

## si queremos que los valores de 0 y 1 cambien podemos usar el siguiente codigo:
mtcars$am <- factor(mtcars$am, levels = c(1,0), labels = c("manual","automatico"))
# y ahora probamos nuevamnet el codigo del boxplot para observar el cambio
ggplot(mtcars, aes(x=as.factor(am), y=mpg, fill=am))+geom_boxplot()+labs(x="Tipo de caja", y="millas por galon", title="Millas por galon segun tipo de caja-mtcars")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())
```

Al tratar de hacer un boxplot de economia naranja nos topamos con el inconveniente de que las unas etiquetas con las que contamos en este dataset con las etiquetas de los paises y que lo demas datos son numeros asi que no se podria hacer ningun cruce para hacer el boxplot, no podemos hacer un boxplot para cada pais. Boxplot nos cruza una **variable categotica** o etiquetas **con numeros**.

Para resolver esta problematica se hara una clasificacion de paises segun el pib per capita por cada pais(cuales estan por ensema del promedio y cuales estan por debajo)

```r
# para ver el promedio del pib per capita
economy <- mean(orangeec$GDP.PC)
economy

# Despues usaremos el paquete dplyr, se instala con 'install.packages("dplyr")' y cuando lo hayamos instalado solamente usamos el comando para activar la libreria
library(dplyr)
```
**CREAR UNA NUEVA VARIABLE CATEGORICA**

Esta variable se crea usando la variable numerica declarada en el **PASO 1**

- `%>%` : significa que 'va a pasar a'

- **mutate**: viene porque ese dataset va a cambiar, se va agrandar, va a mutar 

- **ifelse**: significa que la nueva variable sera si otra variable del dataset es > menor a la declarada en el 

```r
# CREAR UNA NUEVA VARIABLE CATEGORICA
orangeec <- orangeec %>% mutate(Strong_economy = ifelse(GDP.PC < economy, "Por debajo del promedio pib per capita", "Sobre promedio pib per capita"))
# despues de correr el codigo vamos a poder ver una nueva variable en el dataset
```

```r
# box plot de economia naranja
ggplot(orangeec, aes(x=Strong_economy, y=Creat.Ind...GDP, fill=Strong_economy))+geom_boxplot(alpha=0.4)+labs(x="Tipo de pais", y="Aporte economia naranja al pib", title="Aporte economia naranja en pid paises latam con alto y bajo pib per capita")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())

# box plot de economia naranja penetracion de internet
ggplot(orangeec, aes(x=Strong_economy, y=Internet.penetration...population, fill=Strong_economy))+geom_boxplot(alpha=0.4)+labs(x="Tipo de pais", y="penetracion de internet", title="Penetracion de internet en paises latam con alto y bajo pib per capita")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())
```

## EDA con gráficas de dispersión con más de dos variables - ggplot2

```r
# scatter plot con ggplot en mtcars - dos variables
ggplot(mtcars, aes(hp, mpg))+geom_point()+labs(x="caballos fuerza", y="millas por galon", title="Relacion caballos de fuerza y millas por galon")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())

# scatter plot de Relacion peso-potencia
ggplot(mtcars, aes(wt, hp))+geom_point()+labs(x="peso", y="potencia", title="Relacion peso-potencia")+theme(legend.position = "none")+theme(panel.background = element_blank(),panel.grid.major = element_blank(), panel.grid.minor = element_blank())

# scatter plot con ggplot en mtcars - cuatro variables
ggplot(mtcars, aes(hp, qsec))+geom_point(aes(color=am,size=cyl))+labs(x="caballos fuerza", y="tiempo en 1/4 de milla", title="Caballos-verlocidad segun cilindraje y tipo de caja")+theme(legend.position = "none")

# Internet y aporte economia
ggplot(orangeec, aes(Internet.penetration...population,Creat.Ind...GDP))+geom_point(aes(color=factor(Strong_economy),size=GDP.Growth..))+labs(x="Penetracion Internet", y="Aporte economia naranja PIB", title="Internet y aporte economia naranja segun economia y crecimiento pib")

# Relaciòn entre inversion en educacion y desempleo
# En el eje x se encuentra la inversiòn en educaciòn como porcentaje % del PIB como Education.invest…GDP
#El tamaño de cada esfera depende del porcentaje % de la poblacion que esta por debajo de la linea de pobreza se ve con la etiqueta X…pop.below.poverty.line
En el eje y esta el desempleo como Unemployment
ggplot(orangeec, aes(Education.invest...GDP,Unemployment))+geom_point(aes(color=factor(Strong_economy),size=X..pop.below.poverty.line))+labs(x="Inversion en educacion", y="Desempleo", title="Relacion entre inversion en educacion y desempleo segun el % de la poblacion que esta por debajo de la linea de pobreza")
```

**SCATTER PLOT INTERACTIVO**

Para crear un scatter plot interactivo se hara uno de el paquete `plotly` con el comando `install.packages("plotly")` y despues usamos la libreria con el comando `library(plotly)`. Si llega a tener un error y no se descarga `plotly` intenta descargando las siguientes dependencias:
```
sudo apt-get install libssl-dev
sudo apt-get install libcurl4-openssl-dev
sudo apt-get install libssh2-1-dev
sudo apt-get install libpq-dev
sudo apt-get install zlib1g-dev
```
```r
# SCATTER PLOT INTERACTIVO
my_graph <- ggplot(orangeec, aes(Internet.penetration...population, Creat.Ind...GDP, label=row.names(orangeec)))+geom_point()+labs(x="Penetracion de internet", y="Aporte economia naranja", title="Penetracion Internet y aporte economia naranja")
my_graph
p <- ggplotly(my_graph)
p
```