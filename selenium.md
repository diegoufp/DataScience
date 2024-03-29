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

Selenium WebDriver nos brinda la posibilidad de poder referirnos a estos elementos y ejecutar métodos específicos para realizar las mismas acciones que un humano haría sobre los mismos, gracias a las clases WebDriver y WebElement.

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
Para responder esta pregunta se tienen que tomar en cuenta factores como el lenguaje de programacion que conoces tu y tu equipo de trabajo, el proyecto en el que se va a trabajar, si require de grandes llamadas de asincronismo o no, si solo quieres automatizar una tarea que es repetitiva, etc.

## Instalacion 

```
sudo apt update
apt install python3-pip
pip3 --version
pip3 install selenium
pip3 install pyunitreport
```
## WebDriver y WebElement 

### Clase WebDriver

Cuenta con una serie de propiedades y métodos para interactuar directamente con la ventana del navegador y sus elementos relacionados, como son pop-ups o alerts. Por ahora nos centraremos a las más utilizadas.

- Propiedades de la clase WebDriver

Estas son las más comunes para acceder al navegador.

Propiedad/Atributo | Descripción | Ejemplo
-------------------|-------------|---------
current_url | Obtiene la URL del sitio en la que se encuentra el navegador | driver.get_url
current_window_handle | Obtiene la referencia que identifica a la ventana activa en ese momento | driver.current_window_handle
name | Obtiene el nombre del navegador subyacente para la instancia activa | driver.name
orientation | Obtiene la orientación actual del dispositivo móvil | driver.orientation
page_source | Obtiene el código fuente de disponible del sitio web | driver.page_source
title | Obtiene el valor de la etiqueta `<title>` del sitio web | driver.title

- Metodos de la clase WebDriver
Estas son las mas comunes para interactuar con la ventana del navegador , los sitios web y elementos de los sitios.

Metodo/Atributo | Descripcion | Ejemplo
----------------|-------------|-----------
back() | Va una pagina atras en el historial de navegacion de la sesion actual | driver.back()
close() | Cierra la ventana actual | driver.close()
forward() | Va una pagina adelante en el historial de navegacion de la sesion actual | driver.forward()
get(url) | Navega hacia y carga la url indicada | driver.get('https://www.platzi.com')
maximize_window() | Maximiza la ventana del navegador | driver.maximize_window()
quit() | Cierra el driver de navegacion y todas las ventanas asociadas al mismo | driver.quit()
refresh() | Actualiza el sitio mostrado por el navegador en ese momento | driver.refresh()
switch_to.active_element() | Retorna el elemento donde se encuentra el focus del navegador | dirver.switch_to.active_element()
switch_to_alert() | Cambia el focus del navegador al alert de JS que se este mostrando | driver.switch_to_alert()

### Clase WebElement

Esta clase nos permite interactuar específicamente con elementos de los sitios web como textbox, text area, button, radio button, checkbox, etc.

- Propiedades más comunes de la clase WebElement

Propiedad/Atributo | Descripción | Ejemplo
-------------------|-------------|----------
size | Obtiene el tamaño del elemento | login.size
tag_name | Obtiene el nombre de la etiqueta HTML del elemento| login.tag_name
text | Obtiene el texto del elemento | login.text

- Métodos más comunes de la clase WebElement

Método/Atributo | Descripción | Ejemplo
----------------|-------------|---------
clear() | Limpia el contenido de un textarea | first_name.clear()
click() | Hace clic en el elemento | send_button.click()
get_attribute(name) | Obtiene el valor del atributo de un elemento | submit_button.get_attribute(‘value’) last_name.get_attribute(max_length)
is_displayed() | Verifica si el elemento está a la vista al usuario | banner.is_displayed()
is_enabled() | Verifica si el elemento está habilitado | radio_button.is_enabled()
is_selected() | Verifica si el elemento está seleccionado, para el caso de checkbox o radio button | checkbox.is_selected()
send_keys(value) | Simula escribir o presionar teclas en un elemento | email_field.send_keys(`‘team@platzi.com’`)
submit() | Envía un formulario o confirmación en un text area | search_field.submit()
value_of_css_property(property_name) | Obtiene el valor de una propiedad CSS del elemento | header.value_of_css_property(‘background-color’)

