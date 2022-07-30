import random
from random import choice

coin = random.choice(["tails","head"])
print(coin)
number = random.randint(1,10)
print(number)



cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)


    import statistics

    print(statistics.mean([100,94]))


