### Crear entorno virtual en windows

* comando: `python -m venv venv/env1`

* activar entorno virtual: `./venv/env1/Scripts/activate`

### Instalacion de dependencias
Para ello se hace uso de pip, el cual es un manejador de paquetes de python

* instalar pip: `pip install pip`

* actualizar pip: `python -m pip install --upgrade pip`

* comando: `pip install mi_paquete`


### Documentacion de Django##

* [Documentacion de Django](https://docs.djangoproject.com/en/4.2/)

* instalar django: `pip install django`

Nota: se recomienda instalar django en el entorno virtual "env1"

* revisar paquetes instalados: `pip freeze`

### Crear proyecto en Django

* comando: `django-admin startproject nombre_proyecto`

Esto crea una carpeta con el nombre del proyecto. Dentro de esta se encuentra un archivo llamado manage.py, el cual permite ejecutar comandos de django. y una carpeta con el mismo nombre del proyecto, la cual contiene los archivos del proyecto.

* acceder a la carpeta del proyecto: `cd nombre_proyecto`

* ver lista de comandos: `python manage.py help`

* generar migracion inicial: `python manage.py migrate`

* crear superusuario: `python manage.py createsuperuser`
Luego nos solicita un nombre de usuario, correo electronico y contraseña.

* ejecutar servidor: `python manage.py runserver`

* entrar al panel de administracion: `http://127.0.0.1:8000/admin/`

### Base de datos por defecto de Django

* SQLite documentacion oficial: [SQLite](https://www.sqlite.org/index.html)

* Programa para visualizar la base de datos: [DB Browser for SQLite](https://sqlitebrowser.org/dl/)

### Arquitectura de Django
Consiste en crear aplicaciones dentro del proyecto, las cuales se pueden reutilizar en otros proyectos. Cada aplicacion tiene su propio modelo, vista y controlador. Y se encarga de una funcionalidad especifica. Pueden ser modulos que forman parte de un proyecto.

* crear aplicacion: `python manage.py startapp nombre_aplicacion`

* agregar aplicacion al proyecto: en el archivo settings.py, en la variable INSTALLED_APPS, agregar el nombre de la aplicacion.

````
  INSTALLED_APPS = [
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'nombre_aplicacion',
  ]
````

### Vistas en Django
Las vistas son funciones que se encargan de procesar la informacion y devolver una respuesta al usuario. Se encuentran en el archivo views.py de cada aplicacion.

### Rutas en Django
Las rutas son las url que se ingresan en el navegador para acceder a una vista. Se encuentran en el archivo urls.py de cada aplicacion. Pero se agregan al archivo urls.py del proyecto.

### templates en Django
Los templates son archivos html que se encuentran en la carpeta templates de cada aplicacion. Estos archivos se pueden reutilizar en otras aplicaciones.

* crear carpeta templates: `mkdir templates`

* se crear un documento html y se agrega a la vista

* tambien pueden tener contexto, para consumo de datos

### models en Django

model -> SQL -> DB Table
ORM de Django simplifica el flujo de datos de un modelo a una base 
de datos.

* comando para crear sql: `python manage.py makemigrations`
Este comando se encarga de buscar todos los modelos creados
Si  encuentra un modelo que no tiene una migracion, procede a 
crearle una. Estas son visibles en la carpeta migrations

* comando para crear la tabla: `python manage.py migrate`
Este comando  busca todas las migraciones y si encuentra una
sin ejecutar, la ejecuta creando las tablas correspondientes.

* comando para modificar o actualizar un model: `python manage.py makemigrations` y `python manage.py migrate`

Nota: si se borran archivos de migraciones, se debe eliminar su 
registro en la base de datos. Tambien si se quiere limpiar la caperta
de migraciones al final se recomienda eliminar la base de datos y los 
archivos de migraciones, para luego ejecutar los dos comandos de migraciones. `python manage.py makemigrations` y `python manage.py migrate`

### Django Rest Framework

* [Documentacion](https://www.django-rest-framework.org/tutorial/quickstart/#quickstart)

* [Instalación](https://www.django-rest-framework.org/)

* comando de instalacion: `pip install djangorestframework`

* Agregue `rest_framework`a su INSTALLED_APPS configuración.
Esto el archivo settings.py del proyecto
`
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    ...
]
`
### Crear end points 
Estos son agregados desde cada app creada, y registrados en
el archivo de url del proyecto.

* agregar los modelos, en el archivo admin.py de la app

* se crea en cada app una carpeta api, con 2 archivos
    - views.py : en este archivo se agregan el response y ORM
    - __init__.py 

* en el archivo url, se registran las url para el CRUD

### ViewSet 

* documentacion [ViewSet](https://www.django-rest-framework.org/api-guide/viewsets/)

### ModelViewSet

* documentacion [ModelViewset](https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset)
Automatiza todos los manejos de las operaciones del crud en la api
Tambien permite controlar las solicitudes que se necesitan, definiendolas