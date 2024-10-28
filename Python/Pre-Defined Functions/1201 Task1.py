password = str(input("Enter password: "))
total = 0

for i in range(len(password)):
    total += ord(password[i])

checkDigit = str(total % 11)
updatedPassword = password + checkDigit

with open("Python/Pre-Defined Functions/password.txt", "w") as file:
    file.write(updatedPassword)