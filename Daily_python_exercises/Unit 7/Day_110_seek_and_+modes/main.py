from pathlib import Path
import time
import random

main_p = Path(__file__).resolve().parent

with open(main_p/"book.txt", "r") as file1:
    for i in range(6):
        if file1.tell() == 98:
            file1.seek(0)
        else:
            print(file1.readline())
            time.sleep(1)

with open("Daily_python_exercises/Unit 7/Day_110_seek_and_+modes/points.txt", "r+") as file2:
    print(file2.readline())
    time.sleep(0.5)
    print("Lets give you random points between 0 and 100")
    file2.seek(13)
    points = str(random.randint(0,100))
    file2.write(points)
    file2.seek(0)
    print(file2.readline())