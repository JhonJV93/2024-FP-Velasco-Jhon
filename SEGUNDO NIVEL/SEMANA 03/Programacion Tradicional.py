# PROGRAMACION TRADICIONAL

def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del día {i + 1}: "))
        temperaturas.append(temp)
    return temperaturas


# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    promedio = sum(temperaturas) / len(temperaturas)
    return promedio


# Función principal
def main():
    # Ingresar las temperaturas de los 7 días
    temperaturas = ingresar_temperaturas()

    # Calcular el promedio
    promedio = calcular_promedio(temperaturas)

    # Mostrar el resultado
    print(f"La temperatura promedio semanal es: {promedio:.2f} °C")


# Ejecutar el programa
if __name__ == "__main__":
    main()
