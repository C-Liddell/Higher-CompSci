numbers = [x for x in range(32)]

target = 19
startpos = 0
endpos = len(numbers)-1
counter = 0
found = False

while found == False and (startpos<=endpos):
    middle = int((startpos+endpos)//2)
    if numbers[middle] == target:
        found = True
    elif numbers[middle] < target:
        startpos = middle + 1
    else:
        endpos = middle - 1
    counter = counter + 1

if found == True:
    print("I found",target,"in",counter,"iterations.")
else:
    print("I didn't find",target)
