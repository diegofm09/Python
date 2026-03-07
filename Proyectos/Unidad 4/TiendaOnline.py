productos = {
    "Raton": 16.2,
    "Monitor": 120.9,
    "Teclado": 34.5,
    "Cables": 6.1,
}
carrito = []
presupuesto = float(input("Bienvenido a la tienda online, cual es tu presupuesto:\n"))
numero_compras = 0
seleccion = "0"
while True:
    seleccion = input("Aqui tienes un menu con las opciones disponibles\n 1: Ver catalogo\n 2: Comprar producto\n 3: Ver mi carrito\n 4: Pagar y salir\n 5: Salir sin pagar\nElige que opcion deseas\n")
    precio = 0
    match seleccion:
        case "1":
            print(f"El catálogo es este:\n")
            for posicion_catalogo, producto_catalogo in enumerate(productos, start=1):
                print(f"{posicion_catalogo}) {producto_catalogo}")
        case "2":
            compra = (input("Que producto deseas comprar\n")).capitalize()
            if compra in productos:
                carrito.append(compra)
                numero_compras += 1
                print("Añadido con exito al carrito\n")
            else:
                print("Error, ese producto no esta disponible\n")
        case "3":
            print ("En tu carrito tienes los siguientes productos:")
            for posicion_carrito, producto_carrito in enumerate(carrito, start = 1):
                print(f"{posicion_carrito}) {producto_carrito}")
            print(f"Ultimas adquisiciones:\n{carrito[:-3:-1]}")
            for producto_carrito in carrito:
                precio += productos[producto_carrito]
            print(f"El precio del carrito es de {precio} euros")
        case "4":
            for comprados in carrito:
                precio += productos[comprados]
            if precio <= presupuesto:
                print (f"Pagaste con exito los {round(precio, 2)}, tu dinero restante es de {round(presupuesto-precio, 2)} euros")
                break
            else:
                carrito.clear()
                numero_compras = 0
                print(f"No tienes suficiente dinero, te faltan {precio-presupuesto} euros\nSe ha vaciado el carrito, por favor, empiece de nuevo la compra")
        case "5":
            print("Saliste del programa con exito")
            break
        case _:
            print("Esta opcion no esta dentro del menu, seleccione otra")
carrito_mas_caro = 0.0
carrito_mas_barato = 1000.0
for producto_carrito in carrito:
    if productos[producto_carrito] < carrito_mas_barato:
        carrito_mas_barato = productos[producto_carrito]
        nombre_objeto_mas_barato = producto_carrito
for producto_carrito in carrito:
    if productos[producto_carrito] > carrito_mas_caro:
        carrito_mas_caro = productos[producto_carrito]
        nombre_objeto_mas_caro = producto_carrito
print(f"Compraste un total de {numero_compras} cosas\nEl objeto mas caro fue {nombre_objeto_mas_caro}\nEl mas barato fue {nombre_objeto_mas_barato}")


            
    