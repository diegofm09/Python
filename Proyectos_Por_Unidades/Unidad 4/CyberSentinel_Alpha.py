print("Bienvenido al Cyber Sentinel")
nombre_agente = input("Introduzca tu nombre de agente\n").capitalize()
nivel_seguridad = int(input("Introduzca tu nivel de seguridad\n"))
if nombre_agente=="Admin" or nivel_seguridad>5:
    print(f"Bienvenido {nombre_agente}, nivel seguridad {nivel_seguridad}")
else:
    print("Lo siento, no tienes el permiso para entrar")
    exit()

nivel_amenaza= {"Malware": 9, "Phishing": 6, "SQLi": 8, "DDoS": 4, }
ataques_criticos = [ataque for ataque in nivel_amenaza if nivel_amenaza[ataque]> 7]
simulacro_crisis = {ataque: nivel+1 for (ataque, nivel) in nivel_amenaza.items()}

ips_sospechosas = list(set(["192.168.1.10", "10.0.0.5", "192.168.1.10", "172.16.0.1", "10.0.0.5", "192.168.1.25", "10.0.0.100", "192.168.1.10", "185.45.12.3", "172.16.0.1"]))

protocolos_de_red = ("TCP", "UDP", "HTTPS")

historial_incidentes = [
    "2024-05-01 10:00 - Alerta: Intento de login fallido desde IP 192.168.1.10",
    "2024-05-01 10:05 - Sistema: Escaneo de puertos detectado en Firewall",
    "2024-05-01 10:15 - Crítico: Archivo infectado detectado en /home/admin/descargas",
    "2024-05-01 10:20 - Info: Actualización de base de datos de virus completada",
    "2024-05-01 10:30 - Alerta: Tráfico inusual detectado desde IP 185.45.12.3",
    "2024-05-01 10:45 - Sistema: Nueva IP sospechosa añadida a la lista de bloqueo",
    "2024-05-01 11:00 - Crítico: Intento de inyección SQL bloqueado en el formulario de login"
]
print(f"Ultimos incidentes registrados\n {historial_incidentes[-3:]}")

while True:
    print("Menu:\n 1) Listar amenazas\n 2) Analizar nivel riesgo medio\n 3) Filtrar ataques criticos\n 4) Mostrar IPs unicas\n 5) Simulacro de crisis\n 6) Consultar estado del sistema\n 7) Salir")
    opcion_menu = input("Selecciona la opcion del menu que quieras\n")
    match opcion_menu:
        case "1":
            print("--------------------")
            for (posicion, (amenaza, riesgo)) in enumerate(nivel_amenaza.items(), start=1):
                print(f"{posicion}) {amenaza}, Riesgo {riesgo}")
            print("--------------------")
            
        case "2":
            print("--------------------")
            riesgo_medio = (sum(nivel_amenaza.values()))/len(nivel_amenaza)
            print(f"El nivel de riesgo medio actual es de {round(riesgo_medio, 2)}")
            print("--------------------")

        case "3":
            print("--------------------")
            print(f"Ataques criticos:")
            for (posicion, ataque) in enumerate(ataques_criticos, start = 1):
                print(f"{posicion}) {ataque}")
            print("--------------------")
        
        case "4":
            print("--------------------")
            print("IPs unicas:")
            for (posicion,ip) in enumerate(ips_sospechosas, start=1):
                print(f"{posicion}) {ip}")
            print("--------------------")
        
        case "5":
            print("--------------------")
            print("Nivel amenaza en caso de crisis:")
            for (posicion, (crisis, nivel_riesgo)) in enumerate(simulacro_crisis.items(), start=1):
                print(f"{posicion}) {crisis}, nivel amenaza {nivel_riesgo}")
            print(f"Riesgo medio en caso de crisis:\n{round((sum(simulacro_crisis.values()))/len(simulacro_crisis), 2)}")
            print("--------------------")

        case "6":
            print("--------------------")
            print(f"Hay un total de {len(nivel_amenaza)} amenazas")
            print(f"La amenaza mas alta es {max(nivel_amenaza, key=nivel_amenaza.get)}")
            suma_valores_riesgo = sum(nivel_amenaza.values())
            print(f"La suma de todos los valores de riesgo es de {suma_valores_riesgo}")
            print("Todo esta bajo control" if suma_valores_riesgo<20 else "Alerta, riesgo demasiado alto")
            print("--------------------")
        
        case "7":
            print("--------------------")
            print("Saliste con exito del programa")
            print("--------------------")
            break

        case _:
            print("--------------------")
            print("Opcion no disponible")
            print("--------------------")
