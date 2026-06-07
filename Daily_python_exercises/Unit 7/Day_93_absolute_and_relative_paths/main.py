with open("/home/diegofermend/Python/Daily_python_exercises/Unit 7/Day_93_absolute_and_relative_paths/absolute_path.txt", "w") as absolute_path_file:
    absolute_path_file.write("This file was written using an absolute path")

with open("Daily_python_exercises/Unit 7/Day_93_absolute_and_relative_paths/relative_path.txt", "w") as relative_path:
    relative_path.write("This file was written using a relative path")

