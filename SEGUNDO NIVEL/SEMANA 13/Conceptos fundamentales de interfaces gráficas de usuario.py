import tkinter as tk

# Función para agregar una nueva nota a la lista
def agregar_nota():
    nota = entrada_nota.get()  # Obtener el texto del campo de entrada
    if nota != "":  # Verificar si el campo no está vacío
        lista_notas.insert(tk.END, nota)  # Agregar la nota a la lista
        entrada_nota.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        print("Por favor ingrese una nota.")  # En caso de estar vacío

# Función para limpiar el campo de texto
def limpiar_entrada():
    entrada_nota.delete(0, tk.END)  # Limpiar el campo de texto

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación de Notas")

# Tamaño de la ventana
ventana.geometry("400x350")

# Etiqueta que indica al usuario qué hacer
etiqueta = tk.Label(ventana, text="Escribe una nota:")
etiqueta.pack(pady=10)

# Campo de texto para escribir la nota
entrada_nota = tk.Entry(ventana, width=40)
entrada_nota.pack(pady=5)

# Botón para agregar la nota
boton_agregar = tk.Button(ventana, text="Agregar Nota", command=agregar_nota)
boton_agregar.pack(pady=5)

# Botón para limpiar el campo de texto
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_entrada)
boton_limpiar.pack(pady=5)

# Lista para mostrar las notas
lista_notas = tk.Listbox(ventana, width=40, height=10)
lista_notas.pack(pady=10)

# Iniciar el bucle principal de la interfaz
ventana.mainloop()
