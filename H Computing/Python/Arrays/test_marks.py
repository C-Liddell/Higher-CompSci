names = []
marks = []

for i in range(5):
    names.append(str(input(f"What is name number {i+1}? ")))
    marks.append(int(input(f"What mark did {names[i]} get (1-100)? ")))
    
    while marks[i] < 1 or marks[i] > 100:
        print("Error. Please enter a number between 1-100.")
        marks[i] = int(input(f"What mark did {names[i]} get (1-100)? "))

print(names, marks)