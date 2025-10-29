myList = [3,4,9,7,1]


for outer in range (len(myList)-1,0,-1):
    for inner in range(outer):
        if myList[inner]<myList[inner+1]:
            temp = myList[inner]
            myList[inner] = myList[inner+1]
            myList[inner+1] = temp
  

print(myList)
