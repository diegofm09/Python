import data_vault as dv
import security_logic as sl

if __name__ == "__main__":
    raw_username = input("Welcome, whats your username:\n")
    sanitized_username = raw_username.capitalize()
    security_token = int(input("Whats your security token:\n"))

    if sanitized_username == "Lead_analyst" or (security_token >= 1000 and security_token <= 9999):
        print(f"Welcome {raw_username}")
    else:
        print("You can not enter")
        exit()

    security_mode = "Encrypted" if dv.network_load > 50 else "Plain Text"
    print(f" Network load:{dv.network_load}\n Security mode: {security_mode}")
