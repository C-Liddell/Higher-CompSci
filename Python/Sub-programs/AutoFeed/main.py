
def getTotalWeight():
    totalWeight = 0
    allFoodWeight = []
    for i in range(5):
        while True:
            try:
                foodWeight = int(input(f"Enter the food weight {i+1}: "))
                while foodWeight < 0 or foodWeight > 200:
                    print("Error. A single container can only hold up to 200g.")
                    foodWeight = int(input(f"Enter the food weight {i+1}: "))
                break
            except:
                print("Error. Enter a valid number.")
        allFoodWeight.append(foodWeight)
        totalWeight = totalWeight + foodWeight
    return (totalWeight, allFoodWeight)

def getDogSize():
    dogSize = str(input("Please enter the size of your dog (small, medium or large): "))
    while dogSize != "small" and dogSize != "medium" and dogSize != "large":
        print("Error. Enter a valid size.")
        dogSize = str(input("Please enter the size of your dog (small, medium or large): "))
    return(dogSize)

def getMessage(totalWeight, dogSize):
    if dogSize == "small" and (totalWeight >= 110 and totalWeight <= 140):
        message = "This weight of food is suitable for your small dog."
    elif dogSize == "medium" and (totalWeight >= 330 and totalWeight <= 440):
        message = "This weight of food is suitable for your medium dog."
    elif dogSize == "large" and (totalWeight >= 690 and totalWeight <= 900):
        message = "This weight of food is suitable for your large dog."
    else:
        message = "This weight of food is not recommended for the size of your dog."
    return(message)

def getAvgWeight(totalWeight):
    avgWeight = totalWeight/5
    avgWeight = round(avgWeight, 1)
    return(avgWeight)

def output(allFoodWeight, totalWeight, avgWeight, message):
    for i in range(5):
        print(f"The food weight of container {i+1} is {allFoodWeight[i]}.")
    print(f"The total food weight is {totalWeight}.")
    print(f"The average food weight is {avgWeight}.")
    print(message)


totalWeight, allFoodWeight = getTotalWeight()
dogSize = getDogSize()
message = getMessage(totalWeight, dogSize)
avgWeight = getAvgWeight(totalWeight)
output(allFoodWeight, totalWeight, avgWeight, message)