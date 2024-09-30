# 805Task4.py
# Standard Algorithms - Linear Search & Counting Occurrences

# Investigate and modify

def getTarget():
  targetAnimal = input("Please enter the target animal you are searching for")

  return targetAnimal

def getCircusAnimalsList():
  animals = ["giraffe", "chicken", "lion", "cheetah", "rat", "elephant", "snake", "chicken", "horse"]

  return animals

def countOccurrences(targetAnimal, animals):
  occurrences = 0
  for i in range(1,len(animals)):
    if animals[i] == targetAnimal:
      occurrences += 1
  return occurrences


def printOccurrences(occurrences):
  print(occurrences)


#*************  MAIN *************

targetAnimal = getTarget()
animals= getCircusAnimalsList()
occurrences = countOccurrences(targetAnimal, animals)
printOccurrences(occurrences)