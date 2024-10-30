def getPass():
    password = str(input("Enter password: "))
    return password

def checkCap(password):
    character = ord(password[0])
    if character > 64 and character < 91:
        return True
    else:
        return False

def checkSymbol(password):
    character = ord(password[-1])
    if character > 34 and character < 38:
        return True
    else:
        return False
    
password = getPass()

while checkCap(password) != True or checkSymbol(password) != True:
    password = getPass()

print("Success")

