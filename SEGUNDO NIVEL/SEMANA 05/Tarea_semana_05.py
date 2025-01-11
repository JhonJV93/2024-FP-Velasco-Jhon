# Programa de conversión de unidades de longitud
# Funcionalidad: Este programa permite convertir entre diferentes unidades de longitud: metros, kilómetros, millas y centímetros.

def convertir_metros_a_kilometros(metros):
    """
    Convierte una cantidad en metros a kilómetros.
    """
    return metros / 1000


def convertir_metros_a_millas(metros):
    """
    Convierte una cantidad en metros a millas.
    """
    return metros / 1609.34


def convertir_metros_a_centimetros(metros):
    """
    Convierte una cantidad en metros a centímetros.
    """
    return metros * 100


def convertir_unidades(valor, unidad_origen, unidad_destino):
    """
    Convierte un valor de una unidad de medida a otra.
    """
    if unidad_origen == "metros":
        if unidad_destino == "kilometros":
            return convertir_metros_a_kilometros(valor)
        elif unidad_destino == "millas":
            return convertir_metros_a_millas(valor)
        elif unidad_destino == "centimetros":
            return convertir_metros_a_centimetros(valor)
        else:
            return None  # Unidad de destino no válida
    else:
        return None  # Solo se implementan conversiones desde metros por ahora


def mostrar_menu():
    """
    Muestra el menú de opciones para el usuario y recibe su elección.
    """
    print("Conversor de Unidades de Longitud")
    print("1. Convertir metros a kilómetros")
    print("2. Convertir metros a millas")
    print("3. Convertir metros a centímetros")
    print("4. Salir")


def ejecutar_programa():
    """
    Ejecuta el programa interactivo para convertir unidades de longitud.
    """
    continuar = True

    while continuar:
        mostrar_menu()

        # Obtener la opción del usuario
        opcion = input("Selecciona una opción (1-4): ")

        # Verificar si la opción es válida
        if opcion == "1" or opcion == "2" or opcion == "3":
            valor = float(input("Introduce el valor en metros: "))  # Valor en metros (float)

            if opcion == "1":
                resultado = convertir_metros_a_kilometros(valor)
                print(f"{valor} metros equivalen a {resultado} kilómetros.")
            elif opcion == "2":
                resultado = convertir_metros_a_millas(valor)
                print(f"{valor} metros equivalen a {resultado} millas.")
            elif opcion == "3":
                resultado = convertir_metros_a_centimetros(valor)
                print(f"{valor} metros equivalen a {resultado} centímetros.")

        elif opcion == "4":
            print("Saliendo del programa.")
            continuar = False  # Cambiar la condición para salir del bucle

        else:
            print("Opción no válida. Por favor, selecciona una opción válida (1-4).")


# Llamar a la función principal para ejecutar el programa
ejecutar_programa()
