import json


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def to_dict(self):
        return {"ID": self.id_producto, "Nombre": self.nombre, "Cantidad": self.cantidad, "Precio": self.precio}

    @staticmethod
    def from_dict(data):
        return Producto(data["ID"], data["Nombre"], data["Cantidad"], data["Precio"])

class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("El producto ya existe en el inventario.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto agregado exitosamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        if id_producto in self.productos:
            if nueva_cantidad is not None:
                self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
            if nuevo_precio is not None:
                self.productos[id_producto].actualizar_precio(nuevo_precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, nombre):
        encontrados = [p.to_dict() for p in self.productos.values() if nombre.lower() in p.nombre.lower()]
        return encontrados if encontrados else "No se encontraron productos."

    def mostrar_productos(self):
        if self.productos:
            return [p.to_dict() for p in self.productos.values()]
        else:
            return "Inventario vacío."

    def guardar_en_archivo(self, archivo):
        with open(archivo, "w") as f:
            json.dump([p.to_dict() for p in self.productos.values()], f, indent=4)
        print("Inventario guardado correctamente.")

    def cargar_desde_archivo(self, archivo):
        try:
            with open(archivo, "r") as f:
                datos = json.load(f)
                self.productos = {p["ID"]: Producto.from_dict(p) for p in datos}
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Archivo no encontrado. Iniciando inventario vacío.")


# Menú interactivo
def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo("inventario.json")

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ")
            precio = input("Nuevo precio (dejar vacío para no cambiar): ")
            # Manejo de la entrada para evitar errores si no se ingresa un valor
            if cantidad:
                cantidad = int(cantidad)
            else:
                cantidad = None

            if precio:
                precio = float(precio)
            else:
                precio = None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            if isinstance(resultados, list):
                for producto in resultados:
                    print(producto)
            else:
                print(resultados)

        elif opcion == "5":
            productos = inventario.mostrar_productos()
            if isinstance(productos, list):
                for producto in productos:
                    print(producto)
            else:
                print(productos)

        elif opcion == "6":
            inventario.guardar_en_archivo("inventario.json")
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
