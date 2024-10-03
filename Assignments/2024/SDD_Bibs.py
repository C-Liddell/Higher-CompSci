import csv

def getData():
    entryID = []
    location = []
    forename = []
    surname = []
    jumps = []
    with open("athletes.csv") as csvfile:
        reader = csv.reader(csvfile)
        for i in reader:
            entryID.append(i[0])
            location.append(i[1])
            forename.append(i[2])
            surname.append(i[3])
            jumps.append(int(i[4]))
    return entryID, location, forename, surname, jumps

def storeBibValues(entryID, location, forename, surname):
    bibValues = []
    with open("bibValues.csv", "w") as csvfile:
        for i in range(0, len(entryID)):
            bibValues.append(forename[i][0] + surname[i] + str(ord(location[i][0])))
            csvfile.write(entryID[i] + "," + bibValues[i] + "\n")

def getMaxJumps(jumps):
    maxJumps = jumps[0]
    for i in range(1, len(jumps)):
        if jumps[i] > maxJumps:
            maxJumps = jumps[i]
    return maxJumps

def displayMaxJumps(forename, surname,maxJumps, jumps):
    pass

entryID, location, forename, surname, jumps = getData()
storeBibValues(entryID, location, forename, surname)
maxJumps = getMaxJumps(jumps)
displayMaxJumps(forename, surname, maxJumps, jumps)