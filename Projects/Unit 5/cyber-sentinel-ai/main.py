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
                sl.save_log("Used /help")

            case "/secmode":
                security_mode = "Encrypted" if dv.network_load > 50 else "Plain Text"
                print(f" Network load:{dv.network_load}\n Security mode: {security_mode}")
                sl.save_log("Used /secmode")

            case "/scan":
                dangerous_threats = sl.risky_virus(dv.sec_threats_cve)
                while True:
                    energy_source = input("Is your energy source a battery or a potato:\n")
                    if energy_source.capitalize() == "Battery":
                        energy_source = sl.energy_gen(7)
                        break
                    elif energy_source.capitalize() == "Potato":
                        energy_source = sl.energy_gen(4)
                        break
                    else:
                        print("Thats not an option, Potato or Battery")
                for (pulse, virus_name) in zip(energy_source, dangerous_threats):
                    print(f"[{pulse}] Deleting: {virus_name}")
                    dv.sec_threats_cve = [i for i in dv.sec_threats_cve if i["name"] != virus_name]
                    print("Scan finished")
                sl.save_log("Used /scan")

            case "/newthreats":
                raw_new_threats = input("What new threats do you want to register (Separated by commas):\n")
                new_threats = set(raw_new_threats.split(","))
                for i in new_threats:
                    level = 0
                    while level <= 0 or level > 10:
                        level = float(input(f"What level of danger does {i} have\n"))
                        print("Error, level must be >0 and <10" if level <= 0 or level > 10 else "")
                    new_dict = {"name": i, "level": level }
                    dv.sec_threats_cve.append(new_dict)
                sl.save_log("Used /newthreats")

            case "/lastlogs":
                print("Last logs:")
                for position, i in enumerate(dv.logs[-2::], start = 1):
                    print(f"{position}: {i}")
                sl.save_log("Used /lastlogs")

            case "/addpatch":
                dv.sec_threats_cve = list(map(lambda x: {"name": x["name"], "level": (round((x["level"]*1.15)), 2)}, dv.sec_threats_cve))
                print("15% patch added")
                sl.save_log("Used /addpatch")

            case "/exit":
                print(f"Bye {raw_username}\nThe most dangerous threat was {max(dv.sec_threats_cve, key = lambda x: x['level'])['name']}")
                sl.save_log("Used /exit")
                exit()

            case _:
                print("Command not found, use /help to show all comands")
                sl.save_log("Error, command not found")



