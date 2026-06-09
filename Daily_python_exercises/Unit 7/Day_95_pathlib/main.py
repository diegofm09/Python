from pathlib import Path

path1 = Path("directory_1")
file1 = Path("file_1.txt")

print(file1.name)
print(path1.name)

print(file1.suffix)
print(path1.suffix)

print(file1.stem)
print(path1.stem)

new_file = path1 / "new_file.txt"

print(new_file)
print(new_file.name)
print(new_file.suffix)
print(new_file.stem)

print(file1.exists())
print(path1.exists())
print(new_file.exists())