import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "La tarea no puede estar vacía.")

def mark_completed():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(selected, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcar como completada.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

def add_task_enter(event):
    add_task()

# Crear la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")

# Entrada de texto
entry = tk.Entry(root, width=40)
entry.pack(pady=10)
entry.bind("<Return>", add_task_enter)

# Botones
frame = tk.Frame(root)
frame.pack()

add_button = tk.Button(frame, text="Añadir Tarea", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

complete_button = tk.Button(frame, text="Marcar como Completada", command=mark_completed)
complete_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(frame, text="Eliminar Tarea", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

# Lista de tareas
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
