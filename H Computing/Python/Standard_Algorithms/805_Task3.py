# 805Task3.py
# Standard Algorithms - Linear Search & Counting Occurrences

# Investigate and modify

def getTargetCharacter():
  target = input("Enter the character you are looking for")

  return target

def getCharacters():
  characters = ["Desperate Dan", "Numbskulls", "Dennis the Menace", "Minnie the Minx", "Walter", "Gnasher", "Billy Whizz"]

  return characters

def findCharacterPosition(oneToFind):
  found = False
  foundPosition = -1
  i = 0
  while i < len(characters) and found == False:
    if characters[i] == target:
      found == True
      foundPosition = i
    i += 1
    
  return foundPosition

#. *************MAIN*************

target = getTargetCharacter()
characters = getCharacters()
foundPosition = findCharacterPosition(target)
if foundPosition != -1:
  print(f"{target} was found at {foundPosition}.")
else:
  print(f"{target} not found.")