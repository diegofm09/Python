class Employee:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def get_info(self):
        return f"{self.name} = {self.job}"

    @staticmethod
    def is_valid_job(job):
        valid_jobs = ["Cook", "Waiter", "Manager", "Receptionist"]
        return job in valid_jobs 

print(Employee.is_valid_job("Waiter"))


employee1 = Employee("SpongeBob", "Cook")
print(employee1.is_valid_job(employee1.job))