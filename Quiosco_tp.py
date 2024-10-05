# Inventario inicial con identificador (ID) único para cada producto
inventario = [
    {"id": 1, "nombre": "Chupetin Sable de luz", "cantidad": 50, "precio": 200},
    {"id": 2, "nombre": "Agua La Fuerza", "cantidad": 35, "precio": 3200},
    {"id": 3, "nombre": "Gomitas Holocubo", "cantidad": 25, "precio": 990},
    {"id": 4, "nombre": "Barrita de Cereal Wookiee", "cantidad": 48, "precio": 2500},
    {"id": 5, "nombre": "Galletitas R2D2", "cantidad": 20, "precio": 15800}
]

# Menú principal
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar producto al inventario")
    print("2. Realizar una venta")
    print("3. Mostrar productos disponibles")
    print("4. Salir del sistema")

# Función para buscar producto por ID
def buscar_producto_por_id(id_producto):
    for producto in inventario:
        if producto["id"] == id_producto:
            return producto
    return None

# Agregar productos al inventario
def agregar_producto():
    print("\n--- Agregar Producto ---")
    print("Si el producto ya existe, ingrese el número de ID del producto.")
    print("Si es un producto nuevo, ingrese '0'.\n")

    # Mostrar productos con sus IDs
    for producto in inventario:
        print(f"ID: {producto['id']} - {producto['nombre']} (Cantidad: {producto['cantidad']}, Precio: ${producto['precio']})")

    id_producto = int(input("\nIngrese el ID del producto (o '0' para un nuevo producto): "))

    # Si el ID es 0, agregar un nuevo producto
    if id_producto == 0:
        nombre = input("Ingrese el nombre del producto: ")
        cantidad = int(input("Ingrese la cantidad disponible: "))
        precio = float(input("Ingrese el precio unitario: "))
        
        # Asignar un nuevo ID único
        nuevo_id = max([producto["id"] for producto in inventario]) + 1
        inventario.append({"id": nuevo_id, "nombre": nombre, "cantidad": cantidad, "precio": precio})
        print(f"Producto '{nombre}' agregado con éxito al inventario.")
    
    # Si el ID ya existe, agregar cantidad
    else:
        producto_existente = buscar_producto_por_id(id_producto)
        if producto_existente:
            cantidad_adicional = int(input(f"Ingrese la cantidad adicional para '{producto_existente['nombre']}': "))
            producto_existente["cantidad"] += cantidad_adicional
            print(f"Se han agregado {cantidad_adicional} unidades a '{producto_existente['nombre']}'. Ahora hay {producto_existente['cantidad']} unidades en total.")
        else:
            print("El ID ingresado no es válido. Intente nuevamente.")

# Función para realizar una venta
def realizar_venta():
    print("\n--- Productos Disponibles ---")
    for idx, producto in enumerate(inventario, 1):
        print(f"{idx}. {producto['nombre']} - Precio: ${producto['precio']} - Cantidad: {producto['cantidad']}")
    
    indice_producto = int(input("\nSeleccione el número del producto que desea comprar: ")) - 1
    if indice_producto < 0 or indice_producto >= len(inventario):
        print("Producto no válido. Intente nuevamente.")
        return
    
    cantidad_comprar = int(input(f"Ingrese la cantidad que desea comprar de {inventario[indice_producto]['nombre']}: "))
    if cantidad_comprar > inventario[indice_producto]["cantidad"]:
        print("No hay suficiente stock para completar la venta.")
    else:
        inventario[indice_producto]["cantidad"] -= cantidad_comprar
        total_pagar = cantidad_comprar * inventario[indice_producto]["precio"]
        print(f"Venta realizada con éxito. Total a pagar: ${total_pagar:.2f}")

# Función para mostrar productos disponibles
def mostrar_productos():
    print("\n--- Productos en Inventario ---")
    for producto in inventario:
        print(f"ID: {producto['id']} - Producto: {producto['nombre']} - Cantidad: {producto['cantidad']} - Precio: ${producto['precio']}")

# Función principal para ejecutar el menú
def sistema_quiosco():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_producto()
        else:
            if opcion == "2":
                realizar_venta()
            else:
                if opcion == "3":
                    mostrar_productos()
                else:
                    if opcion == "4":
                        print("Saliendo del sistema. ¡Hasta luego!")
                        break
                    else:
                        print("Opción no válida. Intente nuevamente.")

# Ejecutar el sistema
sistema_quiosco()
