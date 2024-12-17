**Instrucciones del proyecto I:**

Desarrolla una Aplicación de Gestión de Tareas.

Crea una aplicación en Python que permita a los usuarios gestionar sus tareas diarias. La aplicación debe incluir las siguientes funcionalidades:

1. Agregar Tareas:
        Permitir al usuario agregar nuevas tareas con un título y una descripción (Hay que validar antes de agregar por ejemplo que los valores no pueden ser vacíos).
2. Listar Tareas:
        Mostrar todas las tareas agregadas con su estado (pendiente o completada) Se muestran el check si es que está completo, su número de id, título de la tarea, descripción de la tarea.
3. Marcar Tareas como Completadas:
        Permitir al usuario marcar una tarea como completada (Marcar una sola tarea).
4. Eliminar Tareas:
        Permitir al usuario eliminar tareas completadas (Eliminar todas las tareas completadas).
5. Guardar y Cargar Tareas:
        Puede exportar las tareas en un archivo e importar las desde el mismo archivo (Se hace de un archivo json).
6. Interfaz
        Puedes crear una interfaz gráfica (ideal streamlit, Sin embargo se utilizó tkinder.)

Requisitos Técnicos:

* Utiliza estructuras de datos como listas y diccionarios.
* Maneja excepciones para asegurar que la aplicación no se cierre inesperadamente.
* Utiliza módulos estándar de Python como json para importar y exportar tareas (Se cumple).
* Utiliza una conexión a una base de datos sql para tener persistencia de datos (ideal SQLAlchemy).

**Pasos para conseguir el resultado del producto**

* Paso 1: Se creó la carpeta raíz "PROYECTO 1 CURSO AI PYTHON"
* Paso 2: Se crearon dentro de la carpeta appp como los archivos como __pycache__, __init__.py, database.py, db_utils.py y models.py.
* Paso 3: Se creó la carpeta data para tener el archivo tareas.db realizado en SQLAlchemy.
* Paso 4: Se creó el archivo main.py dentro de la carpeta raíz para ejecutar la interfaz gráfica del programa.
* Paso 5: Se instaló el comando de las librerías y las base de datos en python "pip install streamlit sqlalchemy" 
* Paso 6: Se instalaron otros comandos como "pip install pymysql".
* Paso 7: Se instalaron las dependencias para crear el entorno virtual "python -m venv venv".
* Paso 8: Posteriormente a instalar aparece para activar el entorno virtual con el comando ".\venv\Scripts\activate" en windows.
* Paso 9: Se instalaron estos comandos como: "pip install -r requirements.txt" para ver las dependencias que se instalaron, "pip install pytest pylint", "pip list"

**Evidencias de fotos**
Ver la versión de Python que es Python 3.13.1

![C1](https://github.com/user-attachments/assets/b79a109a-cf18-406c-80d5-486b70c9834c)

Ver la instalación de streamlit sqlalchemy

![C2](https://github.com/user-attachments/assets/e952165c-8a03-40a4-a4cc-04e788abe368)

Segunda parte.

![C3](https://github.com/user-attachments/assets/c6f4291a-123d-4781-b259-0fa1478309c2)

Se instala el comando pip install pymysql.

![C4](https://github.com/user-attachments/assets/dc63a4be-3795-43ca-b232-749e3e75fce0)

Se ejecutó el comando 

![C5](https://github.com/user-attachments/assets/e048f4a3-bb18-47c5-a3d0-a3770c82a49c)

Su resultado es:

![C6](https://github.com/user-attachments/assets/5f0554a9-6468-416c-93a4-0f7f16432a9c)

Se ejecuta el comando  .\venv\Scripts\activate

![C7](https://github.com/user-attachments/assets/4ccb51b1-7fec-45c6-b202-de06e7375bcd)

Listas de librerías instaladas.

![C8](https://github.com/user-attachments/assets/a25bf0c3-d600-4976-8ca4-3a122d29f795)

Parte 2

![C9](https://github.com/user-attachments/assets/2cfc8a63-20c1-4465-b812-0b77ad6242a2)

Pantallas.

Inicio y se muestra las tareas actuales.

![Capture0](https://github.com/user-attachments/assets/7e6357bf-eda2-472a-a54b-c32f8cea7293)

Agregando una tarea.

![C11](https://github.com/user-attachments/assets/2965d351-ab29-4fcb-b0d7-a64219dc0967)

Se agregó la tarea correctamente.

![Capture001](https://github.com/user-attachments/assets/27c6fd32-33a4-4b08-8665-bda8d05a8147)

Se eliminó las tareas completadas.

![C13](https://github.com/user-attachments/assets/a45a08dd-bba3-4919-ae41-79f7cdbdf803)

Exportado correctamente

![C14](https://github.com/user-attachments/assets/74180fdd-5914-43a3-bff1-13d830058269)

Importado correctamente.

![Capture001](https://github.com/user-attachments/assets/c6066e91-30a2-4139-8ffd-ad0cf47e55e1)
























