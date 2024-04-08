# Preguntas

1. ¿Para qué usamos Clases en Python?

La programación orientada a objetos (POO) es una técnica muy útil para estructurar y organizar el código de manera lógica y coherente, lo que hace que el código sea más fácil de entender, mantener y mejorar. Por ello, el uso de clases en Python es una práctica muy común y recomendada para proyectos de software de cualquier tamaño y complejidad.

Veremos la definición de las clases, ventajas y desventajas de su uso, y algunos métodos para utilizarlas.

Una clase es una estructura de programación que permite definir un conjunto de  atributos y métodos que describen un objeto. Las clases son un concepto fundamental en la programación orientada a objetos, que se utilizan para modelar entidades del mundo real o abstracto en un programa.

Una clase define una plantilla o molde para crear objetos, los cuales son instancias de esa clase. Los objetos creados a partir de una clase tienen las mismas propiedades y comportamientos definidos por la clase, pero pueden tener valores diferentes para los atributos que se definen en la clase.

	1.1	Definicion de una clase

En Python, una clase se define mediante la palabra clave «class», seguida del nombre de la clase y dos puntos (:) y luego el cuerpo de la clase. El cuerpo de la clase contiene definiciones de métodos y atributos, que pueden ser públicos o privados según su acceso.
~~~
class Persona:
	def __init__(self, nombre, edad):
	self.nombre = nombre
	self.edad = edad
	
	def saludar(self):
		print("Hola, mi nombre es " + self.nombre)
~~~

	1.2	Atributos de una clase

Un atributo es una **variable** que se define dentro de una clase, la cual almacena datos que pertenecen a un objeto de esa clase. Los atributos se utilizan para representar características o propiedades de un objeto, como su estado actual, su identificador, su tamaño, su color, etc.

Los atributos pueden ser de diferentes tipos de datos, como enteros, flotantes, cadenas, listas, diccionarios, entre otros. Además, los atributos pueden tener distintos niveles de visibilidad, que se especifican mediante los modificadores de acceso en la definición de la clase. Por defecto, los atributos son públicos en Python, lo que significa que puede accederse a ellos desde cualquier lugar del programa.

En la definición de una clase, los atributos se definen como variables que se inicializan en el método especial **__init__**. Por ejemplo, en la clase Persona que definimos anteriormente, los atributos «nombre" y «edad» se definen de la siguiente manera:
~~~
class Persona:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad
~~~

En este caso, «nombre» y «edad» son atributos públicos de la clase Persona, que se inicializan con los valores proporcionados al crear un objeto de la clase. Para acceder a los atributos de un objeto de la clase, se utiliza la notación de punto (.), seguida del nombre del atributo. Por ejemplo, para acceder al atributo «nombre» de un objeto «persona1» de la clase Persona, se utiliza el siguiente código:

~~~
nombre_persona1 = persona1.nombre
~~~

En Python, los atributos de una clase pueden tener diferentes niveles de visibilidad, que se especifican mediante los modificadores de acceso en la definición de la clase. Los tres tipos principales de atributos son:

**Atributos públicos:** se puede acceder a ellos desde cualquier parte del programa, incluso desde fuera de la clase. En Python, los atributos se consideran públicos por defecto, lo que significa que no se requiere ningún modificador de acceso para especificar que un atributo es público. Para acceder a un atributo público, se utiliza la notación de punto (.) seguida del nombre del atributo.

**Atributos privados:** solo se puede acceder a ellos desde dentro de la clase en la que se definen. En Python, los atributos privados se definen mediante el prefijo **«__»** seguido del nombre del atributo. Por ejemplo, si queremos definir un atributo privado llamado «saldo» en una clase llamada CuentaBancaria, podemos hacerlo de la siguiente manera:
~~~
class CuentaBancaria:
	def __init__(self, saldo):
		self.__saldo = saldo
