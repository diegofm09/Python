productos = {
    "raton": 16.2,
    "monitor": 120.9,
    "teclado": 34.5,
    "cables": 6.1,
}
carrito = []
presupuesto = float(input("Bienvenido a la tienda online, cual es tu presupuesto:\n"))
numero_compras = 0
seleccion = 0
while seleccion != 5:
    seleccion = int(input("Aqui tienes un menu con las opciones disponibles:\n 1) Ver catalogo\n 2) Comprar producto\n 3) Ver mi carrito\n 4) Pagar y salir\n 5) Salir sin pagar\nElige que opcion deseas\n"))
    match seleccion:
        case 1:
            print(f"El catálogo es este:\n")
            for posicion, producto in enumerate(productos, start=1):
                print(f"{posicion}) {producto}")
        case 2:
            compra = input("Que producto deseas comprar\n")
            if compra in productos:
                carrito.append(compra)
                numero_compras += 1
                print("Añadido con exito al carrito")
            else:
                print("Error, ese producto no esta disponible")
        case 3:
            for posicion_carrito, objeto in enumerate(carrito):
                print(f"{posicion_carrito}) {objeto}")
            print(f"Ultimas adquisiciones:\n{carrito[0:-2]}")

            
    