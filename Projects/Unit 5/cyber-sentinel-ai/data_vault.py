import random

network_load = random.randint(0,100)

sec_threats_cve = {"SQLi": 9.7,"XSS": 8.3, "Info disclosure": 5.3, "Banner Grabbing": 3.2 }

security_policies = (
    "PROTOCOL_01: Do not export sensitive biometric data.",
    "PROTOCOL_02: AI core must remain isolated from public web.",
    "PROTOCOL_03: Encryption is mandatory for all neural transfers.")