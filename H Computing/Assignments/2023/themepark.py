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
    maxValue = visitors[0]
    minPos = 0
    minValue = visitors[0]

    for i in range(0, len(visitors)):
        if visitors[i] > maxValue:
            maxPos = i
            maxValue = visitors[i]
        if visitors[i] < minValue:
            minPos = i
            minValue = visitors[i]

    print(f"The most visited attraction is {attraction[maxPos]}. The least visited attraction is {attraction[minPos]}.")


def write(attraction, category, daysOpen):
    with open("Assignments/2023/service.csv", "w") as file:
        for i in range(0, len(attraction)):
            if category[i] == "Roller Coaster":
                days = daysOpen[i]%90
                if (90-days) <= 7:
                    file.write(f"{attraction[i]},")


def heightRestriction(attraction, height):
    count = 0
    list = []
    for i in range(0, len(height)):
        if str(height[i])[0] == "1":
            count += 1
            list.append(attraction[i])
    print(f"There are {count} attractions with a height restriction of over 1m. They are: {', '.join(list)}.")


attraction, category, visitors, daysOpen, height = read()
visitedAttractions(attraction, visitors)
write(attraction, category, daysOpen)
heightRestriction(attraction, height)