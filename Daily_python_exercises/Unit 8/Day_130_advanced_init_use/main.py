#Data types valuation

class BankAccount:
    def __init__(self, initial_money, name):
        if not isinstance(name, str) or not name.strip():
            raise ValueError ("The titular name must be a str")

        if initial_money<0:
            raise ValueError ("The initial money must be a number higher than 0")

        self.initial_money = initial_money
        self.name = name

#Add extra 
class Student:
    def __init__(self, name, notes = None):
        self.name = name
        self.notes = notes if notes != None else []

    def new_note(self, x):
        self.notes.append(x)

a = Student("Jhon", [8, 9, 2.3])
print(a.notes)

b = Student("Anna")
print(b.notes)
