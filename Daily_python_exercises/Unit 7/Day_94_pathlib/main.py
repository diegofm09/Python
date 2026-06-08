from pathlib import Path

print(Path.cwd())
for p in Path().iterdir():
    print(p)
