myList = [3,4,9,7,1]
counter = 0 

for outer in range (len(myList)-1,0,-1):
    for inner in range(outer):
        if myList[inner]<myList[inner+1]:
            temp = myList[inner]
            myList[inner] = myList[inner+1]
            myList[inner+1] = temp
            counter += 1
  

print("Bubble sort complete in", counter, "swaps.")
print(myList)
