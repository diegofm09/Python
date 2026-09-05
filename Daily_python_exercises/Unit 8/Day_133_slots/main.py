from dataclasses import dataclass


class Process:

    __slots__ = ("pid", "name", "priority")

    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority


o = Process(12, "Hi", 1)


try:
    print(o.__dict__)
except Exception:
    print("The class Process has no dict atribute")