#Application to open the program in the Tkinter graphical interface.
#It comes from the database file in the Appp folder.
from appp.database import Base, engine
#It comes from the interface.py file in the Appp folder.
from appp.interface import TaskManagerApp
#Import the tkinter library to show the graphical interface.
import tkinter as tk

# The database is initialized.
def initialize_database():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    initialize_database()
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()















