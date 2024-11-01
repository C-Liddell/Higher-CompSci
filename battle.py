import random as rd

class character():
    def __init__(self, health, strength, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
        self.strength = strength

player = character(100, 5, 7, 6)
monster = character(75, 8, 6, 4)

print("A monster approaches.")

def main():
    mAction = rd.randint(1,3)
    print("""
          The Monster looms in front of you.
          Would you like to...

          1. Fight
          2. Block
          3. Dodge

 """)
    pAction = int(input("Your action: "))
    if pAction == 1:
        fight(mAction)
    if pAction == 2:
        block()
    if pAction == 3:
        dodge()

def fight(mAction):
    if mAction == 1:
        print("You and the monster both take a swing at each other.")
        pStrength = rd.randint(1,10) + player.strength
        mStrength = rd.randint(1,10) + monster.strength
        if pStrength > mStrength:
            ("You slide by the monsters attack and strike it.")

def block():
    pass

def dodge():
    pass

while monster.health > 0:
    main()