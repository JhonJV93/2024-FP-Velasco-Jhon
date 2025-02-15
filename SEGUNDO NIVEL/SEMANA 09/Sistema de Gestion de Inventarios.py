# Clase Producto
class Producto:
    def __init__(self, producto_id, nombre, cantidad, precio):
        self.producto_id = producto_id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio


# Clase Inventario
class Inventario:
    def __init__(self):
        self.productos = []

    # Añadir producto
    def añadir_producto(self, producto):
        self.productos.append(producto)
        print(f"Producto {producto.nombre} añadido.")

    # Eliminar producto
    def eliminar_producto(self, producto_id):
        for producto in self.productos:
            if producto.producto_id == producto_id:
                self.productos.remove(producto)
                print(f"Producto {producto.nombre} eliminado.")
                return
        print("Producto no encontrado.")

    # Actualizar cantidad o precio
    def actualizar_producto(self, producto_id, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.producto_id == producto_id:
                if cantidad is not None:
                    producto.cantidad = cantidad
                if precio is not None:
                    producto.precio = precio
                print(f"Producto {producto.nombre} actualizado.")
                return
        print("Producto no encontrado.")

    # Buscar productos
    def buscar_producto(self, nombre):
        encontrados = [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]
        if encontrados:
            for producto in encontrados:
                print(f"{producto.nombre} - Cantidad: {producto.cantidad}, Precio: ${producto.precio}")
        else:
            print("No se encontraron productos.")

    # Mostrar todos los productos
    def mostrar_productos(self):
        if self.productos:
            for producto in self.productos:
                print(f"{producto.nombre} - Cantidad: {producto.cantidad}, Precio: ${producto.precio}")
        else:
            print("El inventario está vacío.")


# Función principal
def main():
    inventario = Inventario()

    while True:
        print("\n--- Menú de Inventario ---")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto")
        print("5. Mostrar Todos los Productos")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == "1":
            try:
                producto_id = int(input("Ingrese el ID del producto: "))
                nombre = input("Ingrese el nombre del producto: ")
                cantidad = int(input("Ingrese la cantidad del producto: "))
                precio = float(input("Ingrese el precio del producto: "))
                producto = Producto(producto_id, nombre, cantidad, precio)
                inventario.añadir_producto(producto)
            except ValueError:
                print("Por favor, ingrese valores válidos.")

        elif opcion == "2":
            try:
                producto_id = int(input("Ingrese el ID del producto a eliminar: "))
                inventario.eliminar_producto(producto_id)
            except ValueError:
                print("Por favor, ingrese un ID válido.")

        elif opcion == "3":
            try:
                producto_id = int(input("Ingrese el ID del producto a actualizar: "))
                cantidad = input("Ingrese la nueva cantidad (deje en blanco para no cambiar): ")
                precio = input("Ingrese el nuevo precio (deje en blanco para no cambiar): ")

                if cantidad:
                    cantidad = int(cantidad)
                if precio:
                    precio = float(precio)

                inventario.actualizar_producto(producto_id, cantidad if cantidad else None, precio if precio else None)
            except ValueError:
                print("Por favor, ingrese valores válidos para cantidad y precio.")

        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a buscar: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


# Ejecutar el programa
if __name__ == "__main__":
    main()
