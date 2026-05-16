def divide(x,y):
    return x / y
errors = 0

while True:
    try:
        num1 = int(input("Write a number\n"))
        break
    except ValueError:
        print("Please, enter a non decimal number")
        errors += 1
    finally:
        print("We are going to divide number 1 by number 2")
    
while True:
    try:
        num2 = int(input("Write a number\n"))
        break
    except ValueError:
        print("Please, enter a non decimal number")
        errors += 1
    finally:
        print("We are going to divide number 1 by number 2")

try:
    divide(num1,num2)
except ZeroDivisionError:
    print("The division, went wrong, de denominator was 0")
    errors += 1
finally:
    print("We have divided number 1 by number 2")

print(f"During the process, {errors} errors were made")