~~~
En este caso, **«__saldo»** es un atributo privado de la clase CuentaBancaria, que solo se puede acceder a él desde dentro de la clase. Si intentamos acceder a este atributo desde fuera de la clase se producirá un error.

**Atributos protegidos:** solo se puede acceder a ellos desde dentro de la clase en la que se definen y desde las clases derivadas (heredadas) de esa clase. En Python, los atributos protegidos se definen mediante el prefijo "" seguido del nombre del atributo. Sin embargo, en Python no existe un verdadero modificador de acceso protegido como en otros lenguajes de programación orientados a objetos, por lo que el uso del prefijo "" es una convención para indicar que un atributo está protegido, pero aún es posible acceder a él desde fuera de la clase.

	1.3	Métodos para las clases de Python

En Python, los métodos son funciones que se definen dentro de una clase y se utilizan para realizar operaciones en los objetos creados a partir de esa clase. Los métodos se definen de la misma manera que las funciones, pero siempre tienen como primer parámetro el objeto al que se aplicará el método, que suele llamarse **«self»** por convención.

Por ejemplo, si queremos definir una clase llamada CuentaBancaria que tenga un método para depositar dinero en la cuenta, podemos hacerlo de la siguiente manera:
~~~
class CuentaBancaria:
	def __init__(self, saldo):
		self.saldo = saldo
	def depositar(self, cantidad):
	self.saldo += cantidad
~~~

En este ejemplo, la clase CuentaBancaria tiene un método llamado «depositar» que toma como parámetro la cantidad de dinero a depositar en la cuenta y actualiza el saldo de la cuenta en consecuencia.

Para utilizar un método de una clase, primero debemos crear un objeto a partir de esa clase y luego llamar al método sobre ese objeto. Por ejemplo, para crear una instancia de la clase CuentaBancaria y depositar $100 en la cuenta, podemos hacer lo siguiente:

~~~
cuenta = CuentaBancaria(0)
cuenta.depositar(100)
~~~

En este caso, primero creamos una instancia de la clase CuentaBancaria con un saldo inicial de cero, y luego llamamos al método «depositar» sobre esa instancia para depositar $100 en la cuenta.

	1.4 Ventajas y desventajas del uso de las clases en Python
		
		1.4.1 Ventajas

**Reutilización de código:** las clases pueden reutilizarse en diferentes partes del programa o en distintos programas, lo que ahorra tiempo y reduce la duplicación de código.
	
**Encapsulación:** permiten ocultar la complejidad de un objeto y exponer solo una interfaz simple y fácil de usar para interactuar con él.
	
**Modularidad:** pueden descomponer un programa en componentes más pequeños y manejables, lo que facilita el mantenimiento y la solución de problemas.
	
**Polimorfismo:** ayudan a implementar el mismo conjunto de métodos con diferentes comportamientos para distintos tipos de objetos, lo que permite una mayor flexibilidad y extensibilidad en el diseño de programas.
	
		1.4.2 Desventajas

**Sobrecarga de complejidad:** las clases pueden agregar complejidad adicional a un programa y hacer que sea más difícil de entender y depurar.

**Curva de aprendizaje:** el aprendizaje de las clases y la programación orientada a objetos en general pueden requerir una curva de aprendizaje más pronunciada para los programadores principiantes.

**Uso innecesario:** a veces, las clases se utilizan innecesariamente en situaciones en las que una función simple podría haber hecho el trabajo de manera más eficiente.

2. ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

En la definición de una clase suele haber un método llamado __init__ que se conoce como inicializador. Es un método especial (también llamado método dunder) que se llama cada vez que se instancia una clase y sirve para **inicializar** el objeto que se crea. Cuando se crea una instancia de una clase, el método __init__ es llamado automáticamente por el intérprete de Python y se utiliza para realizar cualquier inicialización que sea necesaria para la instancia.

El método __init__ se usa para asignar valores iniciales a los atributos de una instancia de la clase. Los atributos son las variables que pertenecen a una instancia particular de la clase. Al llamar al método __init__, podemos establecer los valores de estos atributos y configurar la instancia de la clase para su uso posterior.

