from dataclasses import dataclass

@dataclass
class node():
  data : str = ''
  nextptr : int = -1

fat = [node() for x in range(7)]
headptr = 0 # position of first node

fat[0].data = "Red"
fat[1].data = "Orange"
fat[2].data = "Yellow"
fat[3].data = "Green"
fat[4].data = "Blue"
fat[5].data = "Indigo"
fat[6].data = "Violet"

fat[0].nextptr = 1
fat[1].nextptr = 2
fat[2].nextptr = 3
fat[3].nextptr = 4
fat[4].nextptr = 5
fat[5].nextptr = 6
fat[6].nextptr = 7

print("headptr : ",headptr)
for x in range(12):
  print(x,": ",fat[x].data, "-> ",fat[x].nextptr)

# Process linked list
nextptr = headptr
while nextptr != -1:
  data = fat[nextptr].data
  nextptr = fat[nextptr].nextptr
  print(data)
