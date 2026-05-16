while True:
    try:
        num1 = float(input("Write a number\n"))
        num2 = float(input("Write anothet number\n"))
        div = num1/num2
        print(div)
        break
    except ValueError:
        print("Error, you have to enter a number")
    except ZeroDivisionError:
        print("Cannot divide by 0")
        