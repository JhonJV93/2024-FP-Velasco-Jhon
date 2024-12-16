#PROGRAMACION ORIEMNTADA A OBJETOS

class Clima:
    def __init__(self):
        """
        El constructor de la clase Clima inicializa una lista vacía de temperaturas.
        Esta lista se llenará con las temperaturas diarias de la semana.
        """
        self.temperaturas = []  # Lista para almacenar las temperaturas de los 7 días

    def ingresar_temperaturas(self):
        """
        Este método solicita al usuario las temperaturas de los 7 días de la semana.
        Cada temperatura ingresada se almacena en la lista 'temperaturas'.
        """
        for i in range(7):
            # Solicitar la temperatura para cada día y agregarla a la lista
            temp = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        """
        Este método calcula el promedio de las temperaturas registradas.
        Retorna el promedio de las temperaturas de la semana.
        """
        if len(self.temperaturas) == 7:
            # Calcular el promedio sumando las temperaturas y dividiendo por 7
            promedio = sum(self.temperaturas) / len(self.temperaturas)
            return promedio
        else:
            raise ValueError("Debe ingresar exactamente 7 temperaturas")

    def mostrar_promedio(self):
        """
        Este método calcula y muestra el promedio semanal de las temperaturas.
        """
        # Llamamos a calcular_promedio para obtener el promedio y luego lo mostramos
        promedio = self.calcular_promedio()
        print(f"La temperatura promedio semanal es: {promedio:.2f} °C")

# Función principal que coordina el flujo del programa
def main():
    """
    Función principal que crea un objeto de la clase Clima, ingresa las temperaturas
    y muestra el promedio semanal.
    """
    # Crear un objeto de la clase Clima
    clima = Clima()

    # Ingresar las temperaturas de los 7 días
    clima.ingresar_temperaturas()

    # Mostrar el promedio semanal calculado
    clima.mostrar_promedio()

# Ejecutar el programa
if __name__ == "__main__":
    main()  # Llamamos a la función principal para iniciar el programa
