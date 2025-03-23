 SGE_FASTAPI_Grup_C

![img.png](img.png)
Se realizó una consulta SQL en pgAdmin para obtener todos los registros de la tabla public.user, ordenados por id de forma ascendente. La consulta devolvió un usuario con nombre "Akasha" y correo "Akasha@gmail.com", lo que confirma que los datos fueron almacenados correctamente en la base de datos.

## Creación de Usuario mediante el Endpoint POST /users
![img_1.png](img_1.png)
Aquí se muestra cómo se hizo una solicitud POST a http://127.0.0.1:8000/users/, enviando un JSON con los datos de un nuevo usuario. La respuesta del servidor indica que el usuario se creó exitosamente, lo que confirma que la API está almacenando nuevos usuarios correctamente en la base de datos.

## Prueba de Creación de Usuario con POST /users en la Documentación de la API
![img_2.png](img_2.png)
Esta imagen muestra la interfaz de la documentación de la API, donde se probó la solicitud POST /users, enviando los parámetros name y email. La respuesta confirma que el usuario fue registrado con éxito, validando que el sistema gestiona correctamente la creación de usuarios.

## Recuperación de Usuarios con GET /users
![img_3.png](im.png)
Se ejecutó una solicitud GET /users para recuperar los usuarios almacenados en la base de datos.

## Consulta de Usuarios en PostgreSQL desde pgAdmin
![img_4.png](img_4.png)
Se realizó una consulta SQL en pgAdmin para obtener todos los registros de la tabla public.user, ordenados por id de forma ascendente. La consulta devolvió un usuario con nombre "Akasha" y correo "Akasha@gmail.com", lo que confirma que los datos fueron almacenados correctamente en la base de datos.





