import random

network_load = random.randint(0,100)

sec_threats_cve = [{"name":"SQLi", "level": 9.7},{"name": "XSS", "level": 8.3}, {"name": "Info disclosure", "level": 5.3}, {"name": "Banner Grabbing", "level": 3.2}]

security_policies = (
    "PROTOCOL_01: Do not export sensitive biometric data.",
    "PROTOCOL_02: AI core must remain isolated from public web.",
    "PROTOCOL_03: Encryption is mandatory for all neural transfers.")

logs = []