## Condicionales esperadas 

Expected Condition | Descripcion | Ejemplo
-------------------|-------------|-----------
element_to_be_clickable(locator) | Espera a que el elemento sea visible y habilitado para hacer clic en el mismo | WebDriverWait(self.driver, 10).until(espected_conditions.element_to_be_clickable(By.NAME, "accept_button"))
elemte_to_be_selected(element) | Espera a que un elemento sea seleccionado | subscription = self.driver.find_element_by_name('terms') WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_selected(terms))
invisibility_of_element_located(locator) | Espera a que un elemento no sea visible o no se encuentre presente en el DOM | WebDriverWait(self.driver, 10).until(expected_conditions.invisibility_of_element_located(By.ID, "loading_banner"))
presence_of_all_elements_located(locator) | Espera a que por lo menos uno de los elementos que se indican coincida con los presentes en el sitio | WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_all_elements_located(By.CLASS_NAME, "input-text"))
presence_of_element_located(locator) | Espera a que un elemento sea visible se encuentre presente en el DOM | WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(By.ID, "search-bar"))
text_to_be_present_in_element(locator, text) | Espera a que un elemento con texto indicado se encuentre presente | WebDriverWait(self.driver, 10).until(expected_conditions.text_to_be_present_in_element(By.ID, "select_order"), "high")
title_contains(title) | Espera a que la pagina contenga en el titulo exactamente como es indicado | WebDriverWait(self.driver, 10).until(expected_conditions.title_contains("Welcome"))
title_is(tile) | Espera a que la pagina tenga un titulo identico a como es indicado | WebDriverWait(self.driver, 10).until(expected_conditions.title_is("Welcome_to_Platzi"))
visibility_of(element) | Espera a que el elemento indicado este en el DOM, sea visible, su alto y ancho sean mayores a cero | first_name = self.driver.find_element_by_id("firstname") WebDriverWait(self.driver,10).until(expected_conditions.visibility_of(first_name))
visibility_of_element_located(locator) | Espera a que el elemento indicado por su selector este en el DOM, sea visible y que su alto y ancho sean mayores a cero | WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(By.ID, "firstname"))

## Conceptos

### Unittest (PyTest)
Una libreria de python con la cual vamos a realizar pruebas unitarias para obtener la informacion de lo que ocurre con nuestras automatizaciones. En otras palabras va a preparar el entorno de nuestra automatizacion y despues realizara una serie de acciones para cuando termine el caso de prueba que se esta realizando.

**El caso de prueba** Es una unidad de codigo con el cual estaremos indicando a selenium que queremos que haga o en su defecto alguna funcion que queramos probar.

- **Test Fixture**: preparaciones para antes y despues de la prueba.
- **Test Case**: unidad de codigo a provar.
- **Test Suite**: coleccion de Test Cases.
- **Test Runner**: orquestador de la ejecucion.
- **Test Report**: resumen de resultados.

## Caso de prueba

- Codigo base

```python
import unittest
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main(verbosity = 2)
```
 
- codigo de prueba

```python
# <- nos servira para traer todas nuestras pruebas
import unittest
# <- Nos ayudara a orquestar cada una de nuestra pruebas que estemos ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner 
#  Para comunicarnos con el navegador
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    # Debe ser asi tal y como indica la sintaxis
    def setUp(self): # va a ejecutar todo lo necesario antes de hacer un prueba(unittest)
        self.driver = webdriver.Chrome(executable_path= r'./chromedriver') # en windows es r'c://Documents/selenium/chromedriver.exe
        driver = self.driver
        driver.implicitly_wait(10) #Tiempo de espera

    def test_hello_word(self): # <- caso de prueba
        driver = self.driver
        driver.get('https://www.platzi.com')


    def tearDown(self): # Dara salida a lo que estes escribiendo
        self.driver.quit() # <- se vana cerrar las ventanas cuando se hagan las pruebas

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
    # Lo que va ahacer este script es abrir el navegador y direccionar ala pagina de platzi y despues cerrara la ventana.
```

