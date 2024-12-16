#PROGRAMACION TRADICIONAL

# Función para ingresar las temperaturas diarias de la semana
def ingresar_temperaturas():
    """
    Esta función solicita al usuario que ingrese las temperaturas diarias para los 7 días de la semana
    y las almacena en una lista.
    """
    temperaturas = []  # Lista vacía para almacenar las temperaturas
    for i in range(7):
        # Solicitar la temperatura de cada día y agregarla a la lista
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


# Función para calcular el promedio semanal de las temperaturas
def calcular_promedio(temperaturas):
    """
    Esta función recibe una lista de temperaturas y devuelve el promedio semanal.
    """
    # Sumamos las temperaturas y dividimos entre el número de días (7) para obtener el promedio
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio


# Función principal que organiza el flujo del programa
def main():
    """
    Esta es la función principal que coordina el flujo del programa.
    Llama a las funciones para ingresar las temperaturas y calcular el promedio.
    """
    # Llamamos a la función para ingresar las temperaturas
    temperaturas = ingresar_temperaturas()

    # Llamamos a la función para calcular el promedio
    promedio = calcular_promedio(temperaturas)

    # Mostramos el resultado con dos decimales
    print(f"La temperatura promedio semanal es: {promedio:.2f} °C")


# Ejecutar el programa
if __name__ == "__main__":
    main()  # Llamamos a la función principal
