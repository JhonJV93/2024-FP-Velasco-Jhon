import os
import subprocess
from time import sleep


def mostrar_codigo(ruta_script):
    """
    Muestra el código del script Python que se encuentra en la ruta especificada.
    """
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Intenta abrir y leer el archivo
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        # Si no se encuentra el archivo
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        # Manejo de errores genéricos
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script, en_segundo_plano=False):
    """
    Ejecuta el script Python en la ruta especificada.
    Si 'en_segundo_plano' es True, ejecuta el script en segundo plano.
    """
    try:
        if os.name == 'nt':  # En sistemas Windows
            comando = ['cmd', '/k', 'python', ruta_script]
        else:  # En sistemas basados en Unix (Linux/macOS)
            comando = ['xterm', '-hold', '-e', 'python3', ruta_script]

        if en_segundo_plano:
            # Ejecuta en segundo plano sin esperar a que termine
            subprocess.Popen(comando)
            print("El script se está ejecutando en segundo plano.")
        else:
            # Ejecuta en la ventana de comandos, esperando a que termine
            subprocess.Popen(comando)
    except Exception as e:
        # Manejo de errores al ejecutar el script
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    """
    Muestra el menú principal donde el usuario puede elegir una unidad.
    """
    ruta_base = os.path.dirname(__file__)

    # Diccionario de unidades (puedes personalizar estos valores)
    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        # Muestra las opciones del menú principal

