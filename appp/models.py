#Data types and Libraries for the database.
from sqlalchemy import Column, Integer, String, Boolean
from .database import Base
#hello
class Tarea(Base):
    __tablename__ = 'tareas'
    id = Column(Integer, primary_key=True)#It is an integer type, since the id is generally an integer, it is a primary key and cannot be null.
    titulo = Column(String, nullable=False)#The title is in string, it cannot be null and is validated when registering a task that cannot be null.
    descripcion = Column(String, nullable=True)#The description is in string, it cannot be null and is validated when registering a task that cannot be null.
    completada = Column(Boolean, default=False)#The task is in a boolean state, since when completed it will be true while it will not be false.





