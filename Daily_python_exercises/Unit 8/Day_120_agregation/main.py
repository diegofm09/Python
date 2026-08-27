class Bussines:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def new_employee(self, employee):
        self.employees.append(employee)

    def employees_name(self):
        return [employee.name for employee in self.employees]

class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name
        self.salary = salary


bussines = Bussines("Amazon")

employee1 = Employee("Pablo", 150000)
employee2 = Employee("Marta", 130000)

bussines.new_employee(employee1)
bussines.new_employee(employee2)

print(bussines.employees_name())
