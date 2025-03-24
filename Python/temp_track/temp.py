from dataclasses import dataclass

@dataclass
class TEMP():
    day: str
    dayTemp: float



def getValidTemps():
    temps = []
    for i in range(3):
        day = str(input(f"Enter day of the week {i+1}: "))
        temp = float(input(f"Enter temperature {i+1}: "))
        while temp > 50 or temp < -20:
            print("Enter a valid temperature.")
            temp = float(input(f"Enter temperature {i+1}: "))
        temps.append(TEMP(day, temp))
    return temps



def findMax(temps):
    max = -20
    for i in temps:
        if i.dayTemp > max:
            max = i.dayTemp
    return max
    


def findMin(temps):
    min = 50
    for i in temps:
        if i.dayTemp < min:
            min = i.dayTemp
    return min



def findAvg(temperatures):
    avg = 0
    for i in temperatures:
        avg += i.dayTemp
    avg = avg / (len(temperatures))
    return avg



def displayOutput(temps, max, min, avg):
    print("The temperatures entered were:")
    for i in temps:
        print(f"{i.day}: {i.dayTemp}oC")
    print(f"The highest temperature was {max}oC. The lowest temperature was {min}oC.")
    print(f"The average temperture was {avg}oC.")



def writeFile(avgTemp):
    with open("Python/temp_track/avgTemp.txt", "w") as file:
        file.write(str(avgTemp))



temperatures = getValidTemps()
maxTemp = findMax(temperatures)
minTemp = findMin(temperatures)
avgTemp = findAvg(temperatures)
displayOutput(temperatures, maxTemp, minTemp, avgTemp)
writeFile(avgTemp)