myList = ["G","X","b","P","z"]


for outer in range (len(myList)-1,0,-1):
    for inner in range(outer):
        if ord(myList[inner])>ord(myList[inner+1]):
            temp = myList[inner]
            myList[inner] = myList[inner+1]
            myList[inner+1] = temp
  

print(myList)