- Para que se visite los 2 sitios sin cerrar completamente el navegador.

```python
# <- nos servira para traer todas nuestras pruebas
import unittest
# <- Nos ayudara a orquestar cada una de nuestra pruebas que estemos ejecutando junto con los reportes
from pyunitreport import HTMLTestRunner 
#  Para comunicarnos con el navegador
from selenium import webdriver

class HelloWorld(unittest.TestCase):
    # Debe ser asi tal y como indica la sintaxis
    @classmethod #<- para que no se cierren las ventanas y se corran los dos en una sola
    def setUpClass(cls): # va a ejecutar todo lo necesario antes de hacer un prueba(unittest)
        cls.driver = webdriver.Chrome(executable_path= r'./chromedriver') # en windows es r'c://Documents/selenium/chromedriver.exe
        driver = cls.driver
        driver.implicitly_wait(10) #Tiempo de espera

    def test_hello_word(self): # <- caso de prueba
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_hello_world(self):
        self.driver.get('https://es.wikipedia.org/wiki/Wikipedia:Portada')

    @classmethod
    def tearDownClass(cls): # Dara salida a lo que estes escribiendo
        cls.driver.quit() # <- se vana cerrar las ventanas cuando se hagan las pruebas

if __name__ == "__main__":
    unittest.main(verbosity = 2, testRunner = HTMLTestRunner(output = 'reportes', report_name = 'hello-world-report'))
    # Lo que va ahacer este script es abrir el navegador y direccionar ala pagina de platzi y despues cerrara la ventana.
```

## Encontrar elementos

Un sitio web se compone de codigo **HTML** el cual puede tener un head y un body y estos asu vez van a tener por dentro etiquetas con los cuales puedes interactuar atravez de los **selectores**.

- **Selectores**
    - ID
    - Nombre del atributo
    - Nombre de la clase
    - Nombre de la etiqueta
    - XPath: Es una ruta de nodos en el xml que nos indica la ubicaciones exacta de donde se encuentra un elemento.
    - Selectores de CSS
    - Texto del link
    - Texto parcial del link

### find_element
- **find_element_by_id(id)**
    - Encuentra un elemento por el valor de su ID

- **find_element_by_name(name)**
    - Encuentra un elemento por el valor de su nombre (name)

- **find_element_by_class_name(class)**
    - Encuentra un elemento por el valor del nombre de su clase (class)

- **find_element_by_tag_name(name)**
    - Encuentra un elemento por el valor del nombre de su etiqueta HTML (tag)

- **find_element_by_xpath(xpath)**
    - Encuentra un elemento utilizado XPath, mediante su correspondiente ruta de nodos de XML

- **find_element_by_css_selector(css_selector)**
    - Encuentra un elemento por su selector CSS

- **find_element_by_link_text(link_text)**
    - Encuentra un elemento por su texto en el hipervinculo, debe ser identico

- **find_element_by_partial_link_text(link_text)**
    - Encuentra un elemento por una parte de su testo en el hipervinculo


### Prueba de Selectores

