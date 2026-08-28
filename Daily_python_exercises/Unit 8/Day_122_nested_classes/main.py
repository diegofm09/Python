class Bussiness:  
    def __init__(self, name):
        self.name = name
        self.employees = []

    def create_employee(self, name, job):
        new_employee = self.Employee(name, job)
        self.employees.append(new_employee)

    def all_employees(self):
        for i in self.employees:
            i.details()

    class Employee:
        def __init__(self, name, job):
            self.name = name
            self.job = job

        def details(self):
            print(f"{self.name} {self.job}")

bussiness = Bussiness("Nvidia")

bussiness.create_employee("Jhon", "Admin")
bussiness.create_employee("Mia", "Manager")

bussiness.all_employees()