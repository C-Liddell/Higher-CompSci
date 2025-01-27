# RECAP - UFO
# Original task by Mr Neil, adapted by Mr Simpson

import csv
thisDate = []
country = []
location = []
shape = []
description = []
filePath = 'Assignments/Practice/'

# -------------------------------------------------- DO NOT ALTER -----
def importFile():
    with open(filePath+'ufo_sighting.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            thisDate.append(row[0])
            country.append(row[1])
            location.append(row[2])
            shape.append(row[5])
            description.append(row[6])
    return thisDate, country, location, shape, description
# -------------------------------------------------- DO NOT ALTER -----

thisDate, country, location, shape, description = importFile()


specifiedCountry = str(input("Enter a country: "))

def CountSightings(c, sC):
    count = 0
    for country in c:
        if country == sC:
            count += 1 
    return count

def DisplaySightings(sC, nS):
    print(f"There were {nS} sightings in {sC}")
    
numSightings = CountSightings(country, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)


def CountYearSightings(d):
    count = -1
    lastYear = d[0][6:10]
    for date in d:
        thisYear = date[6:10]
        if thisYear == lastYear:
            count += 1
        else:
            print(f"{thisYear}: {count}")
            count = 0
            lastYear = thisYear

CountYearSightings(thisDate)


def FindSightingsByLocation(l, tD, s, d):
    specifiedLocation = str(input("Enter a location to search for: "))
    for pos in range(0, len(l)):
        if l[pos] == specifiedLocation:
            print(f"{tD[pos]}, {s[pos]}, {d[pos]}")

FindSightingsByLocation(location, thisDate, shape, description)