```python
import unittest
from selenium import webdriver

class HomePageTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        driver.get('https://demo.cart2quote.com/')
        driver.maximize_window() # Maximise la ventana por si hay elementos que cambien su ubicacion u orden dependiendo del tamaño de la vista.
        driver.implicitly_wait(15) # añadir una pausa de 15 segundos

    def test_search_text_field(self):
        # find_element <- va a entontrar al elemento (en este caso por su id)
        search_field = self.driver.find_element_by_id('search')
    
    def test_search_text_field_by_name(self):
        search_field = self.driver.find_element_by_name("q")

    def test_search_text_field_class_name(self):
        search_field = self.driver.find_element_by_class_name("input-text")

    def test_search_button_enabled(self):
        botton = self.driver.find_element_by_class_name('button')

    def test_count_of_promo_banner_images(self):
        banner_list = self.driver.find_element_by_class_name("promos")
        banners =  banner_list.find_elements_by_tag_name('img')
        #los asesertion son validaciones que hacemos en el codigo para verificar que una condicion se cumpla o no.
        self.assertEqual(3, len(banners)) #Seran 3 imagenes deacuerdo a la longitud de la variable banners

    def test_vip_promo(self):
    # XPath no ayuda a identificar elementos cuando no hay algo que es lo suficientemente explicito
        vip_promo = self.driver.find_element_by_xpath('/html/body/div/div[2]/header/div/a/img[1]')
        # El xpath puede aveces no ser la mejor opcion por que un sitio web puede cambiar

    def test_shopping_cart(self):
    # identificar elementos con su selector de css
        shopping_cart_icon = self.driver.find_element_by_css_selector('div.header-minicart span.icon')


    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
```

## assertions y test suites

- **Assertions**: Metodos que permiten validar el valor esperado en la ejecucion del test. Si el resultado es verdadero el test continua, en caso contrario "falla" y termina.
    - **Ejemplo**: assertEqual(price.text, "300")

- **Test suites**: Coleccion de test unificados en una sola prueba, permitiendo tener resultados grupales e individuales. 

### Metodos 

**Metodo** | **Condicion que verifica** | **Ejemplo** 
-----------|----------------------------|-------------
assertEqual(a,b) | a == b | Verifica que 'a' y 'b' sean iguales. Util para verificar valores, por ejemplo: assertEqual(element.text, "100") 
assertNoEqual(a,b) | a != b | Verifica que 'a' y 'b' sean diferentes. Util para verificar valores, por ejemplo: assertNotEqual(element.text, "100") 
assertTrue(x) | bool(x) is True | Verifica que la expresion evaluada tenga como resultado 'True' o 'False'. Por ejemplo, que un elemento se este mostrando, activo o disponible para interactuar: assertTrue(element.is_dispalyed()) 
assertFalse(x) | bool(x) is False | Verifica que la expresion evaluada tenga como resultado 'True' o 'False'. Por ejemplo, que un elemento se este mostrando, activo o disponible para interactuar: assertFalse(element.is_dispalyed()) 
assertNot(x) | a is a not b | Verifica que la expresion evaluada tenga como resultado 'True' o 'False'. Por ejemplo, que un elemento se este mostrando, activo o disponible para interactuar: assertNot(element.is_dispalyed()) 
assertAlmostEqual(a, b) | round(a-b, 7) == 0 | Estos metodos verifican especificamente valores numericos y redondean su valor para buscar igualdad. Utiles al validar resultados con numeros flotantes
assertNotAlmostEqual(a, b) | round(a-b, 7) != 0 | Estos metodos verifican especificamente valores numericos y redondean su valor para buscar igualdad. Utiles al validar resultados con numeros flotantes
assertGreater(a, b) | a > b | Funcionan igual que assertEqual, pero con condiciones logicas de comparacion
assertGreaterEqual(a, b) | a >= b | Funcionan igual que assertEqual, pero con condiciones logicas de comparacion
assertLess(a, b) | a < b | Funcionan igual que assertEqual, pero con condiciones logicas de comparacion
assertLessEqual(a, b) | a <= b | Funcionan igual que assertEqual, pero con condiciones logicas de comparacion
assertRegexpMatches(s, r) | r.search(s) | Verifica si la busqueda de una expresion regular coincide con el string indicado
assertNotRegexpMatches(s, r) | not.r.search(s) | Verifica si la busqueda de una expresion regular coincide con el string indicado
asserListEqual(a, b) | assertListEqual(lista_a, lista_b) | Valida que los elementos de las listas coinciden. Util para validar las opciones de un dropdown
fail() || Hace fallar una prueba incondicionalmente.

### prueba de assertions y tests suites

- archivo donde esta el test suites

