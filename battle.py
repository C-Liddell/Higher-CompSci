import random as rd
from dataclasses import dataclass

@dataclass
class character:
    name: str
    health: int
    damage: int
    speed: int
    strength: int

    def __str__(self):
        return self.name

player = character("player", 100, 5, 7, 6)
monster = character("monster", 75, 6, 6, 5)

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
        if getStrength(player) > getStrength(monster):
            print("You slide by the monsters attack and strike it.")
            pDamage = rd.randint(1,5) + player.damage
            takeDamage(monster, pDamage)
        else:
            print("The monster strikes you.")
            mDamage = rd.randint(1,5) + monster.damage
            takeDamage(player, mDamage)
    elif mAction == 2:
        print("The monster tries to block your attack.")
        if getStrength(monster) > getStrength(player):
            print("The monster blocked you.")
        else:
            print("You break through the block")
            pDamage = rd.randint(1,5) + player.damage - (monster.strength/2)
            takeDamage(monster, pDamage)
    

def block():
    pass

def dodge():
    pass

def getStrength(name):
    name = rd.randint(1,10) + name.strength
    return name

def takeDamage(name, damage):
    name.health -= damage
    print(f"{name} took {damage}hp of damage.")

while monster.health > 0:
    main()