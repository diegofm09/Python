from pathlib import Path
#mode x

try:
    with open("Daily_python_exercises/Unit 7/Day_106_advanced_file_opening_modes/file.txt", "x") as file:
        file.write("new text written")
except:
        print("This file already exists")


#mode b, rb and wb
main_path = Path(__file__).resolve().parent
image = main_path/"image.jpg"
image_copy = main_path/"image_copy.jpg"
if not image_copy.exists():
    with open(image, "rb") as file1, open(image_copy, "wb") as file2:
        size = 4096
        while True:
            block = file1.read(size)
            if not image:
                break
            file2.write(block)


secret_info = "Password = 90923"
encoded_info = secret_info.encode("utf-8")

with open(main_path/"secret_info.bin", "wb") as file:
    file.write(encoded_info)

with open(main_path/"secret_info.bin", "rb") as file:
    print(file.read().decode())