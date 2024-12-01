import random as rd
from dataclasses import dataclass
import os
import json

@dataclass
class character:
    name: str
    health: int
    damage: int
    speed: int
    strength: int

    def __str__(self):
        return self.name

with open("Game\player.json", "r") as file:
    data = json.load(file)
    player = character(data["name"], data["health"], data["damage"], data["speed"], data["strength"])

monster = character("Goblin", 75, 8, 9, 5)


def main():
    mAction = rd.randint(1,3)
    pAction = int(input("Choose an action (1. Fight, 2. Block or 3. Cast Spell)(1, 2 or 3): "))

    os.system("cls")

    if pAction == 1:
        fight(mAction)
    if pAction == 2:
        block(mAction)
    if pAction == 3:
        castSpell()

    print("")    


def fight(mAction):

    if mAction == 1:
        print(f"You and the {monster} both try to fight.")
        if skillCheck(player.speed) > skillCheck(monster.speed):
            print(f"You slide by the {monster} and strike it.")
            damage(player, monster, 5)

        else:
            print(f"The {monster} strikes you.")
            damage(monster, player, 5)


    elif mAction == 2:
        print(f"The {monster} tries to block your attack.")
        if skillCheck(monster.strength) > skillCheck(player.strength):
            print(f"The {monster} blocked successfully.")
            
        else:
            print("You break through the block.")
            damage(player, monster, 3)


    else:
        print(f"The {monster} tries to dodge.")
        if skillCheck(monster.speed) > skillCheck(player.speed):
            print(f"The {monster} dodged successfully.")
        else:
            print(f"The {monster} failed to dodge.")
            damage(player, monster, 4)


def block(mAction):

    if mAction == 1:
        print(f"You try and block the {monster} as it swings at you.")
        if skillCheck(player.strength) > skillCheck(monster.strength):
            print(f"You blocked successfully.")

        else:
            print(f"The {monster} breaks through your block.")
            damage(monster, player, 3)


    else:
        print(f"You raise your shield. You and the {monster} stare each other down.")


def castSpell():
    
    pass


def skillCheck(type):

    value = rd.randint(1,10) + type
    return value


def damage(attack, defence, mod):

    mod = rd.randint(1, mod)
    damage = mod + attack.damage
    defence.health -= damage
    print(f"{defence} took {damage}hp of damage.")


os.system("cls")
print(f"A {monster.name} approaches.")

while monster.health > 0:
    main()