class Habitacion:
    def __init__(self, numero, tipo, precio_por_noche, disponible=True):
        """
        Inicializa un objeto Habitacion con un número, tipo, precio por noche y disponibilidad.
        """
        self.numero = numero
        self.tipo = tipo
        self.precio_por_noche = precio_por_noche
        self.disponible = disponible

    def __str__(self):
        """
        Representación en cadena de la habitación para mostrar detalles de la habitación.
        """
        disponibilidad = "Disponible" if self.disponible else "No disponible"
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio_por_noche} por noche - {disponibilidad}"

    def reservar(self):
        """
        Marca la habitación como no disponible.
        """
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"Habitación {self.numero} no está disponible.")

    def liberar(self):
        """
        Libera la habitación, marcándola como disponible.
        """
        self.disponible = True
        print(f"Habitación {self.numero} ahora está disponible.")

class Cliente:
    def __init__(self, nombre):
        """
        Inicializa un cliente con un nombre y una lista de reservas vacía.
        """
        self.nombre = nombre
        self.reservas = []

    def hacer_reserva(self, habitacion, noches):
        """
        El cliente realiza una reserva si la habitación está disponible.
        """
        if habitacion.disponible:
            habitacion.reservar()
            self.reservas.append((habitacion, noches))
            print(f"{self.nombre} ha reservado la habitación {habitacion.numero} por {noches} noches.")
        else:
            print(f"{self.nombre}, no puedes reservar la habitación {habitacion.numero} porque no está disponible.")

    def calcular_total_reserva(self):
        """
        Calcula el costo total de todas las reservas del cliente.
        """
        total = sum(habitacion.precio_por_noche * noches for habitacion, noches in self.reservas)
        return total

    def mostrar_reservas(self):
        """
        Muestra todas las reservas del cliente.
        """
        if not self.reservas:
            print(f"{self.nombre} no tiene reservas.")
        else:
            print(f"Reservas de {self.nombre}:")
            for habitacion, noches in self.reservas:
                print(f"Habitación {habitacion.numero} ({habitacion.tipo}) - {noches} noches - ${habitacion.precio_por_noche * noches}")

class Hotel:
    def __init__(self, nombre):
        """
        Inicializa un hotel con un nombre y una lista de habitaciones.
        """
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion):
        """
        Agrega una habitación al hotel.
        """
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        """
        Muestra todas las habitaciones del hotel.
        """
        print(f"Habitaciones disponibles en el hotel {self.nombre}:")
        for habitacion in self.habitaciones:
            print(habitacion)

# Creación de habitaciones en el hotel
habitacion1 = Habitacion(110, "Individual", 100)
habitacion2 = Habitacion(115, "Doble", 175)
habitacion3 = Habitacion(120, "Suite", 350)

# Creación del hotel
hotel = Hotel("Riveras de Duran")

# Agregar habitaciones al hotel
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)
hotel.agregar_habitacion(habitacion3)

# Mostrar las habitaciones disponibles
hotel.mostrar_habitaciones()

# Creación de clientes
cliente1 = Cliente("Jhon Velasco")
cliente2 = Cliente("Morelia Aldaz")

# Los clientes hacen reservas
cliente1.hacer_reserva(habitacion1, 3)  # Juan Pérez reserva la habitación 101 por 3 noches
cliente2.hacer_reserva(habitacion2, 2)  # Ana Gómez reserva la habitación 102 por 2 noches

# Mostrar las reservas de los clientes
cliente1.mostrar_reservas()
cliente2.mostrar_reservas()

# Calcular el total de las reservas de cada cliente
print(f"\nTotal de la reserva de {cliente1.nombre}: ${cliente1.calcular_total_reserva()}")
print(f"Total de la reserva de {cliente2.nombre}: ${cliente2.calcular_total_reserva()}")

# Liberar una habitación
habitacion1.liberar()

# Mostrar las habitaciones disponibles después de liberar
hotel.mostrar_habitaciones()