```python
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtests import SearchTests

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    "output": 'smoke-repot'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)
```
------------

- El archivos assertions.py

```python
import unittest
from selenium import webdriver
# Nos servira como una excepcion para nuestros assertions cuando queramos validar la presencia de un elemento
from selenium.common.exceptions import NoSuchElementException
# Nos ayudara a llamar a las excepciones que queremos validar.
from selenium.webdriver.common.by import By 

class AssertionsTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30) # añadir una pausa de 30 segundos
        driver.maximize_window() # Maximise la ventana por si hay elementos que cambien su ubicacion u orden dependiendo del tamaño de la vista.
        driver.get('https://demo.cart2quote.com/')

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_search_option(self):
        self.assertTrue(self.is_element_present(By.ID, 'search'))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
    # Es una fguncion de utilidad para identificar cuando un elemento esta presente de acuerdo a los paramentros.
        # how nos va a indicar el tipo de selector
        # what el valor que tienen
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == "__main__":
    unittest.main(verbosity = 2)
```
------------

- El archivo searchtests.py

```python
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 

class SearchTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30) # añadir una pausa de 30 segundos
        driver.maximize_window() # Maximise la ventana por si hay elementos que cambien su ubicacion u orden dependiendo del tamaño de la vista.
        driver.get('https://demo.cart2quote.com/')

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        # Va a limpiar el campo de busqueda en dado caso que haya algun texto
        search_field.clear()
        # En viar una serie de teclas con send_keys
        search_field.send_keys('tee')
        # submit <- que envia los datos
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        # Es send_keys no send_key
        search_field.send_keys('salt shaker')
        search_field.submit()
        # find_element != find_elements
        products = driver.find_elements_by_xpath('/html/body/div/div[2]/div[2]/div/div[2]/div[2]/div[2]/ul/li[2]/a')
        # La forma rapida de obtener la lista delos elementos es atravez del xpath
        # el assert va a identificar si la cantidad de productos es una o no
        self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
```

## for, textbox, checkbox y radio button

En este tema automatizaremos todo el proceso de la creacion de una nueva cuenta dentro del sitio.

Con esto podremos crear automatizaciones para interactuar con campos de texto botones y checks box para amrcarlos, esto en conjunto con los assertions nos permite validar que la automatizacion esta funcionando, que elementos estan disponibles y visibles para el usuario.

### Pruebas 

```python
import unittest
from selenium import webdriver 

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30) # añadir una pausa de 30 segundos
        driver.maximize_window() # Maximise la ventana por si hay elementos que cambien su ubicacion u orden dependiendo del tamaño de la vista.
        driver.get('https://demo.cart2quote.com/')

    def test_new_user(self):
        driver = self.driver
        s = driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]') # se hara un click para que se despliegen las opciones
        s.click()
        m = driver.find_element_by_link_text('Log In')
        m.click()

        create_account_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/form/div/div[1]/div[2]/a/span/span')
        # Vamos a validar que ese boton este habilitado con un assertion (que este visible al usuario y se pueda interactuar con el)
        self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())
        create_account_button.click()
        # para verificar si estamos en la pagina correcta    
        self.assertEqual('Create New Customer Account', driver.title)

        first_name = driver.find_element_by_id('firstname')
        last_name = driver.find_element_by_id('lastname')
        email_address = driver.find_element_by_id('email_address')
        news_letter_subscription = driver.find_element_by_id('is_subscribed')
        password = driver.find_element_by_id('password')
        confirm_password = driver.find_element_by_id('confirmation')
        submit_button = driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/div/div/form/div[2]/button')
        # para verificar que esten habilitados con assert
        self.assertTrue(first_name.is_enabled()
        and last_name.is_enabled()
        and email_address.is_enabled()
        and news_letter_subscription.is_enabled()
        and password.is_enabled()
        and confirm_password.is_enabled()
        and submit_button.is_enabled())
        # Para enviar datos a cada una de estas variables con send_keys
        first_name.send_keys('Test')
        driver.implicitly_wait(1) # pausa de 1 segundo
        last_name.send_keys('Test')
        driver.implicitly_wait(1)
        email_address.send_keys('Test@gmail.com')
        driver.implicitly_wait(1)
        password.send_keys('Test')
        driver.implicitly_wait(1)
        confirm_password.send_keys('Test')
        driver.implicitly_wait(1)
        submit_button.click()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main(verbosity = 2)
```

