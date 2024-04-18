# Module 3 _ Checkpoint 6

## 1. ¿Para qué usamos Clases en Python?

Python es un tipo de programación orientada a objetos(POO), por lo que prácticamente todo en Python es un objeto que posee propiedades (o atributos) y métodos. Un método es una función está asociada a un objeto específico.

A grandes rasgos, en Python, una clase podría asemejarse al plano de construcción de una casa (blueprint), con la diferencia de que en lugar de casas podremos construir objetos. 

La clase vendría a ser una especie de plantilla que se utiliza para crear objetos, en esa plantilla van a estar determinados los atributos(propiedades) y los comportamientos que van a tener los objetos que creemos a partir de ella. 

Cuando construimos varias casas a partir de un mismo plano, si bien podrá variar el color de las paredes, el tipo de ventanas, o la orientación de la misma, la estructura de la casa seguirá siendo idéntica. Lo mismo ocurre con las diferentes clases que vayamos creando a partir de ese patrón: estamos creando un objeto único e individual, con sus propios métodos, atributos, instancias de objeto (que ya veremos lo que son).

Las clases son un tipo de objeto que contiene: 

- Métodos, que determinarán los diversos comportamientos que tenga.

- Atributos de clase, que son propiedades almacenadas en variables que pertenecen a la clase y que, por tanto, serán comunes a todas las instancias de objeto dentro de esa clase y se aplicarán a ellas.

- Instancias de objeto pertenecientes a esa clase. Es decir, objetos que pertenecen a esa clase y a los que pasaremos argumentos para que se les apliquen los métodos que nosotros determinemos dentro de la misma.

La sintaxis para crear instancias de objeto de cada clase es la siguiente:

```python

perro = Perro() 

"""creo la instancia perro que pertenece a la clase Perro, a la que no he pasado argumentos -->()"""

#ver método __init__ en la pregunta 2
```

**Cómo crear una clase**

Para crear una clase lo primero es usar la palabra reservada class(en minúsculas) y el nombre que le demos a nuestra clase. Para nombrar clases se usa la convención CamelCase, donde cada palabra debe iniciar con mayúsculas, de este modo no se confundirá con variables, instancias de objeto, etc.

Una vez creada nuestra clase ya podremos agregar atributos de clase, métodos e instancias de objetos exclusivos de esa clase pero que se aplicarán a todas las instancias(objetos) que creemos dentro de ella.

```python

class Perro: #creo la clase
    def sonido(self): """defino un método con self como argumento,que hace referencia al objeto)"""
        return "guau" #lo que quiero que retorne

print(Perro().sonido()) #imprimo en la consola para verlo

```
**Atributos de clase**

```python

class Perro: 
    reino = "animal" #aquí hemos creado un atributo de clase
    def sonido(self): 
        return "guau" 
print
```

**Para qué sirven las clases**

Algunas utilidades de las clases en Python:

1) Permiten crear representaciones de entidades del mundo real en forma de objetos "simplificados". Se identifican sus atributos y sus comportamientos principales y se crea una representación. Por ejemplo, si pensamos en un perro podemos identificar como atributos su raza, su tamaño, su color, su nombre, su edad... y como comportamientos que ladra, que come, que muerde... Basándonos en eso podemos crear una representación abstracta, y a grandes rasgos, de un perro. 

2) Permiten agrupar los atributos, instancias de objeto y métodos en una única estructura, esto se conoce como encapsulación. Entre otras cosas, la encapsulación evita, por ejemplo, que haya acceso a las variables desde fuera de la clase y nuestro código se modifique accidentalmente. La encapsulación permite, en cierta forma, restringir el acceso a los métodos y variables que hemos creado dentro de esa clase.

3) Abstracción: Las clases hacen que sea posible interactuar con los objetos sin conocer todos los detalles internos de como funciona, lo  mismo que cuando usamos un electrodoméstico, sabemos usarlo pero no necesariamente todo lo que está ocurriendo dentro de este para que pueda funcionar.

