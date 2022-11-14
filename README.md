### Integrante: Molle Mathias.

*En la base de datos hay 2 usuarios que son los siguiente:*

#### Usuario administrador

username = admin
pass = 123

#### Usuario normal

username = user
pass = user1234

 #### Directorio de proyecto

 - PROYECTOFINAL  *(Directorio Raiz)
      - urls.py (Contiene url admin y home)
 - home  *(Directorio de Modulo General)
      - static (Directorio que contiene CSS, JS y Assets)
      - templates (Directorio que contiene templates de la app)
          - acerca_de_mi.html (Acerca del alumno)
          - delete_servs.html (Para eliminar servicios ofrecidos)
          - edit_servs.html (Para editar servicios ofrecidos)
          - index.html (Página inicial)
          - input_servs.html (Para crear servicios)
          - view_serv.html (Para ver servicio puntual de la BD)
          - view_servs.html (Visualiza datos de BD)
          Padres 
              - base.html (Bloques de Herencia de padre)
      - forms.py (Contiene Clase para Busqueda de usuarios)
      - models.py (Contiene clase Servs con campos de datos requeridos)
      - urls.py (contiene urls de index, acerca de, vista, ingreso, edición, elimnación de los servicios que se ingresan en el blog
      - views.py (Contiene funciones de visualizacion y creacion de los servivios que el blog ofrece)
 - db.sqlite3  (Base de datos vacia, rellenar con servicios desde Oferta tu servicio)
 - Requirements.txt  (Requerimientos minimos para iniciar el proyecto)

#### tener en cuenta que los servicios son los que ofrecen lo usuaios que utilizan la página