# Crear y escribir en el archivo my_notes.txt
with open('my_notes.txt', 'w') as file:
    file.write("Nota 1: Salir a trotar 30 minutos.\n")
    file.write("Nota 2: Sacar a pasear a los perros.\n")
    file.write("Nota 3: Realizar los deberes de la Universidad.\n")

# Abrir el archivo y leer el contenido línea por línea
with open('my_notes.txt', 'r') as file:
    for line in file:
        print(line.strip())  # Imprimir cada línea, eliminando espacios en blanco al inicio y al final
