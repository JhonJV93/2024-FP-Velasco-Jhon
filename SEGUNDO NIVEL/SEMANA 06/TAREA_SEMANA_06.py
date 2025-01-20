# Ejemplo de un programa en Python que demuestra herencia, encapsulación y polimorfismo

# Clase base
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.__edad = edad    # Atributo privado (encapsulación)

    # Método público para acceder al atributo privado
    def obtener_edad(self):
        return self.__edad

    # Método público para modificar el atributo privado
    def establecer_edad(self, edad):
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser positiva.")

    def descripcion(self):
        return f"Soy {self.nombre} y tengo {self.__edad} años."

# Clase derivada (Herencia)
class Estudiante(Persona):
    def __init__(self, nombre, edad, curso):
        super().__init__(nombre, edad)
        self.curso = curso  # Atributo adicional

    # Sobrescritura de método (Polimorfismo)
    def descripcion(self):
        return f"Soy {self.nombre}, tengo {self.obtener_edad()} años y estudio {self.curso}."

# Clase derivada adicional para demostrar polimorfismo
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    # Sobrescritura de método (Polimorfismo)
    def descripcion(self):
        return f"Soy {self.nombre}, tengo {self.obtener_edad()} años y enseño {self.materia}."

# Programa principal
if __name__ == "__main__":
    # Crear una instancia de la clase base
    persona = Persona("Jhon Velasco", 32)
    print(persona.descripcion())

    # Modificar un atributo privado usando los métodos
    persona.establecer_edad(32)
    print(f"Nueva edad: {persona.obtener_edad()}")

    # Crear una instancia de la clase derivada Estudiante
    estudiante = Estudiante("Morelia Aldaz", 29, "Matemáticas")
    print(estudiante.descripcion())

    # Crear una instancia de la clase derivada Profesor
    profesor = Profesor("Jose Delgado", 45, "Programacion")
    print(profesor.descripcion())

    # Demostración de polimorfismo
    personas = [persona, estudiante, profesor]
    for p in personas:
        print(p.descripcion())
