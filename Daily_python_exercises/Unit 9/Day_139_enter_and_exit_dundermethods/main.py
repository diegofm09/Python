
class File:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.file = open(self.path, "w")
        print("File Opened")
        return self.file
        

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print("File closed")

        if exc_type is not None:
            print(f"⚠️ ¡Error detected!")
            print(f"  - Error Type (exc_type): {exc_type.__name__}")
            print(f"  - Message (exc_val): {exc_val}")
            print(f"  - Traceback (exc_tb): {exc_tb}")
            return True
        


a = File("Daily_python_exercises/Unit 9/Day_139_enter_and_exit_dundermethods/text.txt")

with a as file1:
    file1.write("hi")
    print("hi")
    