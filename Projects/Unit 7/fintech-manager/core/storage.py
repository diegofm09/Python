from pathlib import Path

main_p = Path(__file__).resolve().parent.parent

data_path = main_p/"data"

if not data_path.is_dir():
    data_path.mkdir()
