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

player = character("Player", 100, 5, 7, 6)
monster = character("Goblin", 75, 6, 6, 5)

print(f"A {monster.name} approaches.")

def main():
    mAction = rd.randint(1,3)
    pAction = int(input("Choose an action (1. Fight, 2. Block or 3. Dodge)(1, 2 or 3): "))

    if pAction == 1:
        fight(mAction)
    if pAction == 2:
        block()
    if pAction == 3:
        dodge()

def fight(mAction):
    if mAction == 1:
        print(f"You and the {monster} both try to fight.")
        if skillCheck(player.speed) > skillCheck(monster.speed):
            print(f"You slide by the {monster} strike it.")
            damage(player, monster, 5)
        else:
            print(f"The {monster} strikes you.")
            damage(monster, player, 5)

    elif mAction == 2:
        print(f"The {monster} tries to block your attack.")
        if skillCheck(monster.strength) > skillCheck(player.strength):
            print(f"The {monster} blocked you.")
        else:
            print("You break through the block")
            damage(player, monster, 5) 

def block():
    pass

def dodge():
    pass

def skillCheck(type):
    value = rd.randint(1,10) + type
    return value

def damage(attack, defence, mod):
    mod = rd.randint(1, mod)
    damage = mod + attack.damage
    defence.health -= damage
    print(f"{defence} took {damage}hp of damage.")

while monster.health > 0:
    main()