## Dropdown y listas

Interactuar con Dropdown y listas 

```python
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select # Para poder manipular un drop down

class LanguageOptions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        driver.implicitly_wait(30) # añadir una pausa de 30 segundos
        driver.maximize_window() # Maximise la ventana por si hay elementos que cambien su ubicacion u orden dependiendo del tamaño de la vista.
        driver.get('https://demo.cart2quote.com/')

    def test_select_language(self):
        exp_options = ['English', 'French', 'German']
        act_options = [] # Aqui se almacenaran las opciones que elijamos
        # Pra acceder a las opciones del drop down
        select_language = Select(self.driver.find_element_by_id('select-language'))
        # Validar que el drop down tenga 3 opciones
        self.assertEqual(3, len(select_language.options))
        # iterar por cada opcion que tenga el drop down
        for option in select_language.options:
            act_options.append(option.text)
        # conparar listas con assertListEqual
        self.assertListEqual(exp_options, act_options)
        # Verificar si el idioma ingles esta por defecto
        self.assertEqual('English', select_language.first_selected_option.text)
        # Ahora seleccionaremos un idioma
        select_language.select_by_visible_text('German')
        # Verificar que se cambio a aleman 
        self.assertTrue('store=german' in self.driver.current_url)

        select_language = Select(self.driver.find_element_by_id('select-language'))
        select_language.select_by_index(0) # valor 0 para que vuelva a ingles
    
    def tearDown(self):
        self.driver.implicitly_wait(3)

if __name__ == "__main__":
    unittest.main(verbosity = 2)
```

## Clase Select

### Propiedades

Propiedad/Atributo | Descripcion | Ejemplo
-------------------|-------------|----------
all_selected_options | Obtiene una lista de todas las opciones seleccionadas que pertenecen al dropdown o list | select_element.all_selected_options
first_selected_option | Obtiene el primer elemento seleccionado o el elemento actualmente seleccionado de un dropdown o lista | select_element.first_selected_option
options | Obtiene una lista de todas las opciones disponibles del dropdown o lista | select_element.options

### Metodos

Metodo/Atributo | Descripcion | Ejemplo
----------------|-------------|------------
deselect_all() | Limpia todas las opciones seleccionadas de un dropdown o lista de seleccion multiple | select_elemet.deselect_all()
deselect_by_index(index) | Deselecciona la opcion en el indice dado del dropdown o lista | select_element.deselect_by_index(1)
deselect_by_value(value) | Deselecciona todas las opciones que coincidan con el valor del argumento dado en el dropdown o lista | select_element.deselect_by_value('gratis')
deselect_by_visible_text(text) | Deselecciona todas las opciones que coincidan con el texto del argumento dado en el dropdown o lista | select_element.deselect_by_visible_text('gratis')
select_by_index(index) | Selecciona las opciones en el indice indicado del dropdown o lista) | select_element.select_by_index
select_by_value(value) | Selecciona todas las opciones que coincidan con el valor del argumento dado en el dropdown o lista | select_element.select_by_value('gratis')
select_by_visible_text(text) | Selecciona todas las opciones que coincidan con el texto del argumento dado en el dropdown o lista | select_element.select_by_visible_text('gratis')


## alert y pop-up

### Metodos de la clase Alert

Metodo/Atributo | Descripcion | Ejemplo
----------------|-------------|----------
accept() | Acepta el mensaje enviado por alert haciando clic en el boton 'Aceptar' | alert.accept()
dismiss() | Rechaza el mensaje enviado por el alert, haciendo clic en el boton 'Cancelar' | alert.dismiss()
send_keys(value) | Simula escibir o presionar teclas en un elemento | alert.send_keys('Platzi')