Por ejemplo, supongamos que queremos crear una clase llamada Persona con dos atributos: nombre y edad. Podríamos definir la clase de la siguiente manera:

class persona:

~~~
def __init__(self, nombre, edad): 
	self.nombre = nombre 
	self.edad = edad
~~~

En este ejemplo, el método __init__ toma dos parámetros: nombre y edad. Estos se utilizan para inicializar los atributos nombre y edad de la instancia de la clase.

Al crear una instancia de la clase Persona, se debe proporcionar un valor para cada uno de los parámetros nombre y edad, como en el siguiente ejemplo:

~~~
persona1 = Persona("Juan", 30)
~~~

3. ¿Cuáles son los tres verbos de API?

Los verbos Http involucrados en un sistema API REST son GET, POST y DELETE.

	3.1 GET

GET es el más simple de todos, es el que usamos para obtener un recurso. Las peticiones GET no deben causar efectos secundarios en un servidor, no deben producir nuevos registros, ni modificar los ya existentes. A esta cualidad la llamamos idempotencia, cuando una acción ejecutada un número indefinido de veces, produce siempre el mismo resultado.

Esto quiere decir, que no importa cuántas veces hagamos una petición GET, los resultados obtenidos serán los mismos.

Cuando ingresamos a la dirección usando GET https://codigofacilito.com/cursos/backend-profesional/ estamos solicitando que se nos entregue el recurso identificado por /cursos/backend-profesional, este es un buen ejemplo de uso con GET.

Esta otra ruta: https://codigofacilito.com/cursos/recomendar?selected_level=0&category_options=28 aunque más compleja, también es correcta, estamos solicitando los recursos identificados por /cursos con las opciones ahí indicadas. Sin importar cuantas veces hagamos esta solicitud, no modificará los resultados por sí misma.

	3.2 POST

Las peticiones con POST son para crear recursos nuevos, no para eliminarlos, ni para modificarlos. Cada llamada con POST debería producir un nuevo recurso.

Lo que es interesante acerca de POST no es el verbo en sí, queda muy claro que es para crear, más bien es los recursos a los que se dirige.

Por ejemplo, si en nuestra aplicación existe una colección de cursos, la solicitud para crear uno nuevo, debe ser con el verbo POST al recurso que identifica la colección, por ejemplo /cursos.

Si queremos crear un nuevo artículo, pudiéramos tener una URI /articulos. Lo que es importante en estos casos, es recordar que la URI no debe decir qué acción estamos ejecutando, nos olvidamos de /articulos/crear o de /cursos/agregar, etc. El verbo dice qué haremos, y la URI sobre qué recurso se harán las modificaciones.

Algunos escenarios más complejos para el uso de POST son los inicios de sesión, agregar a un carrito de compras, procesar un pago nuevo, etc.

Consideremos por ejemplo el inicio de sesión, normalmente al iniciar sesión, no producimos un nuevo registro en la base de datos, sin embargo, usamos POST porque estamos creando una sesión nueva. Esto nos da a entender que para saber si usaremos POST o no, no necesariamente tenemos que agregar registros en la base de datos, el recurso creado puede ser de otros tipos, como una sesión.

	3.3 DELETE

Por último, DELETE es el verbo que usamos para eliminar registros, bien pudiera ser para eliminar un recurso con un mensaje Http como

DELETE /cursos/backend-profesional

O para eliminar una colección completa:

DELETE /cursos

Esta es la manera a través de la que usamos los verbos Http en una aplicación web. Estos en combinación con las URIs proveen la interfaz uniforme de la que hablamos cuando discutimos las características de un sistema REST.


4. ¿Es MongoDB una base de datos SQL o NoSQL?

MongoDB es una base de datos NoSQL orientada a documentos que apareció a mediados de la década de 2000. Se utiliza para almacenar volúmenes masivos de datos.

