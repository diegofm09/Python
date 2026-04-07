master_name = "Diego"
student_name = input("Whats your student name:\n").capitalize()
student_age = int(input("How old are you:\n"))
acces_granted = True if student_name==master_name or student_age>=18 else False
if not acces_granted:
    print("You dont meet the conditions for entry, sorry")
    exit()
print(f"Welcome {student_name.upper()}: {student_age} years old")