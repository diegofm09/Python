import data_vault as dv
import security_logic as sl

if __name__ == "__main__":
    raw_username = input("Welcome, whats your username:\n")
    sanitized_username = raw_username.capitalize()
    security_token = int(input("Whats your security token:\n"))

    if sanitized_username == "Lead_analyst" or (security_token >= 1000 and security_token <= 9999):
        print(f"Welcome {raw_username}")
        sl.save_log("Entered the system")
    else:
        print("You can not enter")
        sl.save_log("Access denyed")
        exit()
        
    while True:
        print("Use /help to show all comands")
        comand = input("")
        match comand:
            case "/help":
                print("Commands:\n  /secmode\n  /newthreats\n  /lastlogs\n  /addpatch\n  /exit\n  /help\n  /scan")

            case "/secmode":
                security_mode = "Encrypted" if dv.network_load > 50 else "Plain Text"
                print(f" Network load:{dv.network_load}\n Security mode: {security_mode}")
                sl.save_log("Showed security mode")

            case "/scan":
                pass

            case "/newthreats":
                raw_new_threats = input("What new threats do you want to register (Separated by commas):\n")
                new_threats = set(raw_new_threats.split(","))
                dv.sec_threats_cve |= dv.sec_threats_cve.fromkeys(new_threats, 5)
                sl.save_log("Added new threats")

            case "/lastlogs":
                print("Last logs:")
                for position, i in enumerate(dv.logs[-2::], start = 1):
                    print(f"{position}: {i}")

            case "/addpatch":
                dv.sec_threats_cve = {nombre: round(nota*1.15, 2) for (nombre,nota) in dv.sec_threats_cve.items()}
                print(dv.sec_threats_cve)

            case "/exit":
                max_threat = 0
                max_threat_name = ""
                for (name,level) in dv.sec_threats_cve.items():
                    max_threat_name = name if level > max_threat else max_threat_name
                    max_threat = level if level > max_threat else max_threat
                print(f"Bye {raw_username}\nThe most dangerous threat was {max_threat_name}")
                exit()

            case _:
                print("Command not found, use /help to show all comands")



