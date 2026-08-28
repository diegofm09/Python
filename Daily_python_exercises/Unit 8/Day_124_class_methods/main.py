class Student:

    count = 0
    classroom = "2023-2024 2ºA"

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1

    def get_info(self):
        return f"{self.name}: {self.gpa}"

    @classmethod
    def get_students_number(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def change_classroom(cls, new_class):
        cls.classroom = new_class