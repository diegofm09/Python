from pathlib import Path
main_path = Path().home()/"Python"

for p in main_path.glob("*s"):
    print(p)

for p in main_path.rglob("*Day*"):
    print(p)