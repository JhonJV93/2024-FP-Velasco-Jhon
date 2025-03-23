import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry

# Función para agregar un evento
def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        treeview.insert("", "end", values=(fecha, hora, descripcion))
        entry_fecha.delete(0, tk.END)
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")

# Función para eliminar un evento seleccionado
def eliminar_evento():
    seleccion = treeview.selection()
    if seleccion:
        treeview.delete(seleccion)
    else:
        messagebox.showwarning("Advertencia", "Por favor, seleccione un evento para eliminar.")

# Función para salir de la aplicación
def salir():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Agenda Personal")

# Crear un frame para los campos de entrada
frame_entrada = tk.Frame(root)
frame_entrada.pack(pady=10)

# Etiquetas y campos de entrada
label_fecha = tk.Label(frame_entrada, text="Fecha:")
label_fecha.grid(row=0, column=0, padx=5, pady=5)
entry_fecha = DateEntry(frame_entrada, width=12, background='darkblue', foreground='white', borderwidth=2)
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

label_hora = tk.Label(frame_entrada, text="Hora (HH:MM):")
label_hora.grid(row=1, column=0, padx=5, pady=5)
entry_hora = tk.Entry(frame_entrada)
entry_hora.grid(row=1, column=1, padx=5, pady=5)

label_descripcion = tk.Label(frame_entrada, text="Descripción:")
label_descripcion.grid(row=2, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(frame_entrada)
entry_descripcion.grid(row=2, column=1, padx=5, pady=5)

# Crear botones
frame_botones = tk.Frame(root)
frame_botones.pack(pady=10)

btn_agregar = tk.Button(frame_botones, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_botones, text="Eliminar Evento Seleccionado", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
btn_salir.grid(row=0, column=2, padx=10)

# Crear un frame para el Treeview (lista de eventos)
frame_eventos = tk.Frame(root)
frame_eventos.pack(pady=10)

# Crear el Treeview para mostrar los eventos
columnas = ("Fecha", "Hora", "Descripción")
treeview = ttk.Treeview(frame_eventos, columns=columnas, show="headings")

# Configurar las columnas
for col in columnas:
    treeview.heading(col, text=col)
    treeview.column(col, width=100)

treeview.pack()

# Ejecutar la aplicación
root.mainloop()
