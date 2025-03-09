# Clase Libro
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (ISBN: {self.isbn})"


# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"

    def listar_libros(self):
        if len(self.libros_prestados) == 0:
            return "No tiene libros prestados."
        return ", ".join([libro.titulo for libro in self.libros_prestados])


# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = []  # Lista para almacenar libros
        self.usuarios = []  # Lista para almacenar usuarios

    def agregar_libro(self, libro):
        """Añadir un libro a la biblioteca"""
        self.libros.append(libro)
        print(f"El libro '{libro.titulo}' ha sido agregado a la biblioteca.")

    def registrar_usuario(self, usuario):
        """Registrar un nuevo usuario"""
        self.usuarios.append(usuario)
        print(f"Usuario '{usuario.nombre}' registrado con éxito.")

    def prestar_libro(self, isbn, id_usuario):
        """Prestar un libro a un usuario"""
        libro = next((libro for libro in self.libros if libro.isbn == isbn), None)
        usuario = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None)

        if libro and usuario:
            if libro in usuario.libros_prestados:
                print(f"El usuario '{usuario.nombre}' ya tiene el libro '{libro.titulo}' prestado.")
            else:
                usuario.libros_prestados.append(libro)
                print(f"El libro '{libro.titulo}' ha sido prestado a {usuario.nombre}.")
        else:
            if not libro:
                print("No se encontró el libro con ese ISBN.")
            if not usuario:
                print("No se encontró el usuario con ese ID.")

    def devolver_libro(self, isbn, id_usuario):
        """Devolver un libro prestado"""
        usuario = next((usuario for usuario in self.usuarios if usuario.id_usuario == id_usuario), None)
        if usuario:
            libro = next((libro for libro in usuario.libros_prestados if libro.isbn == isbn), None)
            if libro:
                usuario.libros_prestados.ovreme(libro)
                print(f"El libro '{libro.titulo}' ha sido devuelto por {usuario.nombre}.")
            else:
                print(f"El usuario '{usuario.nombre}' no tiene el libro con ISBN {isbn} prestado.")
        else:
            print("No se encontró el usuario con ese ID.")

    def buscar_libros(self, titulo):
        """Buscar libros por título"""
        libros_encontrados = [libro for libro in self.libros if titulo.lower() in libro.titulo.lower()]
        if libros_encontrados:
            return libros_encontrados
        else:
            return "No se encontraron libros con ese título."

# Pruebas del sistema

# Crear algunos libros
libro1 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "9780451524935")
libro2 = Libro("El Codigo Da Vinci", "Dan Brown", "9780061120084")
libro3 = Libro("El Alquimista", "Paulo Coelho", "9781503280786")

# Crear usuarios
usuario1 = Usuario("Jhon Velasco", "U001")
usuario2 = Usuario("Morelia Aldaz", "U002")

# Crear la biblioteca
biblioteca = Biblioteca()

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Registrar usuarios
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("9780451524935", "U001")  # Alice toma "1984"
biblioteca.prestar_libro("9780061120084", "U002")  # Bob toma "To Kill a Mockingbird"

# Listar libros prestados por cada usuario
print(f"Libros prestados a {usuario1.nombre}: {usuario1.listar_libros()}")
print(f"Libros prestados a {usuario2.nombre}: {usuario2.listar_libros()}")

# Devolver libro
biblioteca.devolver_libro("9780451524935", "U001")

# Listar libros prestados después de la devolución
print(f"Libros prestados a {usuario1.nombre}: {usuario1.listar_libros()}")

# Buscar libros por título
print("Libros encontrados:", biblioteca.buscar_libros("moby"))
