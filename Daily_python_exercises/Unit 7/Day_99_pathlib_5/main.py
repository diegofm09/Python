from pathlib import Path
p = Path(__file__).resolve().parent

i = p/"new_direct/inner_direct"
if i.exists():
    pass
else:
    i.mkdir(parents=True)
y = p /"new_direct"/"new_file1.txt"
y.touch()

z = i / "new_file.txt" 
print(z)
z.touch()
z.rename(i/"new_file2.txt")
y.unlink()

