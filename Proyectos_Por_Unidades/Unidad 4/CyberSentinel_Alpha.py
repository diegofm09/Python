print("Bienvenido al Cyber Sentinel")
nombre_agente = input("Introduzca tu nombre de agente\n").capitalize()
nivel_seguridad = int(input("Introduzca tu nivel de seguridad\n"))
if nombre_agente=="Admin" or nivel_seguridad>5:
    print(f"Bienvenido {nombre_agente}, nivel seguridad {nivel_seguridad}")
else:
    print("Lo siento, no tienes el permiso para entrar")
    exit()

nivel_amenaza= {"Malware": 9, "Phishing": 6, "SQLi": 8, "DDoS": 4, }
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

print("Menu:\n 1) Listar amenazas\n 2) Analizar nivel riesgo medio\n 3) Filtrar ataques criticos\n 4) Salir")
opcion_menu = input("Selecciona la opcion del menu que quieras\n")
match opcion_menu:
    case "1":
        for (posicion, amenaza) in enumerate(nivel_amenaza.keys(), start=1):
            print(f"{posicion}) {amenaza}")
