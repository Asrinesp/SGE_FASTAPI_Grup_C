# SGE_FASTAPI_Grup_C

####  Nom i cognoms: Akasha Karam

Proyecto de API para la gestión de **clientes** y **menús/productos** utilizando **FastAPI**. 

---

## ESTRUCTURA DEL PROYECTO

![Estructura del proyecto](sge_theBear/IMG%20Client/Estructura.png)

---

## MODELS

Contiene la definición de los **modelos de base de datos** con SQLAlchemy.  
Aquí se definen las tablas, campos y relaciones utilizadas por la API.

### Módulos incluidos:

- `client.py`: modelo de datos del cliente.

  ![Modelo cliente](sge_theBear/IMG%20Client/Client.png)

- `menu.py`: modelo de datos del menú o producto.

  ![Modelo menú](sge_theBear/IMG%20Menu/Menu.png)

---

## SCHEMA

Define los **esquemas de entrada y salida** usando **Pydantic**, lo que garantiza la validación y serialización de los datos en las operaciones de la API.

### Módulos incluidos:

- `client_sch.py`: esquema para los datos del cliente.

  ![Esquema cliente](sge_theBear/IMG%20Client/Client_sch.png)

- `menu_sch.py`: esquema para los datos del menú/producto.

  ![Esquema menú](sge_theBear/IMG%20Menu/Menu_sch.png)

---

##  SERVICES

Contiene la lógica de negocio del proyecto.  
Aquí se implementan las operaciones CRUD (**crear, consultar, modificar y eliminar**) para cada uno de los modelos.

### Módulos incluidos:

- `client.py`: gestiona las operaciones del cliente:
  - Crear nuevo cliente
  
  ![img_1.png](sge_theBear/IMG Client/Añadir.png)
  - Consultar clientes
  ![img_3.png](sge_theBear/IMG Client/Obtener.png)

  - Modificar datos de un cliente
  
  ![img_2.png](sge_theBear/IMG Client/Modificar.png)

  - Eliminar cliente
  
  ![img_4.png](sge_theBear/IMG Client/Eliminar.png)

<br>

- `menu.py`: gestiona las operaciones del menú/producto:
  - Crear nuevo producto
  
  ![img_1.png](sge_theBear/IMG Menu/Añadir.png)
  - Consultar productos
  
  ![img_2.png](sge_theBear/IMG Menu/Modificar.png)
  - Modificar producto
  
  ![img.png](sge_theBear/IMG Menu/Obtener.png)
  - Eliminar producto

  ![img_3.png](sge_theBear/IMG Menu/Eliminar.png)
---

## requirements.txt

Archivo con las dependencias necesarias para ejecutar el proyecto.

El archivo debe contener lo siguiente:
```env
fastapi
uvicorn
dotenv
sqlmodel
psycopg2
```

Para instalar las dependencias:

```env
pip install -r requirements.txt
```

## .env

El archivo .env es una configuración del proyecto para conectarse con la base de datos, creado en la raíz del proyecto.

El archivo debe contener el siguiente código:

```env
DATABASE_URL=postgresql://admin:admin@localhost:5432/the_bear
```
Lo que hacemos es guardar las variables de entorno con la URL indicada en el código.

DATABASE_URL: es la variable que guarda la información para conectarse a la base de datos.

postgresql+psycopg2: se utilizará PostgreSQL a través de psycopg2.

usuario y contraseña: credenciales de acceso a la base de datos. Podemos verlas en el archivo .yml de Docker.

localhost:5432: dirección (en este caso el propio PC del usuario) y el puerto de ejecución de PostgreSQL.

the_bear: nombre de la base de datos.

Para activar el entorno virtual:
```env
python3 -m venv .env
```

## docker-compose.yml

Archivo que configura los servicios necesarios para el proyecto, incluyendo la base de datos y la API.

### Contenido del archivo:
![img.png](sge_theBear/IMG Client/Docker.png)

Un contenedor que ejecuta PostgreSQL con un usuario, una contraseña y una base de datos preconfigurados. Se necesita acativar cuando cuando hagamos uso de fatstAPI.

Para levantar los servicios:

```env
docker compose up -d
```
<br>

## Main.py

El main.py es para iniciar la aplicación FastAPI, configurando las rutas y arrancando el servidor web. Es el punto de entrada del proyecto.

### Rutas para Client

Consultar  clientes

![img.png](sge_theBear/IMG Client/GET.png)

Crear cliente

![img_1.png](sge_theBear/IMG Client/POST.png)

Modificar cliente

![img_2.png](sge_theBear/IMG Client/PUT.png)

Eliminar cliente

![img_3.png](sge_theBear/IMG Client/DELETE.png)

<br>

### Rutas para Menu
Consultar productos del menúgit

![img_1.png](sge_theBear/IMG Menu/GET.png)

Crear producto del menú

![img.png](sge_theBear/IMG Menu/POST.png)

Modificar producto del menú

![img_2.png](sge_theBear/IMG Menu/PUT.png)

Eliminar producto del menú

![img_3.png](sge_theBear/IMG Menu/DELETE.png)

Para comprobar que funciona la API, ejecutar el siguiente comando:

```env
uvicorn Main:app --reload
```