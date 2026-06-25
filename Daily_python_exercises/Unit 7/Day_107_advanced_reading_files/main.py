with open("Daily_python_exercises/Unit 7/Day_107_advanced_reading_files/book.txt", "r") as file:
    while True:
        line = file.readline()
        if line:
            print(line.strip())
        else:
            print("-The end of the file-")
            break

with open("Daily_python_exercises/Unit 7/Day_107_advanced_reading_files/book.txt", "r") as file:
    lines = file.readlines()

print(f"This song has {len(lines)} lines and it ends with '{lines[-1]}'\n\n---------------")


with open("Daily_python_exercises/Unit 7/Day_107_advanced_reading_files/book.txt", "r") as file:
    file.readline()
    file.readline()
    file.readline(5)
    bookmark = file.tell()
    print(f"You have read till the {bookmark} character")

with open("Daily_python_exercises/Unit 7/Day_107_advanced_reading_files/book.txt", "r") as file:
    song = file.read()

replaced = song.replace("I", "You")
print(replaced)