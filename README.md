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
* Paso 5: Se instaló el comando de las librerías y las base de datos en python "pip install streamlit sqlalchemy sqlite3" 
* Paso 6: Se instalaron otros comandos como "pip install pymysql", "pip install psycopg2-binary".
* Paso 7: Se instalaron las dependencias para crear el entorno virtual "python -m venv venv".
* Paso 8: Posteriormente a instalar aparece para activar el entorno virtual con el comando ".\venv\Scripts\activate" en windows.
* Paso 9: Se instalaron estos comandos como: "pip install -r requirements.txt" para ver las dependencias que se instalaron, "pip install streamlit sqlalchemy pandas", "pip install pytest pylint", "pip list"

![image](https://github.com/user-attachments/assets/35e8e6d9-4b4e-4a60-81a8-69ac8441aadb)
