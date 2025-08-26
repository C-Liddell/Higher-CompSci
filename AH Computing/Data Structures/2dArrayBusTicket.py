seat = [ ['' for col in range(5)] for row in range(2)]

seat[0][0] = 'D'
seat[0][1] = 'AB'
seat[0][2] = 'MD'
seat[1][4] = 'LL'
seat[1][0] = 'ES'
seat[1][2] = 'T'

for row in range(2):
  print(seat[row])

initial = str(input("Enter your intials: "))
row = int(input("Enter row: "))
column = int(input("Enter column: "))

while seat[row][column] != "":
  print("Seat taken.")
  row = int(input("Enter row: "))
  column = int(input("Enter column: "))

seat[row][column] = initial