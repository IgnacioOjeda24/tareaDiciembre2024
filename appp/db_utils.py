#Libraries for importing and exporting JSON files..
import json
#Import Tasks from the models file in the Appp folder.
from appp.models import Tarea
#Import tasks from the database file in the Appp folder.
from appp.database import SessionLocal
#Libraries for making database queries.
from sqlalchemy.orm import Session

# Function to export the tasks to a JSON file.
def Export_tasks_to_a_JSON_file():
    with Session(SessionLocal()) as session:
        tareas = session.query(Tarea).all()
        tareas_data = [
            {
                "id": tarea.id,#id attribute
                "titulo": tarea.titulo,#title attribute
                "descripcion": tarea.descripcion,#description attribute
                "completada": tarea.completada #Completed atrribute.
            } for tarea in tareas
        ]   
    with open('data/tareas.json', 'w') as file:
        json.dump(tareas_data, file, indent=4)

#Import tasks from a JSON file so that they appear in the list of completed or pending tasks.
def import_tasks_json():
    #To read the tasks.json file
    with open('data/tareas.json', 'r') as file:
        tareas_data = json.load(file)

    with Session(SessionLocal()) as session:
        for tarea_data in tareas_data:
            tarea = Tarea(
                id=tarea_data["id"],#id attribute
                titulo=tarea_data["titulo"],#title attribute
                descripcion=tarea_data["descripcion"],#description attribute
                completada=tarea_data["completada"]#Completed atrribute.
            )
            session.add(tarea)
        session.commit()



