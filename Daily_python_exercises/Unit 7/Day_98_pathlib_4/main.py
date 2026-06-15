from pathlib import Path

main_path = Path(__file__).resolve().parent
file1 = main_path / "file1.txt"

with file1.open() as text:
    print(text.read())



new_path = main_path / "new_direct"
if new_path.exists():
    pass
else:
    new_path = new_path.mkdir()

file = new_path / "new_file.txt"
with file.open("w") as file:
    file.write("Hi, i am a new file")


