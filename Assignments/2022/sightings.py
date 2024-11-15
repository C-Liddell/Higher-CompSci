from dataclasses import dataclass
import csv


@dataclass
class sighting:
    town: str
    mammal: str
    date: str
    age: int


def read():
    sightings = []
    with open("Assignments/2022/mammals.txt", "r") as file:
        reader = csv.reader(file)
        for i in reader:
            sightings.append(sighting(i[0], i[1], i[2], int(i[3])))
    return sightings


def findMaxAge(sightings):
    maxAge = 0
    for i in sightings:
        if i.age > maxAge:
            maxAge = i.age
    print(f"The oldest walker was {maxAge}.")


def findDates(sightings):
    town = capitalise(str(input("Enter town: ")))
    mammal = capitalise(str(input("Enter mammal: ")))
    print("The dates of the sightings were: ")
    for i in sightings:
        if i.town == town and i.mammal == mammal:
            print(i.date)


def capitalise(string):
    character = ord(string[0])
    if character >= 97 and character <= 122:
        character = chr(character - 32)
        string = character + string[1:len(string)]
    return string
    

def findSightingsPerDay(sightings):
    counter = 0
    dayToCount = sightings[0].date
    for i in sightings:
        if i.date == dayToCount:
            counter += 1
        else:
            print(f"Day to count: {dayToCount}, Count: {counter}")
            dayToCount = i.date
            counter = 1
    print(f"Day to count: {dayToCount}, Count: {counter}")


sightings = read()
findMaxAge(sightings)
findDates(sightings)
findSightingsPerDay(sightings)