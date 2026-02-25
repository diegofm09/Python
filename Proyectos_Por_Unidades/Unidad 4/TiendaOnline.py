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
precio = 0
while seleccion != "5":
    seleccion = input("Aqui tienes un menu con las opciones disponibles\n 1: Ver catalogo\n 2: Comprar producto\n 3: Ver mi carrito\n 4: Pagar y salir\n 5: Salir sin pagar\nElige que opcion deseas\n")
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
            print ("Falta esta")
        case "5":
            print("Saliste del programa")
            break
        case _:
            print("Esta opcion no esta dentro del menu, seleccione otra")


            
    