from dataclasses import dataclass

@dataclass
class node():
  data : str = ''
  nextptr : int = -1

countries = [node() for x in range(12)]
headptr = 0





print("headptr : ",headptr)
for x in range(12):
  print(x,": ",countries[x].data, "-> ",countries[x].nextptr)

# Process linked list
nextptr = headptr
while nextptr != -1:
  data = fat[nextptr].data
  nextptr = fat[nextptr].nextptr
  print(data)