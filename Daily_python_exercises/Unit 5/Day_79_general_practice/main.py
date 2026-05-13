#lambda and map
prices = [10,20,30,40]
iva_added = list(map(lambda x: x*1.21, prices))
print(iva_added)


#filter
def long_name(name):
    if len(name)>4:
        return True
names = ["Ana", "Diego", "Luz", "Pablo", "German"]
long_names = list(filter(long_name, names))
print(long_names)


#list comprehensions
squares = [i**2 for i in range(1,11) if i%2==0]
print(squares)


#zip
players = ["Player1", "Player2", "Player3"]
points = [1550, 2800, 1200]
scores = dict(zip(players,points))
print(scores)


#decorators
def duplicator(funct):
    def wrap(*args):
        result = funct(*args)
        return result *2
    return wrap

@duplicator
def say_numb(numb):
    return numb

print(say_numb(8))