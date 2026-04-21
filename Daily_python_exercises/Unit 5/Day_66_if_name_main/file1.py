def add(x,y):
    return x+y

if __name__ == "__main__":
    print("You are on the main file")
    if add(1,2)==3:
        print("Success")
    else:
        print("Fail")
else:
    print("You are not on the main file")

print(f"File 1 name: {__name__}")