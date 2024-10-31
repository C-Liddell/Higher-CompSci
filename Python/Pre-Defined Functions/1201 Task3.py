def getPass():
    password = str(input("Please enter a secure password: "))
    return password

def checkCap(password):
    character = ord(password[0])
    if character > 64 and character < 91:
        print("Your password begins with a capital letter. Good!")
        return True
    else:
        print("This password is not secure. Try again.")
        return False

def checkSymbol(password):
    character = ord(password[-1])
    if character > 34 and character < 38:
        print("Your password ends with a symbol. Good!")
        return True
    else:
        print("This password is not secure. Try again.")
        return False
    
password = getPass()

while checkCap(password) != True or checkSymbol(password) != True:
    password = getPass()

print("This password is secure. Well done.")

