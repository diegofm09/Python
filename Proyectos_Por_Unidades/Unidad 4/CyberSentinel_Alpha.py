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
