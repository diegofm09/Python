with open("Daily_python_exercises/Unit 7/Day_92_advanced_context_managers/raw_series.txt", "r") as file1, open("Daily_python_exercises/Unit 7/Day_92_advanced_context_managers/sorted_series.txt", "w") as file2:
    series = file1.read().split("\n")
    series.sort()
    file2.write("\n".join(series))

with open("Daily_python_exercises/Unit 7/Day_92_advanced_context_managers/numbers.txt", "r") as numbers1, open("Daily_python_exercises/Unit 7/Day_92_advanced_context_managers/odd_numbers.txt", "w") as numbers2:
    numbers = numbers1.read().split("\n")
    numbers = map(lambda x: int(x), numbers)
    numbers = list(filter(lambda x: x%2 != 0, numbers))
    numbers = map(lambda x: str(x), numbers)
    numbers2.write("\n".join(numbers))

    