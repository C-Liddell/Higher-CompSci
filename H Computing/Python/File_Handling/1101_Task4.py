names = ["John","Joan","Mark","Michael"]
birthMonth = ["May", "June", "July", "August"]
ages = [23,35,23,8]

with open("Python/File_Handling/names.txt","w") as wfile:
    for counter in range(0,len(names)):
        wfile.write(f"{names[counter]},{birthMonth[counter]},{str(ages[counter])}\n")

