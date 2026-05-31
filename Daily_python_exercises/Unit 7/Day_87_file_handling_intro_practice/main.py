file = open("Daily_python_exercises/Unit 7/Day_87_file_handling_intro_practice/countries_to_visit.txt")
text = file.read()
file.close()
print(f"Places to visit:\n{text}")
