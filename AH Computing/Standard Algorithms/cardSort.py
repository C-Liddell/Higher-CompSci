from dataclasses import dataclass
import random

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

@dataclass
class Card:
    number: int
    suit: str

cards = [Card for i in range(10)]

for i in cards:
    i.number = random.randint(1,14)
    i.suit = random.choice(suits)


for i in range (1,len(cards)):
    currentSuit = cards[i].suit
    currentValue = ord(currentSuit[:1])
    position = i

    while position > 0 and ord(cards[position-1].suit[:1]) > currentValue:
        cards[position].suit = cards[position-1].suit
        position -= 1

    cards[position].suit = currentSuit


for i in cards:
    print(i.suit)