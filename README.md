# PIPS (Miniblog)

Este proyecto es una implementación básica de un miniblog en Django, centrado en la funcionalidad de publicar y comentar entradas. La interfaz de usuario no ha sido el foco principal, el proyecto se enfoca en aspectos fundamentales de Django como la creación de modelos, vistas, migraciones, signals y pruebas.

## Configuración del entorno

1. Clona el repositorio en tu máquina local.
2. Movete al directorio del repo y crea y activa un entorno virtual:

   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

2. Instala las dependencias del proyecto:

   ```bash
   pip install -r requirements.txt
   ```

3. Realiza las migraciones de la base de datos (se realizaran en el archivo db.sqlite3):

   ```bash
   python3 manage.py migrate
   ```

4. Inicia servidor de desarrollo:

   ```bash
   python manage.py runserver
   ```
5. Logueate en la parte de admin:

   ```bash
   localhost:8000/admin
    user: user
    password: user
   ```
6. Testea los endpoints! (Si no estas logeado es posible que no funcionen)

# Endpoints

-  **Listar entradas**

  - URL: `/`
  - Vista: `EntradaListView`
  - Nombre de la ruta: `entrada_list`

- **Crear nueva entrada**

  - URL: `/entrada/new/`
  - Vista: `EntradaCreateView`
  - Nombre de la ruta: `entrada_new`

- **Eliminar entrada**

  - URL: `/entrada/<int:pk>/delete/`
  - Vista: `EntradaDeleteView`
  - Nombre de la ruta: `entrada_delete`

- **Editar entrada**

  - URL: `/entrada/<int:pk>/edit/`
  - Vista: `EntradaUpdateView`
  - Nombre de la ruta: `entrada_edit`

- **Agregar comentario a una entrada**

  - URL: `/entrada/<int:pk>/comentario/new/`
  - Vista: `ComentarioCreateView`
  - Nombre de la ruta: `comentario_new`

- **Eliminar comentario**

  - URL: `/comentario/<int:pk>/delete/`
  - Vista: `ComentarioDeleteView`
  - Nombre de la ruta: `comentario_delete`

# Miniblog API Documentation

## Autenticación

### Obtener Token de Acceso

#### Endpoint

- **Método HTTP**: `POST`
- **URL**: `/api-token-auth/`

#### Parámetros del Cuerpo (Body)

- `username`: Nombre de usuario (Tipo: String)
- `password`: Contraseña del usuario (Tipo: String)

#### Headers

Ninguno

#### Respuesta Exitosa

- **Código de Estado HTTP**: `200 OK`
- **Contenido del Cuerpo (Body)**:

  ```json
  {
      "token": "YOUR_ACCESS_TOKEN_HERE"
  }
  ```

**Nota**: Utilice el token de acceso recibido en el encabezado `Authorization` para las solicitudes subsiguientes. El formato debe ser `Token YOUR_ACCESS_TOKEN_HERE`.

---

# 📚 Categoría

###  📌 Listar Todas las Categorías

#### Endpoint

- **Método HTTP**: `GET`
- **URL**: `/api/categorias/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Respuesta Exitosa

- **Código de Estado HTTP**: `200 OK`
- **Contenido del Cuerpo (Body)**:

  ```json
  [
      {
          "id": 1,
          "nombre": "Tecnología"
      },
      // ... más categorías
  ]
  ```

### ➕ Crear una Nueva Categoría

#### Endpoint

- **Método HTTP**: `POST`
- **URL**: `/api/categorias/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Parámetros del Cuerpo (Body)

- `nombre`: Nombre de la nueva categoría (Tipo: String)

#### Respuesta Exitosa

- **Código de Estado HTTP**: `201 Created`
- **Contenido del Cuerpo (Body)**:

  ```json
  {
      "id": 3,
      "nombre": "Nueva Categoría"
  }
  ```

###  🔄 Actualizar una Categoría

#### Endpoint

- **Método HTTP**: `PUT`
- **URL**: `/api/categorias/{id}/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Parámetros del Cuerpo (Body)

- `nombre`: Nuevo nombre de la categoría (Tipo: String)

#### Respuesta Exitosa

- **Código de Estado HTTP**: `200 OK`
- **Contenido del Cuerpo (Body)**:

  ```json
  {
      "id": 3,
      "nombre": "Categoría Actualizada"
  }
  ```

### ❌ Eliminar una Categoría

#### Endpoint

- **Método HTTP**: `DELETE`
- **URL**: `/api/categorias/{id}/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Respuestas

##### Exitosa

- **Código de Estado HTTP**: `204 No Content`
- **Contenido del Cuerpo (Body)**:

  ```json
  {
      "detail": "El objeto se eliminó con éxito."
  }
  ```

---
# 📝 Entrada

###  📌 Listar Todas las Entradas

#### Endpoint

- **Método HTTP**: `GET`
- **URL**: `/api/entradas/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Respuesta Exitosa

- **Código de Estado HTTP**: `200 OK`
- **Contenido del Cuerpo (Body)**:

  ```json
  [
      {
          "id": 1,
          "titulo": "Primera Entrada",
          "contenido": "Contenido de la primera entrada",
          "autor": 1,
          "categoria": 1
      },
      // ... más entradas
  ]
  ```

### ➕ Crear una Nueva Entrada

#### Endpoint

- **Método HTTP**: `POST`
- **URL**: `/api/entradas/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Parámetros del Cuerpo (Body)

- `titulo`: Título de la nueva entrada (Tipo: String)
- `contenido`: Contenido de la nueva entrada (Tipo: String)
- `categoria`: ID de la categoría asociada (Tipo: Integer)