### Prueba de alert

```python
import unittest
from selenium import webdriver

class CompareProducts(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        driver.implicitly_wait(200) # añadir una pausa de 30 segundos
        driver.maximize_window() # Maximise la ventana por si hay elementos que cambien su ubicacion u orden dependiendo del tamaño de la vista.
        driver.get('https://demo.cart2quote.com/')
    
    def test_compare_products_renoval_alert(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        # como una buena practica siempre debemos de limpiar el texto que haya en la area de busqueda
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

        drvier.find_elemento_by_class_name('link-compare').click()
        driver.find_element_by_link_text('Clear All').click()

        # Interactuar con el alert
        alert = driver.switch_to_alert() # Cambiar la atencion del navegador se encuente en el aler
        alert_text = alert.text # Extraer el texto que muestra
        # Para aregurarnos de que el texto que muestra es el mismo que el de la variable usaremos assert
        self.assertEqual('Are you sure you would link to remove all products from your comparison?', alert_text)
        # simular un click en el boton aceptar del alert.
        alert.accept()


    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity = 2)
```

## Automatizar navegacion

[**Propiedades de WebDriver y WebElement**](https://github.com/diegoufp/DataScience/blob/master/selenium.md#webdriver-y-webelement "Propiedades de WebDriver y WebElement")

### prueba automatizar navegacion

```python
import unittest
from selenium import webdriver
#from time import sleep
class NavigationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        driver.implicitly_wait(200) # añadir una pausa de 30 segundos
        driver.maximize_window() # Maximise la ventana por si hay elementos que cambien su ubicacion u orden dependiendo del tamaño de la vista.
        driver.get('https://www.google.com/')

    def test_browser_navigator(self):
        driver = self.driver

        search_field = driver.find_element_by_name('q') # Buscador
        search_field.clear()
        search_field.send_keys('Platzi')
        search_field.submit()

        driver.back() # Retroceder
        # sleep(3) <- Este tipo de pausas agregan segundos a la ejecucion de la prueba
        driver.forward() # Avanzar
        driver.refresh() # Refescar

    def tearDown(self):
        self.driver.close()
        

if __name__ == "__main__":
    unittest.main(verbosity = 2)
```

## Demora implícita y explícita

Las pausas se pueden usar para forzar que selenium se detenga antes de continuar con las acciones que hay escritas. Sin embargo, las pausas no solamente sirven para eso, tambien nos ayudan a manejar el asincronismo, una de las debilidades que tiene selenium, y podemos encontrarlas en dos formas:

- **Imprisitas**: Busca uno o varios elementos en el DOM si no se encuentran disponibles por la cantidad de tiempo asignado.

- **Explicita**: Utiliza condiciones de espera determinadas y continua hasta que se cumplan.

### prueba [condiciones esperadas](https://github.com/diegoufp/DataScience/blob/master/selenium.md#condicionales-esperadas "condiciones esperadas") y demoras

```python
import unittest
from selenium import webdriver
#By nos ayuda a hacer referencia a un elemento del sitio web a travez de sus selectores, no para identificarlo sino para interactuar, distico a como lo hace driver
from selenium.webdriver.common.by import By 
# WebDriverWait nos ayudara a hacer las espected conditions junto con las esperas explicitas
from selenium.webdriver.support.ui import WebDriverWait
# Esperas explicitas 
from selenium.webdriver.support import expected_conditions as EC


class ExplicitWaitTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'./chromedriver')
        driver = self.driver
        driver.get('https://www.google.com/')

    def test_account_link(self):
        #until <- hasta que se cumpla la condicion esperada
        WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3' ) 

        account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'ACCOUNT')))
        account.click()

    def test_create_new_customer(self):
        self.driver.find_element_by_link_text('ACCOUNT').click()

        my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'My Account')))
        my_account.click()

        create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CREATE AN ACCOUNT')))
        create_account_button.click()

        WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))
```