4) Polimorfismo: Dentro de las diferentes clases podemos crear un método con el mismo nombre, en el siguiente ejemplo será el método "sonido". Ambas clases tendrán un método idéntico, pero con comportamientos diferentes (retornan cosas distintas).

```python

class Perro:
    def sonido(self):
        return "guau"

class Gato:
    def sonido(self):
        return "miau"

```
Una vez hecho esto puedo crear un método fuera de esas clases. Ese método se aplicará a ambas clases cuando hagamos el llamado al método "sonido"(que ambas comparten), y estas responderán de forma diferente, de acuerdo al comportamiento que se haya determinado para cada una de ellas (retornar una cosa u otra, en este caso). 

```python
class Perro:
    def sonido(self):
        return "guau"

class Gato:
    def sonido(self):
        return "miau"
      
def hacer_sonido(animal):
    return animal.sonido()    
  
perro = Perro()
gato = Gato()

print(hacer_sonido(perro))  #imprime guau
print(hacer_sonido(gato)) #imprime miau

```

5) El código creado en una clase puede ser reutilizado a través de la herencia, es decir que una clase puede heredar métodos y atributos de otra clase, lo cual nos permite utilizar el tiempo de manera más eficiente, evitar la duplicación del código (y con ello evitar posibles errores de sintaxis) y crear un código más eficiente y fácil de entender. 


## 2. ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

Cuando creamos una instancia de clase se ejecuta el método especial __ init__ (método dunder init). Este método se conoce también como método constructor y sirve para crear instancias de objeto, es decir, objetos de la clase dentro de la cual los estemos creando.

Este método funciona como una plantilla, en la cual se establecerán los atributos que debe tener cada uno de los objetos creados. Esos atributos o propiedades luego se pasarán a la instancia de objeto en forma de argumentos. 

La sintaxis para crear este método es la siguiente:

```python
class Perro:
       def __init__(self, tamaño, actitud):
           self.tamañao = tamaño
           self.actitud = actitud

```
Dentro de la clase he definido el método __ init__ y le he pasado como parámetros self(que hace referencia al objeto que crearé a partir de este método), tamaño y actitud. Esos parámetros hacen referencia a los atributos (propiedades, o en este caso características) de nuestro objeto, los cuales determinaremos en las siguientes dos líneas de la siguiente forma: self.atributo1 = parámetro1.

Una vez que hemos definido el método con los atributos y sus parámetros correspondientes, podemos proceder a crear la instancia de objeto. En este caso, como la clase es Perro crearemos las instancias de acuerdo a su raza. Al crear la instancia de objeto, en la clase Perro() es donde debo pasar argumentos para los parámetros anteriores que corresponden a los atributos.

```python

class Perro:
    def __init__(self, tamaño, actitud):
        self.tamaño = tamaño
        self.actitud = actitud

    def __str__ (self):
        return f' Perro {self.tamaño}, {self.actitud}.'

labrador_retriever = Perro("mediano","fácil de adiestrar")
fila_brasileño = Perro("muy grande", "fiel, aunque no compatible con niños")

print(labrador_retriever)
print(fila_brasileño)

```

En este caso se ha definido también el método especial __ str__ que permite crear una representación legible del objeto, de lo contrario solo obtendríamos algo como: <__ main__.Perro object at 0x7f7bf800e530>, que es una representación del objeto que muestra su ubicación en la memoria. 

Es importante mencionar que los atributos que se designan dentro del método __ innit__ no son atributos de clase, sino atributos de objeto, por lo que serán únicos para cada instancia de objeto. Cada instancia de objeto tiene su propia copia independiente de esos atributos y se definen por los argumentos que le pasemos al crearla, por lo que cada instancia de objeto suele tener valores distintos asociados a esos atributos. 

**Los atributos de clase**, como lo hemos mencionado previamente, son comunes a todas las instancias de objeto de la clase. En el ejemplo de la clase perro, todos son animales, por lo que eso sería un atributo de clase, ya que es común a todas las instancias de objeto. Los atributos de clase se definen en una variable.

