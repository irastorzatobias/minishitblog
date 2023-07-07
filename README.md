# PIPS (Miniblog)

Este proyecto es una implementación básica de un miniblog en Django, centrado en la funcionalidad de publicar y comentar entradas. La interfaz de usuario no ha sido el foco principal, el proyecto se enfoca en aspectos fundamentales de Django como la creación de modelos, vistas, migraciones, signals y pruebas.

## Configuración del entorno

1. Clona el repositorio en tu máquina local.
2. Mueve al directorio y crea y activa un entorno virtual:

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
6. Testea los endpoints!

# Endpoints

- **Listar entradas**

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


