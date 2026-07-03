from pathlib import Path

main_path = Path(__file__).resolve().parent

with open(main_path/"file.txt","w") as file:
    file.write("El sol brilla\n")
    file.write("La luna duerme\n")
    file.write("Las estrellas observan\n")

with open("Daily_python_exercises/Unit 7/Day_108_advanced_reading_files_practice/file.txt", "r") as file:
    print(file.readline().strip())
    print(file.readline().strip())
    print(file.tell())

with open("Daily_python_exercises/Unit 7/Day_108_advanced_reading_files_practice/file.txt", "r") as file:
    lines = file.readlines()

line_3 = lines[2].upper()

print(line_3)
with open("Daily_python_exercises/Unit 7/Day_108_advanced_reading_files_practice/file.txt", "r") as file:
    song = file.read()

song = song.replace("luna", "selva")

print(song)