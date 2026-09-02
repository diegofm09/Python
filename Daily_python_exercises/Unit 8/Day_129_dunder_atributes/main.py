class X:
    class Y:
        class Z:
            """Hi this is a class"""
            def __init__(self, name, age):
                self.name = name
                self.age = age

a = X.Y.Z("Diego", 17)

print(a.__dict__)

print(X.Y.Z.__qualname__)

print(X.Y.Z.__name__)

print(X.Y.Z.__doc__)

print(a.__class__)

print(a.__module__)

print(__file__)