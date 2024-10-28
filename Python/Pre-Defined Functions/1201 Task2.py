def capitalise(name):
    name = ord(name[0])
    name -= 32
    name = chr(name)
    return name

animal = str(input("Please enter the name of an animal: "))
character = capitalise(animal)
print(character + animal[1:len(animal)])
