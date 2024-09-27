# Linear search

array = [1,6,4,8,3,2,7,3,4,6,8]
target = int(input("Enter number to search for: "))
found = False
pos = -1

for index in range(len(array)):
    if array[index] == target:
        print("Found it.")
        found = True
        print("Index is",index)
        pos = index

if pos == -1:
    print("Not found.")
else:
    print("Found",target,"at",pos) # only possible if you store pos
print("Loop end.")