#### Respuesta Exitosa

- **Código de Estado HTTP**: `201 Created`
- **Contenido del Cuerpo (Body)**:

  ```json
  {
      "id": 2,
      "titulo": "Segunda Entrada",
      "contenido": "Contenido de la segunda entrada",
      "autor": 1,
      "categoria": 1
  }
  ```

###  🔄 Actualizar una Entrada

#### Endpoint

- **Método HTTP**: `PUT`
- **URL**: `/api/entradas/{id}/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Parámetros del Cuerpo (Body)

- `titulo`: Nuevo título de la entrada (Tipo: String)
- `contenido`: Nuevo contenido de la entrada (Tipo: String)
- `categoria`: ID de la nueva categoría asociada (Tipo: Integer)

#### Respuesta Exitosa

- **Código de Estado HTTP**: `200 OK`
- **Contenido del Cuerpo (Body)**:

  ```json
  {
      "id": 2,
      "titulo": "Entrada Actualizada",
      "contenido": "Contenido actualizado",
      "autor": 1,
      "categoria": 2
  }
  ```

### ❌ Eliminar una Entrada

#### Endpoint

- **Método HTTP**: `DELETE`
- **URL**: `/api/entradas/{id}/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Respuesta Exitosa

- **Código de Estado HTTP**: `204 No Content`
- **Contenido del Cuerpo (Body)**:

  ```json
  {
      "detail": "El objeto se eliminó con éxito."
  }
  ```

---
# 💬 Comentario

###  📌 Listar Todos los Comentarios

#### Endpoint

- **Método HTTP**: `GET`
- **URL**: `/api/comentarios/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Respuesta Exitosa

- **Código de Estado HTTP**: `200 OK`
- **Contenido del Cuerpo (Body)**:

  ```json
  [
      {
          "id": 1,
          "texto": "Primer comentario",
          "autor": 1,
          "entrada": 1
      },
      // ... más comentarios
  ]
  ```

### ➕ Crear un Nuevo Comentario

#### Endpoint

- **Método HTTP**: `POST`
- **URL**: `/api/comentarios/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Parámetros del Cuerpo (Body)

- `texto`: Texto del nuevo comentario (Tipo: String)
- `entrada`: ID de la entrada asociada (Tipo: Integer)

#### Respuesta Exitosa

- **Código de Estado HTTP**: `201 Created`
- **Contenido del Cuerpo (Body)**:

  ```json
  {
      "id": 2,
      "texto": "Segundo comentario",
      "autor": 1,
      "entrada": 1
  }
  ```

###  🔄 Actualizar un Comentario

#### Endpoint

- **Método HTTP**: `PUT`
- **URL**: `/api/comentarios/{id}/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Parámetros del Cuerpo (Body)

- `texto`: Nuevo texto del comentario (Tipo: String)

#### Respuesta Exitosa

- **Código de Estado HTTP**: `200 OK`
- **Contenido del Cuerpo (Body)**:

  ```json
  {
      "id": 2,
      "texto": "Comentario actualizado",
      "autor": 1,
      "entrada": 1
  }
  ```

### ❌ Eliminar un Comentario

#### Endpoint

- **Método HTTP**: `DELETE`
- **URL**: `/api/comentarios/{id}/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Respuesta Exitosa

- **Código de Estado HTTP**: `204 No Content`
- **Contenido del Cuerpo (Body)**:

  ```json
  {
      "detail": "El objeto se eliminó con éxito."
  }
  ```
---
# 👤 Usuario

###  📌 Listar Todos los Usuarios

#### Endpoint

- **Método HTTP**: `GET`
- **URL**: `/api/usuarios/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Respuesta Exitosa

- **Código de Estado HTTP**: `200 OK`
- **Contenido del Cuerpo (Body)**:

  ```json
  [
      {
          "id": 1,
          "username": "usuario1",
          "email": "usuario1@email.com"
      },
      // ... más usuarios
  ]
  ```

### ➕ Crear un Nuevo Usuario

#### Endpoint

- **Método HTTP**: `POST`
- **URL**: `/api/usuarios/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Parámetros del Cuerpo (Body)

- `username`: Nombre de usuario (Tipo: String)
- `email`: Correo electrónico (Tipo: String)
- `password`: Contraseña (Tipo: String)

#### Respuesta Exitosa

- **Código de Estado HTTP**: `201 Created`
- **Contenido del Cuerpo (Body)**:

  ```json
  {
      "id": 2,
      "username": "usuario2",
      "email": "usuario2@email.com"
  }
  ```

###  🔄 Actualizar un Usuario

#### Endpoint

- **Método HTTP**: `PUT`
- **URL**: `/api/usuarios/{id}/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Parámetros del Cuerpo (Body)

- `username`: Nuevo nombre de usuario (Tipo: String)
- `email`: Nuevo correo electrónico (Tipo: String)

#### Respuesta Exitosa

- **Código de Estado HTTP**: `200 OK`
- **Contenido del Cuerpo (Body)**:

  ```json
  {
      "id": 2,
      "username": "usuario2_actualizado",
      "email": "usuario2_actualizado@email.com"
  }
  ```

### ❌ Eliminar un Usuario

#### Endpoint

- **Método HTTP**: `DELETE`
- **URL**: `/api/usuarios/{id}/`

#### Headers

- `Authorization`: `Token YOUR_ACCESS_TOKEN_HERE`

#### Respuesta Exitosa

- **Código de Estado HTTP**: `204 No Content`
---
