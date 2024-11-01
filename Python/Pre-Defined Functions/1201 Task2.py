def capitalise(name):
    name = chr((ord(name[0])) - 32)
    return name

animal = str(input("Please enter the name of an animal: "))
character = capitalise(animal)
print(character + animal[1:len(animal)])
