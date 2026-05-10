import data_vault as dv
import datetime

def show_time(function):
    def wrapper(*args):
        raw_time = datetime.datetime.now()
        print(datetime.datetime.strftime(raw_time, "%H:%M:%S"))
        function(*args)
    return wrapper

def save_log(action):
    log_time = datetime.datetime.now()
    log_time = datetime.datetime.strftime(log_time, "%H:%M:%S %d/%m/%Y")
    logs_list = [f"{log_time}: {action}"]
    dv.logs.append(logs_list)

@show_time
def energy_gen(max):
    for i in range(1,max + 1):
        yield f"Pulse {i}"

@show_time
def risky_virus(threats):
    risky_threats = []
    for (name, level) in threats.items():
        if level > 7:
            risky_threats.append(name)
    return risky_threats
