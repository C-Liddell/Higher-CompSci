myList = [3,4,9,7,1]


for index in range (1,len(myList)):
    currentValue = myList[index]
    position = index

    while position > 0 and myList[position-1]>currentValue:
        myList[position] = myList[position-1]
        position -= 1

    myList[position] = currentValue
    print(myList)


print(myList)