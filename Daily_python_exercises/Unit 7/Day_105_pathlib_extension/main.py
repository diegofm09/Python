from pathlib import Path

main_path = Path(__file__).resolve().parent

new_folder = main_path / "folder"

if not new_folder.exists():
    new_folder.mkdir()

new_file = new_folder / "file.txt"

new_file.touch()
relative_path = Path("fodlre") /"new_file"

print("Great, this path is a file" if new_file.is_file() else "This path is not a file")
print("Great, this path is a file" if Path(main_path/"text.txt").is_file() else "This path is not a file")

print("This folder does exits" if new_folder.is_dir() else "This folder does not exist")
print("This folder does exits" if Path(main_path/"folder1").is_dir() else "This folder does not exist")

print("This path is absolute" if new_file.is_absolute() else "This path is relative")
print("This path is absolute" if relative_path.is_absolute() else "This path is relative")

new_file.write_text("Hi, I have been writen with pathlib method write_text")
print(new_file.read_text())
