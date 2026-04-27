import random

poker = ["diamonds", "hearts", "clubs", "spades"]
print(random.choice(poker))

spin =  ["red", "black", "green"]
print(random.choices(spin, weights=[18,18,2], k=40))

positions = ["marco", "ana", "will", "pedro"]
random.shuffle(positions)
print(positions)

deck = list(range(1,53))
print(random.sample(deck, k=5))