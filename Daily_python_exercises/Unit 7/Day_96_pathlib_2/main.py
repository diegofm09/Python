from pathlib import Path

main_path = Path("folder1")
file1 = main_path / "file1"

print(file1.parent)
print(file1.parent.parent)

print(file1.parent.parent.resolve())

p = Path("..").resolve()
print(p)

folder = Path(__file__).resolve().parent
new_file = str(folder) + "/new_file.txt"

with open(new_file, "w") as n:
    n.write("I have created a file on your computer")