A diferencia de una base de datos relacional SQL tradicional, MongoDB no se basa en tablas y columnas. Los datos se almacenan como colecciones y documentos.

Los documentos son pares value/key que sirven como unidad básica de datos. Las colecciones contienen conjuntos de documentos y funciones. Son el equivalente a las tablas en las bases de datos relacionales clásicas.

	4.1 Las características de MongoDB

Cada base de datos MongoDB contiene colecciones, que a su vez contienen documentos. Cada documento es diferente y puede tener un número variable de campos. El tamaño y el contenido de cada documento también varían.
La estructura de un documento corresponde a la forma en que los desarrolladores construyen sus clases y objetos en el lenguaje de programación utilizado. En general, las clases no son filas y columnas, sino que tienen una estructura clara formada por pares Value/key.

Los documentos no tienen un esquema predefinido y los campos pueden añadirse a voluntad. El modelo de datos disponible en MongoDB facilita la representación de relaciones jerárquicas u otras estructuras complejas.

Otra característica importante de MongoDB es la elasticidad de sus entornos. Muchas empresas tienen clusters de más de 100 nodos para bases de datos que contienen millones de documentos.

	4.2 La arquitectura de MongoDB y sus componentes

La arquitectura de MongoDB se basa en varios componentes principales. En primer lugar, «_id» es un campo obligatorio para cada documento. Representa un valor único y puede considerarse como la clave principal del documento para identificarlo dentro de la colección. 

Un documento es el equivalente a un registro en una base de datos tradicional. Se compone de campos de nombre y valor. Cada campo es una asociación entre un nombre y un valor y es similar a una columna en una base de datos relacional.

Una colección es un grupo de documentos de MongoDB, y se corresponde con una tabla creada con cualquier otro RDMS como Oracle o MS SQL en una base de datos relacional. No tiene una estructura predefinida.

Una base de datos es un contenedor de colecciones, al igual que un RDMS es un contenedor de tablas para las bases de datos relacionales. Cada uno tiene su propio conjunto de archivos en el sistema de archivos. Un servidor MongoDB puede almacenar múltiples bases de datos.

Por último, JSON (JavaScript Object Notation) es un formato de texto plano para expresar datos estructurados. Está soportado por muchos lenguajes de programación.  

	4.3 ¿Por qué utilizar MongoDB? ¿Cuáles son las ventajas?

MongoDB tiene varias ventajas importantes. En primer lugar, esta base de datos NoSQL orientada a documentos es muy flexible y se adapta a los casos de uso concretos de una empresa.

Las consultas ad hoc permiten encontrar campos específicos dentro de los documentos. También es posible crear índices para mejorar el rendimiento de las búsquedas. Se puede indexar cualquier campo.

Otra ventaja es la posibilidad de crear «conjuntos de réplicas» formados por dos o más instancias de MongoDB. Cada miembro puede actuar como réplica secundaria o primaria en cualquier momento.

La réplica primaria es el servidor principal, que interactúa con el cliente y realiza todas las operaciones de lectura y escritura. Las réplicas secundarias mantienen una copia de los datos. Así, en caso de fallo de la réplica primaria, el cambio a la secundaria se realiza automáticamente. Este sistema garantiza una alta disponibilidad.

Por último, el concepto de sharding permite el escalado horizontal al distribuir los datos entre múltiples instancias de MongoDB. La base de datos puede ejecutarse en varios servidores, y esto permite equilibrar la carga o duplicar los datos para mantener el sistema en funcionamiento en caso de fallo del hardware.

Debido a estas numerosas ventajas, MongoDB es ahora una herramienta muy utilizada en el campo de la ingeniería de datos. Es una solución imprescindible para los ingenieros de datos.  

	4.4 MongoDB vs RDBMS : ¿cuáles son las diferencias?

Hay varias diferencias importantes entre MongoDB y RDBMS (sistema de gestión de bases de datos relacionales). Como ya se ha mencionado, los datos no se almacenan en tablas, sino en colecciones de documentos. Estos documentos sustituyen a las filas de RDBMS. Contienen campos de pares valor/clave, que a su vez sustituyen a las columnas.

