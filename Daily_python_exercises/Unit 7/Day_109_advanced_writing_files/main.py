from pathlib import Path
import time
import random

main_p = Path(__file__).resolve().parent

names = ["Ana\n", "Pedro\n", "Jonah\n", "Sandra\n", "Michael\n"]

with open(main_p/"file.txt", "w") as file1:
    file1.writelines(names)

with open(main_p/"times.txt", "w") as file2:
    for i in range(5):
        time.sleep(2)
        file2.write(f"Random number between 1-100: {random.randint(1,100)}\n")
        file2.flush()
    print(file2.closed)

print(file2.closed)

    



