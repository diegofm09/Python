from pathlib import Path
import time
#ex 1

main_p = Path(__file__).resolve().parent

for file in main_p.rglob("*"):
    if file.suffix == ".txt":
        print (file.stem)
    elif file.suffix == ".py":
        print (file.resolve())
    else:
        pass


#ex 2

paths = Path(main_p/"ex2/subfolder2")

if Path(main_p/"ex_2").exists():
    paths.mkdir(parents=True)


#ex 3

new = main_p/"old_file.txt"
new.touch()
if new.exists():
    new.rename(main_p/"security_backup")
    time.sleep(5)
    new = Path(main_p/"security_backup")
    new.unlink()
else:
    print("Does not exist")