Además, la integridad de los datos no es una restricción en MongoDB. Los datos no necesitan ser «normalizados» antes de su uso como en un RDBMS. Esto es una ventaja real, ya que la restricción de normalización puede degradar el rendimiento a medida que la base de datos crece.

	4.5 Modelado de datos en MongoDB

A diferencia de las bases de datos SQL, MongoDB no implica ninguna restricción en cuanto a la estructura de los documentos. Los datos no tienen un esquema preconcebido, y es esta flexibilidad la que hace que MongoDB sea tan potente y eficiente.

El modelado de los datos y la estructura de los documentos sólo deben responder a las necesidades del usuario. Es importante tener en cuenta las necesidades de la aplicación y, por tanto, qué datos y tipos de datos se necesitarán.

Si se esperan muchas consultas, es pertinente utilizar índices en el modelo de datos para mejorar la eficiencia de las consultas. Por último, si se producen frecuentes adiciones, actualizaciones y eliminaciones de datos, conviene utilizar los índices y el sistema de fragmentación para mejorar la eficacia global del entorno.


5. ¿Qué es una API?
	
Las API son mecanismos que permiten a dos componentes de software comunicarse entre sí mediante un conjunto de definiciones y protocolos. Por ejemplo, el sistema de software del instituto de meteorología contiene datos meteorológicos diarios. La aplicación meteorológica de su teléfono “habla” con este sistema a través de las API y le muestra las actualizaciones meteorológicas diarias en su teléfono.

API significa “interfaz de programación de aplicaciones”. En el contexto de las API, la palabra aplicación se refiere a cualquier software con una función distinta. La interfaz puede considerarse como un contrato de servicio entre dos aplicaciones. Este contrato define cómo se comunican entre sí mediante solicitudes y respuestas. La documentación de su API contiene información sobre cómo los desarrolladores deben estructurar esas solicitudes y respuestas.

	5.1 ¿Qué son las API de REST?

REST significa transferencia de estado representacional. REST define un conjunto de funciones como GET, PUT, DELETE, etc. que los clientes pueden utilizar para acceder a los datos del servidor. Los clientes y los servidores intercambian datos mediante HTTP.

La principal característica de la API de REST es que no tiene estado. La ausencia de estado significa que los servidores no guardan los datos del cliente entre las solicitudes. Las solicitudes de los clientes al servidor son similares a las URL que se escriben en el navegador para visitar un sitio web. La respuesta del servidor son datos simples, sin la típica representación gráfica de una página web.

6. ¿Qué es Postman?

Postman en sus inicios nace como una extensión que podía ser utilizada en el navegador Chrome de Google y básicamente nos permite realizar peticiones de una manera simple para testear APIs de tipo REST propias o de terceros.

Gracias a los avances tecnológicos, Postman ha evolucionado y ha pasado de ser de una extensión a una aplicación que dispone de herramientas nativas para diversos sistemas operativos como lo son Windows, Mac y Linux.

Cuenta con una versión libre de pago y con tres planes (básico, profesional y empresarial), si deseas consultar el detalle entre cada plan y sus precios puedes verlo en su web oficial.

	6.1 Para qué sirve Postman

Postman sirve para múltiples tareas dentro de las cuales destacaremos en esta oportunidad las siguientes:

Testear colecciones o catálogos de APIs tanto para Frontend como para Backend.
Organizar en carpetas, funcionalidades y módulos los servicios web.
Permite gestionar el ciclo de vida (conceptualización y definición, desarrollo, monitoreo y mantenimiento) de nuestra API.
Generar documentación de nuestras APIs.
Trabajar con entornos (calidad, desarrollo, producción) y de este modo es posible compartir a través de un entorno cloud la información con el resto del equipo involucrado en el desarrollo.

	6.2 Métodos más utilizados y posibles errores

