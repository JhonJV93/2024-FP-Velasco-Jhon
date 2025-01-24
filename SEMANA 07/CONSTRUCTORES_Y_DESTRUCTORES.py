# Uso de constructores (__init__) y destructores (__del__)

class ArchivoTemporal:
    def __init__(self, nombre, contenido):

        self.nombre = nombre
        self.contenido = contenido
        self.archivo = open(nombre, 'w')
        self.archivo.write(contenido)
        print(f"Archivo '{self.nombre}' creado con el contenido inicial.")

    def escribir(self, nuevo_contenido):
        """

        """
        self.archivo.write(nuevo_contenido)
        print(f"Nuevo contenido agregado al archivo '{self.nombre}'.")

    def __del__(self):
        """
        Destructor que cierra el archivo y realiza la limpieza.
        """
        if not self.archivo.closed:
            self.archivo.close()
            print(f"Archivo '{self.nombre}' cerrado y recursos liberados.")

class SesionUsuario:
    def __init__(self, usuario):
        """
        Constructor que inicializa la sesión de un usuario.

        """
        self.usuario = usuario
        self.activa = True
        print(f"Sesión iniciada para el usuario '{self.usuario}'.")

    def cerrar_sesion(self):
        """

        """
        if self.activa:
            self.activa = False
            print(f"Sesión cerrada para el usuario '{self.usuario}'.")
        else:
            print(f"La sesión para el usuario '{self.usuario}' ya está cerrada.")

    def __del__(self):
        """
        Destructor que cierra automáticamente la sesión si sigue activa.
        """
        if self.activa:
            print(f"Cerrando automáticamente la sesión para el usuario '{self.usuario}'.")
            self.cerrar_sesion()

# Demostración del uso de las clases ArchivoTemporal y SesionUsuario
if __name__ == "__main__":
    # Crear un objeto de tipo ArchivoTemporal
    archivo_temp = ArchivoTemporal("temp.txt", "Contenido inicial.\n")
    archivo_temp.escribir("Línea adicional.\n")
    del archivo_temp  # El destructor se llama explícitamente

    # Crear un objeto de tipo SesionUsuario
    sesion = SesionUsuario("JHON VELASCO")
    sesion.cerrar_sesion()
    del sesion  # El destructor se llama explícitamente