```python

class Perro:
  especie = "Perro"  #atributo de clase compartido por todas las instancias de objeto
  
  def __init__(self, tamaño, actitud):
      self.tamaño = tamaño
      self.actitud = actitud

  def __str__ (self):
      return f'{self.especie} {self.tamaño}, {self.actitud}.'

labrador_retriever = Perro("mediano","fácil de adiestrar")
fila_brasileño = Perro("muy grande", "fiel, aunque no compatible con niños")

print(labrador_retriever)
print(fila_brasileño)
```

## 3. ¿Cuáles son los tres verbos de API?

**Los verbos HTTP principales son:**

1. **GET:** Que se utiliza para consultar datos. El verbo GET no debe crear nuevos registros ni modificar los existentes, por lo que al realizar la misma consulta múltiples veces no debe alterarse el resultado. A esa cualidad se le llama idempotencia.

2. **POST:** Que se utiliza para enviar datos al servidor que permitan crear un nuevo recurso. A diferencia de GET, el enviar varias solicitudes POST puede alterar el resultado y crear múltiples recursos. Este no es idempotente, ya que altera el resultado.

3. **PUT:** Permite actualizar o crear recursos en el servidor, pero a diferencia de POST, enviar la misma solicitud varias veces no creará múltiples recursos.

4. **DELETE:** Sirve para eliminar el recurso específico que indiquemos en el servidor. También es idempotente, por lo que sin importar cuantas veces enviemos la solicitud, el recurso se eliminará igualmente.

**Cómo crear un endpoint de API realizando una solicitud con el método POST**


```python
@app.route('/guide', methods=["POST"]) 
def add_guide():
    title = request.json['title']
    content = request.json['content']

    new_guide = Guide(title, content)

    db.session.add(new_guide)
    db.session.commit()

```
## Explicación:

**@app.route('/guide', methods=["POST"])**

Utilizo un decorador de ruta para la ruta '/guide' con el método POST, esto significa que cuando se realice una solicitud POST para la ruta que hemos determinado se activará la función def add_guide().

**def add_guide():**

Esta es la función que se ejecutará cuando se reciba una solicitud POST en '/guide'. 

**title = request.json['title']**

**content = request.json['content']**

Accedemos al valor del campo "title" enviado en la solicitud (request) y lo almacenamos en la variable title (lo mismo con content).

Utilizamos request.json para acceder a esos datos de una manera fácil de manejar. Para ello debemos previamente haber importado los siguientes módulos en nuestra aplicación Flask: from flask import Flask, request, jsonify


**new_guide = Guide(title, content)**


Aquí estamos creando una nueva instancia de la clase 'Guide', con el 'title' y 'content' proporcionados en la solicitud realizada desde Postman u otro cliente que realice solicitudes HTTP.


**db.session.add(new_guide)**

Se guarda una nueva instancia de la clase 'Guide' a la sesión de la base de datos

**db.session.commit()**

Se confirma la transacción en la base de datos, es decir, guarda new_guide en la base de datos.

En caso de querer realizar otras solicitudes habría que verificar o modificar la ruta, elegir el método (GET, PUT, DELETE), definir otra función para que se ejecute cuando se reciba la nueva solicitud y adaptar la lógica dentro de esta a lo que deseamos hacer, sea actualizar, borrar datos, o realizar una consulta.


**Existen otros verbos HTTP:**

**PATCH:** Permite realizar modificaciones parciales a un recurso. Se diferencia de PUT en que no actualiza completamente el recurso, sino que lo modifica parcialmente.

**HEAD:** Es similar al verbo GET, pero a diferencia de este, sólo solicita encabezados. De este modo podemos obtener información del recurso sin necesidad de obtener los datos completos. Sirve para comprobar la existencia de un recurso sin tener que acceder al recurso entero.

**OPTIONS:** Permite obtener información como las capacidades de comunicación de un servidor, los métodos de solicitud permitidos por un recurso o qué encabezados es necesario proporcionar.