Postman cuenta con una serie de métodos que nos permiten tomar acción ante nuestras peticiones, a continuación, te dejamos los más utilizados:
	- GET: Obtener información
	- POST: Agregar información
	- PUT: Reemplazar la información
	- PATCH: Actualizar alguna información
	- DELETE: Borrar información

En cuanto a los posibles errores que podemos apreciar en la respuesta que nos ofrece la herramienta, lo podemos resumir:
	Rango de **“200”** quiere decir que toda la petición ha salido bien.
	Códigos de error en rango de **“400”** hacen referencia a errores con el cliente.
	Con códigos en rango de los **“500”** tienen que ver con fallos en el servidor.

7. ¿Qué es el polimorfismo?

Python permite la implementación de polimorfismo a través del uso de herencia y sobreescritura de métodos. El polimorfismo permite que un objeto se comporte de manera diferente en distintos contextos.

En Python, el polimorfismo se implementa de manera natural gracias a la capacidad de las funciones y métodos para aceptar argumentos de diferentes tipos. Por lo tanto, para implementar el polimorfismo en la clase Automóvil, simplemente se deben definir diferentes métodos que compartan el mismo nombre pero que acepten distintos tipos de argumentos.

Por ejemplo, se podría definir un método llamado «acelerar» en la clase Automóvil, el cual acepte un argumento que represente la cantidad de gas que se quiere suministrar al motor. Luego, se podrían definir diferentes versiones de este método que acepten distintos tipos de argumentos.

~~~
class Automovil:
	def __init__(self, marca, modelo, color, velocidad_maxima):
		self.__marca = marca
		self.__modelo = modelo
		self.__color = color
		self.__velocidad_maxima = velocidad_maxima
		
	def acelerar(self, gas):
		print("Suministrando gas al motor:", gas)
	
	def frenar(self):
		print("Frenando el automóvil")

class AutomovilElectrico(Automovil):
	def __init__(self, marca, modelo, color, velocidad_maxima, capacidad_bateria):
		super().__init__(marca, modelo, color, velocidad_maxima)
		self.__capacidad_bateria = capacidad_bateria

	def acelerar(self, nivel_carga):
		if nivel_carga >= 50:
			print("El automóvil eléctrico acelera rápidamente")
		else:
			print("El automóvil eléctrico acelera lentamente")

class AutomovilDeportivo(Automovil):
	def __init__(self, marca, modelo, color, velocidad_maxima, aleron):
		super().__init__(marca, modelo, color, velocidad_maxima)
		self.__aleron = aleron

def acelerar(self, pedal_a_fondo=true):
	if pedal_a_fondo:
		print("El automóvil deportivo acelera rápidamente")
	else:
		print("El automóvil deportivo acelera lentamente")
~~~


En este ejemplo, la clase Automóvil tiene un método llamado acelerar que acepta un argumento gas, que representa la cantidad de gas que se suministra al motor. La subclase AutomovilElectrico redefine el método acelerar para aceptar un argumento nivel_carga, que representa el nivel de carga de la batería del automóvil eléctrico. Si el nivel de carga es mayor o igual a 50, el automóvil acelera rápidamente; de lo contrario, acelera lentamente.

La subclase AutomovilDeportivo también redefine el método acelerar, esta vez para aceptar un argumento opcional pedal_a_fondo. Si este argumento es True, el automóvil deportivo acelera rápidamente; de lo contrario, lo hace lentamente.

8. ¿Qué es un método dunder?

En Python, los métodos dunder (abreviatura de «double underscore methods», también conocidos como «métodos mágicos» o «métodos especiales») son métodos especiales que tienen un doble guion bajo **(__)** al principio y al final de su nombre. Se emplean para definir el comportamiento especial de las clases y sus instancias, y son llamados automáticamente por el intérprete de Python en respuesta a ciertas operaciones.

Los métodos dunder pueden utilizarse para implementar características como la inicialización de objetos, la representación en forma de cadena, la sobrecarga de operadores, la comparación, entre otras.

