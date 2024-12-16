from abc import ABC, abstractmethod  # Para la abstracción


# Encapsulamiento:
class Vehiculo(ABC):
    def __init__(self, marca, modelo, color):

        self.__marca = marca
        self.__modelo = modelo
        self.__color = color


    def get_marca(self):
        return self.__marca

    def get_modelo(self):
        return self.__modelo

    def get_color(self):
        return self.__color


    def set_color(self, color):
        self.__color = color

    @abstractmethod
    def arrancar(self):

        pass

    @abstractmethod
    def detener(self):

        pass


# Herencia y Polimorfismo
class Coche(Vehiculo):
    def __init__(self, marca, modelo, color, puertas):
        super().__init__(marca, modelo, color)
        self.puertas = puertas

    def arrancar(self):
        print(f"El coche {self.get_marca()} {self.get_modelo()} ha arrancado.")

    def detener(self):
        print(f"El coche {self.get_marca()} {self.get_modelo()} se ha detenido.")

    def abrir_puertas(self):
        print(f"Abriendo {self.puertas} puertas del coche.")


# Herencia y Polimorfismo:
class Moto(Vehiculo):
    def __init__(self, marca, modelo, color, cilindrada):
        super().__init__(marca, modelo, color)
        self.cilindrada = cilindrada

    def arrancar(self):
        print(f"La moto {self.get_marca()} {self.get_modelo()} ha arrancado.")

    def detener(self):
        print(f"La moto {self.get_marca()} {self.get_modelo()} se ha detenido.")

    def hacer_acelerar(self):
        print(f"La moto {self.get_marca()} acelera a máxima potencia.")


# Herencia y Polimorfismo
class Camion(Vehiculo):
    def __init__(self, marca, modelo, color, carga_maxima):
        super().__init__(marca, modelo, color)
        self.carga_maxima = carga_maxima

    def arrancar(self):
        print(f"El camión {self.get_marca()} {self.get_modelo()} ha arrancado.")

    def detener(self):
        print(f"El camión {self.get_marca()} {self.get_modelo()} se ha detenido.")

    def cargar(self):
        print(f"El camión {self.get_marca()} está cargando hasta {self.carga_maxima} kg.")


def iniciar_vehiculo(vehiculo):

    vehiculo.arrancar()
    vehiculo.detener()


# Crear instancias de las clases
coche = Coche("Toyota", "Fortuner", "Negro", 4)
moto = Moto("Honda", "CBR600", "Blanca", 600)
camion = Camion("Hino", "GH", "Blanco", 20000)

# Usar los métodos de las clases
print(f"El coche tiene {coche.get_marca()} {coche.get_modelo()} de color {coche.get_color()}.")
coche.abrir_puertas()
iniciar_vehiculo(coche)

print(f"\nLa moto tiene {moto.get_marca()} {moto.get_modelo()} de color {moto.get_color()}.")
moto.hacer_acelerar()
iniciar_vehiculo(moto)

print(f"\nEl camión tiene {camion.get_marca()} {camion.get_modelo()} de color {camion.get_color()}.")
camion.cargar()
iniciar_vehiculo(camion)
