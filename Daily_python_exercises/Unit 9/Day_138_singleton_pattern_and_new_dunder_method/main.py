class ControlTower:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, not_changeable):
        if not hasattr(self, "not_changeable"):
            self.not_changeable = not_changeable

tower1 = ControlTower("Aron")
tower3 = ControlTower("Pikachu")

print(tower1 is tower3)
print(tower1.not_changeable)
print(tower3.not_changeable)