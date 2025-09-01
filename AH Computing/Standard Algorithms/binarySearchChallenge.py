def initialise():
 searchlist1 = [1,3,5,7,9,11,13,17,18,19]
 searchlist2 = 
 print("Original list:",searchlist)
 return searchlist


def BinarySearch(searchlist,goal):
 found = False
 startpos = 0
 endpos = len(searchlist) -1


 print ("Endpos at beginning = ",endpos)


 while (startpos <= endpos) and found == False:
     middle = (startpos+endpos)//2 #Integer Division
     if searchlist[middle] == goal:
         found = True
     elif searchlist[middle]<goal:
         startpos = middle + 1
     else:
         endpos = middle -1


 if found == True:
   print("Match has been found at position",middle)
 else:
   print("Goal not found")


values = initialise()


goal = int(input("Enter goal"))
BinarySearch(values,goal)

