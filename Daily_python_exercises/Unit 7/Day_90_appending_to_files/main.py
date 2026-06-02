file = open("Daily_python_exercises/Unit 7/Day_90_appending_to_files/animals.txt", "w")
file.write("tiger\nlion\npanda\nfox\n")
file.close()

file = open("Daily_python_exercises/Unit 7/Day_90_appending_to_files/animals.txt", "a")
file.write("bear\nspider")
file.close()
