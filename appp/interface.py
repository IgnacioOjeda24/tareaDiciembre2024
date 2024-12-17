#Library to make the graphical interface in Tkinter.
import tkinter as tk
#In Tkinter you have to request the messagebox for text messages to appear
from tkinter import messagebox
from .database import session
from .models import Tarea
#The json library was imported to export and import the json file.
import json

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task for December 16")#Title above.
        self.root.geometry("800x800")#Size of the graphical interface.
        self.root.configure(bg="#f3ff57")#Background color of the graphical interface.

        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        menu_file = tk.Menu(self.menu, tearoff=0)
        menu_file.add_command(label="Export tasks", command=self.exportar_tareas)
        menu_file.add_command(label="Import tasks", command=self.importar_tareas)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.root.quit)
        self.menu.add_cascade(label="File", menu=menu_file)


        self.header = tk.Label(
            root, text="Task manager", font=("Times New Roman", 26, "bold"),
            bg="#40e0d0", fg="#f3ff57", pady=10)
        self.header.pack(fill=tk.X)

        #Background color.
        self.form_frame = tk.Frame(root, bg="#6600a1")
        self.form_frame.pack(pady=10)
        self.titulo_label = tk.Label(self.form_frame, text="Title:", bg="#40e0d0", font=("Times New Roman", 12), fg="#f3ff57")
        self.titulo_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.titulo_entry = tk.Entry(self.form_frame, width=30, font=("Times New Roman", 12), bg="#ffffff", fg="#000000", insertbackground="white")
        self.titulo_entry.grid(row=0, column=1, padx=5, pady=5)

        self.descripcion_label = tk.Label(self.form_frame, text="Description:", bg="#40e0d0", font=("Times New Roman", 12), fg="#f3ff57")
        self.descripcion_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.descripcion_entry = tk.Entry(self.form_frame, width=30, font=("Times New Roman", 12), bg="#ffffff", fg="#000000", insertbackground="white")
        self.descripcion_entry.grid(row=1, column=1, padx=5, pady=5)

        self.add_button = tk.Button(
            self.form_frame, text="Add task", bg="#40e0d0", fg="black", font=("Times New Roman", 12, "bold"),
            relief="raised", command=self.agregar_tarea)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        #Background color.
        self.list_frame = tk.Frame(root, bg="#cca9dd")
        self.list_frame.pack(pady=10)
        self.tareas_listbox = tk.Listbox(self.list_frame, width=50, height=10, font=("Times New Roman", 12), bg="#6600a1", fg="#f0f0f0", selectbackground="#4CAF50", selectforeground="white")
        self.tareas_listbox.pack(side=tk.LEFT, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self.list_frame)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.tareas_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tareas_listbox.yview)


        self.actions_frame = tk.Frame(root, bg="#cca9dd")
        self.actions_frame.pack(pady=20)
        self.complete_button = tk.Button(
            self.actions_frame, text="Complete tasks", bg="#40e0d0", fg="white", font=("Times New Roman", 12, "bold"),
            relief="raised", command=self.completar_tarea)
        self.complete_button.grid(row=0, column=0, padx=10, pady=5)

        self.delete_button = tk.Button(
            self.actions_frame, text="Delete completed tasks", bg="#40e0d0", fg="white", font=("Times New Roman", 12, "bold"),
            relief="raised", command=self.eliminar_tareas_completadas)
        self.delete_button.grid(row=0, column=1, padx=10, pady=5)


        self.file_actions_frame = tk.Frame(root, bg="#cca9dd")
        self.file_actions_frame.pack(pady=10)
        self.export_button = tk.Button(
            self.file_actions_frame, text="Export tasks", bg="#40e0d0", fg="white", font=("Times New Roman", 12, "bold"),
            relief="raised", command=self.exportar_tareas)
        self.export_button.grid(row=0, column=0, padx=10, pady=5)

        self.import_button = tk.Button(
            self.file_actions_frame, text="Import tasks", bg="#40e0d0", fg="white", font=("Times New Roman", 12, "bold"),
            relief="raised", command=self.importar_tareas)
        self.import_button.grid(row=0, column=1, padx=10, pady=5)


        self.exit_button = tk.Button(
            root, text="Exit", bg="#40e0d0", fg="white", font=("Times New Roman", 12, "bold"),
            relief="raised", command=self.salir)
        self.exit_button.pack(pady=24)

        self.cargar_tareas()


    def agregar_tarea(self):
        titulo = self.titulo_entry.get().strip()
        descripcion = self.descripcion_entry.get().strip()
        if titulo and descripcion:
            nueva_tarea = Tarea(titulo=titulo, descripcion=descripcion)
            session.add(nueva_tarea)
            session.commit()
            self.titulo_entry.delete(0, tk.END)
            self.descripcion_entry.delete(0, tk.END)
            self.cargar_tareas()
            messagebox.showinfo("Sucess", "The task has been added successfully.")
        else:
            messagebox.showwarning("Warning", "Title and description cannot be empty.")

    def cargar_tareas(self):
        self.tareas_listbox.delete(0, tk.END)
        tareas = session.query(Tarea).all()
        for tarea in tareas:
            estado = "[✔]" if tarea.completada else "[ ]"
            self.tareas_listbox.insert(tk.END, f"{tarea.id} :{estado}  {tarea.titulo} - {tarea.descripcion}")

    def completar_tarea(self):
        seleccion = self.tareas_listbox.curselection()
        if seleccion:
             tarea_texto = self.tareas_listbox.get(seleccion[0])
             try:
                tarea_id = int(tarea_texto.split(" :")[0].strip())
                tarea = session.query(Tarea).filter_by(id=tarea_id).first()
                if tarea and not tarea.completada:
                     tarea.completada = True
                     session.commit()
                     self.cargar_tareas()
                     messagebox.showinfo("Éxito", "Tarea marcada como completada.")
                else:
                     messagebox.showwarning("Advertencia", "La tarea ya está completada o no se encontró.")
             except ValueError:
                  messagebox.showwarning("Advertencia", "No se pudo obtener el ID de la tarea.")
        else:
            messagebox.showwarning("Advertencia", "Selecciona una tarea para completar.")

    def eliminar_tareas_completadas(self):
        tareas_completadas = session.query(Tarea).filter_by(completada=True).all()
        if tareas_completadas:
            for tarea in tareas_completadas:
                session.delete(tarea)
            session.commit()
            self.cargar_tareas()
            messagebox.showinfo("Success", "Tasks completed successfully deleted.")
        else:
            messagebox.showwarning("Advertencia", "No hay tareas completadas para eliminar.")

    def exportar_tareas(self):
        tareas = session.query(Tarea).all()
        datos = [
            {
                "id": tarea.id,
                "titulo": tarea.titulo,
                "descripcion": tarea.descripcion,
                "completada": tarea.completada,
            }
            for tarea in tareas
        ]
        with open("data/tareas.json", "w") as archivo:
            json.dump(datos, archivo, indent=4)
        messagebox.showinfo("Success", "Tasks exported to 'data/tasks.json'.")

    def importar_tareas(self):
        try:
            with open("data/tareas.json", "r") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    if not session.query(Tarea).filter_by(id=item["id"]).first():
                        nueva_tarea = Tarea(
                            id=item["id"],
                            titulo=item["titulo"],
                            descripcion=item["descripcion"],
                            completada=item["completada"],
                        )
                        session.add(nueva_tarea)
                session.commit()
            self.cargar_tareas()
            messagebox.showinfo("Success", "Tasks imported from 'data/tasks.json'.")
        except FileNotFoundError:
            messagebox.showwarning("Warning", "The file 'data/tareas.json' was not found.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error reading JSON file.")

    def salir(self):
        self.root.quit()







