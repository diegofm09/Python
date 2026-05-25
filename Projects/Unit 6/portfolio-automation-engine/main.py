import engine
import utils
import time

while True:
    match selection:=input("Menu:\n 1)Run simulation\n 2)View Global analytics\n 3)Exit\n"):
        case "1":
            def simulate():
                pass
        case "2":
            pass
        case "3":
            print("Exiting...")
            time.sleep(3)
            print("Program closed")
            exit()
        case _:
            print("Option not available")