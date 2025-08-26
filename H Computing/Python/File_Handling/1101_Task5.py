temps = []

with open("Python/File_Handling/temps.txt", "r") as file:
    contents = file.readlines()
    for lines in contents:
        temps.append(int(lines.strip()))
print(temps)

total = 0 

for i in temps:
    total += i

avgTemp = total/len(temps)
print(avgTemp)

