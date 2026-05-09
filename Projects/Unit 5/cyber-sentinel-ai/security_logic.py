import data_vault as dv
import datetime

def save_log(action):
    log_time = datetime.datetime.now()
    log_time = datetime.datetime.strftime(log_time, "%H:%M:%S %d/%m/%Y")
    logs_list = [f"{log_time}: {action}"]
    dv.logs.append(logs_list)
