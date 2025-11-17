myList = ["G", "X", "b", "P", "z"]


for index in range (1,len(myList)):
    currentvalue = myList[index]
    position = index

    while position > 0 and ord(myList[position-1]) > ord(currentvalue):
        myList[position] = myList[position-1]
        position -= 1

    myList[position] = currentvalue


print(myList)