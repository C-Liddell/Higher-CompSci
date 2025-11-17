import random
from dataclasses import dataclass


suits = ["Clubs", "Diamonds", "Hearts", "Spades"]


@dataclass
class Card():
    value: int
    card: str
    suit: str

    def __str__(self):
        return f"{self.card} of {self.suit}"
    
cards = []
for x in range(10):
    value = random.randint(1,13)
    suit = random.choice(suits)
    if value == 1:
        card = "Ace"
    elif value == 11:
        card = "Jack"
    elif value == 12:
        card = "Queen"
    elif value == 13:
        card = "King"
    else:
        card = value

    cards.append(Card(value, card, suit))


def swapValues(list, index):
    temp = list[index]
    list[index] = list[index+1]
    list[index+1] = temp
    return list


for outer in range (len(cards)-1,0,-1):
    for inner in range(outer):
        if ord(cards[inner].suit[:1])>ord(cards[inner+1].suit[:1]):
            swapValues(cards, inner)
        
        elif cards[inner].suit == cards[inner+1].suit:
            if cards[inner].value > cards[inner+1].value:
                swapValues(cards, inner)


for x in range(len(cards)):
    print(cards[x])