**TRACE:** Permite solicitar al servidor que devuelva la solicitud que se ha enviado. Es útil para depuración y diagnosticar posibles problemas en la red.


## 4. ¿Es MongoDB una base de datos SQL o NoSQL?

MongoDB es una base de datos NoSQL que almacena datos en un formato similar a JSON. 

Las bases NoSQL se caracterizan por no utilizar el modelo relacional de las bases de datos SQL tradicionales. Las bases de datos SQL utilizan la lógica matemática de las relaciones entre tablas para organizar y representar los datos, mientras que las bases de datos NoSQL se caracterizan por utilizar otros modelos de almacenamiento y estructuras de datos que no se basan en el modelo relacional de tablas.

Dentro de las bases de datos NoSQL podemos encontrar MongoDB y Cassandra, que tienen como ventajas:

Escalabilidad Horizontal: están diseñadas para crecer de manera horizontal, por lo que es posible agregar más servidores para manejar un mayor volumen de datos y tráfico sin comprometer su rendimiento. 

En lugar de depender de un único servidor poderoso, la arquitectura de las bases de datos NoSQL permite distribuir la carga de trabajo entre varios servidores, a esto se le llama escalar horizontalmente. Los datos se distribuyen entre múltiples servidores, lo que evita la saturación de un único servidor y distribuye la carga de manera equitativa, esto también aumenta la capacidad total de almacenamiento y como la carga se distribuye en varios servidores, se obtiene un mejor rendimiento global del sistema. 

También tiene como ventaja que si un servidor falla, los otros pueden garantizar la disponibilidad de los datos sin interrupciones significativas.

Además de las ventajas de las bases de datos NoSQL MongoDB en concreto tiene como ventajas:

- Representación de datos legible: El formato de documentos en MongoDB, similar a objetos JSON o BSON, proporciona una representación legible de los datos, eso facilita tanto comprender como manipular esos datos. 

- Flexibilidad en la Estructura de los Datos: Permite representar datos de forma flexible, sin necesidad de adherirse a un esquema rígido predefinido (cosa que sí ocurre con las bases de datos SQL). Esto sin embargo, requiere que sea el desarrollador quien cree su propio esquema y lo respete, de modo que pueda acceder a los datos de forma eficiente cuando sea necesario.

Compatibilidad con Diversos Tipos de Datos: Permite almacenar múltiples de tipos de datos en sus documentos, así como anidar datos.

Facilidad de Integración con Aplicaciones: La estructura de los documentos en MongoDB facilita la integración con aplicaciones modernas, frameworks y lenguajes de programación que manejan datos en formato JSON.



## 5. ¿Qué es una API?

API significa Interfaz de Programación de Aplicaciones. Es un conjunto de reglas y herramientas que permite a diferentes aplicaciones y sistemas comunicarse entre sí.

