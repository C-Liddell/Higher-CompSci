import csv

def read():
    attraction = []
    category = []
    visitors = []
    daysOpen = []
    height = []
    with open("Assignments/2023/attractions.csv", "r") as file:
        data = csv.reader(file)
        for rows in data:
            attraction.append(str(rows[0]))
            category.append(str(rows[1]))
            visitors.append(int(rows[2]))
            daysOpen.append(int(rows[3]))
            height.append(str(rows[4]))
    return attraction, category, visitors, daysOpen, height

def visitedAttractions(attraction, visitors):
    maxPos = 0
    maxValue = 0

    minPos = 0
    minValue = 1000000
    for i in range(0, len(visitors)):
        if visitors[i] > maxValue:
            maxPos = i


def write(attraction, category, daysOpen):
    pass

attraction, category, visitors, daysOpen, height = read()
visitedAttractions(attraction, visitors)
write(attraction, category, daysOpen)