Por ejemplo, el método __init__ es un método dunder. Como ya hemos visto en el punto 2 que se usa para inicializar un objeto cuando se crea una instancia de una clase. A continuación se muestra una lista de algunos de los métodos dunder más comunes en Python, **__init** ya lo vimos con atr¡erioridad, isto:


**__str__**

Es otro método especial (dunder) en Python que se utiliza para devolver una representación de cadena (string) de una instancia de una clase. Este método se llama cuando se usa la función str() para convertir un objeto en una cadena de caracteres.

En otras palabras, el método **__str__** se emplea para definir cómo se debe imprimir una instancia de la clase cuando se llama la función str() o cuando se utiliza la interpolación de cadenas (f-strings).

Por ejemplo, supongamos que tenemos una clase Persona con los atributos nombre y edad. Podemos definir el método **__str__** de la siguiente manera:

~~~
class Persona:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

	def __str__(self):
		return f"{self.nombre} ({self.edad} años)"
~~~

En este ejemplo, el método **__str__** devuelve una cadena de caracteres que representa la instancia de la clase Persona. La cadena contiene el nombre y la edad de la persona, separados por un espacio.

Al utilizar la función str() con una instancia de la clase Persona, se llamará automáticamente al método **__str__**, como en el siguiente ejemplo:

~~~
persona1 = Persona("Juan", 30)
print(str(persona1)) 	# salida: Juan (30 años)
~~~

**__repr__()**

Es un método especial en Python que se utiliza para devolver una representación de cadena legible de un objeto. Este método se define dentro de una clase y se llama cuando se usa la función repr() en un objeto de esa clase.

La representación de cadena devuelta por **__repr__()** debe ser una cadena que sea suficiente para recrear el objeto original. Por lo tanto, se espera que el resultado sea una cadena que contenga información relevante sobre el objeto y sus valores de atributo.

Es importante tener en cuenta que el método **__repr__()** no es lo mismo que el método **__str__()**. El método **__str__()** devuelve una representación de cadena legible para humanos del objeto, mientras que el método **__repr__()** devuelve una representación de cadena que es suficiente para recrear el objeto.

Aquí hay un ejemplo de cómo se puede implementar el método **__repr__()** en una clase de Python:

~~~
class Persona:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad
	def __repr__(self):
		return f"persona(nombre='{self.nombre}', edad={self.edad})"

~~~

Además, **__add__, __sub__, __mul__** y **__truediv__** se utilizan para sobrecargar los operadores aritméticos (+, -, *, /) para las instancias de una clase.

9. ¿Qué es un decorador de python?

Los decoradores son funciones que modifican el comportamiento de otras funciones, ayudan a acortar nuestro código y hacen que sea más Pythonic. Si alguna vez has visto @, estás ante un decorador o decorator, bien sea uno que Python ofrece por defecto o uno que puede haber sido creado ex profeso.

Si aún no controlas las funciones te recomendamos que empieces con este post.

Veamos un ejemplo muy sencillo. Tenemos una función suma() que vamos a decorar usando mi_decorador(). Para ello, antes de la declaración de la función suma, hacemos uso de @mi_decorador.
~~~
def mi_decorador(funcion):
    def nueva_funcion(a, b):
        print("Se va a llamar")
        c = funcion(a, b)
        print("Se ha llamado")
        return c
    return nueva_funcion

@mi_decorador
def suma(a, b):
    print("Entra en funcion suma")
    return a + b

suma(5,8)

# Se va a llamar
# Entra en funcion suma
# Se ha llamado
~~~

Lo que realiza mi_decorador() es definir una nueva función que encapsula o envuelve la función que se pasa como entrada. Concretamente lo que hace es hace uso de dos print(), uno antes y otro después de la llamada la función.

Por lo tanto, cualquier función que use @mi_decorador tendrá dos print, uno y al principio y otro al final, dando igual lo que realmente haga la función.