Ejemplo:
"El sistema de software del instituto de meteorología contiene datos meteorológicos diarios. La aplicación meteorológica de su teléfono “habla” con este sistema a través de las API y le muestra las actualizaciones meteorológicas diarias en su teléfono." 
(Ejemplo obtenido de -->  https://aws.amazon.com/es/what-is/api/)

¿Cómo funciona una API?

- Una API permite a una aplicación utilizar funcionalidades o datos de otra aplicación o servicio sin necesidad de conocer su implementación interna (no necesita conocer cómo se implementan las funciones o los datos en la otra aplicación).

- Las API pueden enviar solicitudes y recibir respuestas mediante protocolos estándar como HTTP, y suelen utilizar formatos de intercambio de datos como JSON o XML.

**Ventajas de las APIs:**

1. La comunicación entre sistemas y aplicaciones se realiza de manera estandarizada, lo que lo hace más sencilla y eficiente.

2. Las APIs permiten a los desarrolladores utilizar funcionalidades existentes.

3. Es posible aprovechar APIs públicas o privadas, lo cual simplifica la tarea ya que requiere menor tiempo invertido en ello.

4. Son de fácil mantenimiento.

## 6. ¿Qué es Postman?

Postman es una plataforma que permite a los desarrolladores diseñar, probar y documentar APIs. Es una herramienta que permite además enviar solicitudes HTTP a través de una interfaz fácil de usar y de manera sencilla. 

**¿Para qué sirve Postman?**

- Postman se utiliza para probar, desarrollar y documentar APIs.

- Sirve para crear y ejecutar solicitudes HTTP, con soporte para varios métodos como GET, POST, PUT, DELETE, PATCH, HEAD y OPTIONS.

- Facilita la colaboración entre equipos al permitir compartir colecciones de solicitudes y entornos de trabajo.

**Ventajas de usar Postman:**

1. Postman es fácil de usar, ya que tiene una interfaz intuitiva que facilita la creación y ejecución de solicitudes HTTP.

2. Permite automatizar pruebas de API para garantizar la calidad del software.

3. Permite generar documentación interactiva para API. Documentación interactiva es la que permite a los usuarios interactuar con la API directamente desde la documentación misma, en lugar de solo leer sobre ella.

4. Colecciones compartidas: Permite compartir colecciones de solicitudes y entornos de trabajo entre miembros del equipo. Una colección de solicitudes es un conjunto de solicitudes HTTP relacionadas que se agrupan juntas por un tema o funcionalidad común.

5. Permite monitorizar y analizar el rendimiento de las API.

**¿Cómo funciona Postman?**

- Postman funciona como una herramienta de escritorio o como una extensión de navegador que permite crear, probar y modificar solicitudes HTTP.

- Es posible enviar diferentes tipos de solicitudes a una API (GET, POST, PUT, DELETE) y recibir respuestas para verificar el funcionamiento de la API.

- Postman organiza las solicitudes en colecciones, lo que facilita la gestión y la ejecución de pruebas.

## 7. ¿Qué es el polimorfismo?

El polimorfismo es un concepto de la programación orientada a objetos que permite que objetos de distintas clases sean tratados de manera homogénea. Esto significa que a diferentes instancias de objeto puede aplicarse una misma función que proporcionará comportamientos diferentes, ya que estos dependerán de los atributos de cada objeto. 

Dicho de otra forma, el polimorfismo permite que diferentes instancias de una clase respondan de manera específica a una misma llamada de método, lo que devuelve comportamientos distintos según las características y funcionalidades de cada objeto en particular.

**¿Cómo funciona?**

Dentro de las difrentes clases podemos crear un método con el mismo nombre, en el siguiente ejemplo será el método "sonido". Ambas clases tendrán un método idéntico pero con comportamientos diferentes (retornan cosas distintas).

```python

class Perro:
    def sonido(self):
        return "guau"

class Gato:
    def sonido(self):
        return "miau"

```
Una vez hecho esto creo un método fuera de esas clases. Ese método se aplicará a ambas clases cuando hagamos el llamado al método "sonido"(que ambas comparten), y estas responderán de forma diferente, de acuerdo al comportamiento que se haya determinado para cada una de ellas (retornar una cosa u otra, en este caso). 

```python
class Perro:
    def sonido(self):
        return "guau"

class Gato:
    def sonido(self):
        return "miau"
      
def hacer_sonido(animal):
    return animal.sonido()    
  
perro = Perro()
gato = Gato()

print(hacer_sonido(perro))  #imprime guau
print(hacer_sonido(gato)) #imprime miau

```


## 8. ¿Qué es un método dunder?

Los métodos dunder, también conocidos como métodos especiales o métodos mágicos en Python, son métodos predefinidos que comienzan y terminan con doble guion bajo (__). Estos métodos están señalizados por dos guiones bajos antes y después, lo cual sirve para indicar al programador que no debe llamarlos directamente, ya que son llamados por el propio interprete de Python (programa que lee y ejecuta código escrito en el lenguaje de programación Python).

Estos métodos especiales que describen cómo deben comportarse determinados objetos. Por ejemplo, el método __ init__ o método de inicialización de la clase, que hemos visto previamente, se llama automáticamente cuando se crea una nueva instancia de la clase y se utiliza para inicializar(establecer) los atributos del objeto.(Ver pregunta 2 para ejemplos).

El método __ str__ al que también hemos hecho referencia en la pregunta 2, devuelve una representación legible del objeto como una cadena de texto.

Por su parte, el método __ repr__ devuelve una representación para definir la representación oficial de un objeto cuando se llama la función repr() en ese objeto. Al usar este método estamos determinando como debe representarse esa instancia de la clase al momento de llamar a la función repr() en ese objeto.  El método __ repr__ es comúnmente usado en para hacer debugging. A diferencia del método __ str__ cuya salida será leída por humanos, el método __ repr__ dará una salida JSON, por ejemplo, que si bien puede ser útil para desarrolladores o interpretada por nuestro intérprete, no será legible de forma sencilla. Esta salida no es automática sino que la crea el desarrollador al decidir lo que quiere que devuelva.

### Ejemplos: 

```python
class Invoice: #Se crea la clase invoice
  def __init__(self, client, total):#ver pregunta 2 para explicación
    self.client = client
    self.total = total

  def __str__(self):#ver pregunta 2 para explicación
    return f"Invoice from {self.client} for {self.total}"

  def __repr__(self): #método re
    return f"Invoice>value: client: {self.client}, total: {self.total})>"


inv = Invoice('Google', 500)
print(str(inv))
print(repr(inv)) 

"""Al llamar a repr en una instancia de la clase Invoice, se obtendrá la representación definida en el método repr(), mientras que al llamar al método str(), se obtiene representación legible."""

```

## 9. ¿Qué es un decorador de Python?


Los decoradores como el decorador **@property** son útiles para encapsular y proteger nuestro código. Poder acceder a todos los datos de una clase y poder modificarlos en cualquier momento se considera mala práctica, aunque a veces puede ser necesario. El hecho de que todos tengan acceso a los datos puede provocar que sean sobreescritos por error, por lo que se usan decoradores como @property para protegerlos.

**self._client = client**  --> Se usa _ antes del atributo como advertencia de que ese atributo debe ser protegido.

**self.__client = client**  --> Se usa _ antes del atributo cuando quiero que un atributo sea privado y no pueda ser accedido ni siquiera por clases hijas. Esto se conoce como "name mangling", Python realiza un cambio interno de nombre que ahora será _nombredelaclase__atributo, eso obliga a ser muy consciente sobre si deseo modificar ese atributo.

```python
class Perro:
    def __init__(self, nombre):
        self.nombre = nombre 

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

perro = Perro ("Rocky")

print(perro.nombre)
```

#### Explicación
```python
class Perro:
```
Se crea la clase Perro

```python
    def __init__(self, nombre):
        self.nombre = nombre
```
Se define el método constructor __ init__ con el atributo nombre

```python
    @property 
    def nombre(self):
        return self._nombre
```

Se crea el decorador property

Dentro de él se difine una función getter llamada nombre, un getter es un método que nos devuelve un valor.

Luego se retorna el valor al que queremos acceder, a ese valor le agregamos _ antes del atributo para protegerlo y que no sea modificado por error.

```python
    @nombre.setter 
    def nombre(self, nombre):
        self._nombre = nombre
```

Se crea el decorador setter con el método setter dentro, al que hemos llamado nombre.setter porque ese es el valor que vamos a modificar.

Asignamos al atributo self._nombre el valor nombre, por lo que de aquí en más, cuando llamemos al atributo self._nombre lo llamaremos simplemente nombre.

```python
perro = Perro ("Rocky") 
```

Creamos una instancia de objeto de la clase Perro()

```python
print(perro.nombre) 
```

Imprimimos el objeto perro y el atributo al que deseamos acceder (en este caso sólo tenemos uno). 

