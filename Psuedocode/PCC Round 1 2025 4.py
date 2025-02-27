# At the local PackingTins4U factory, tin cans are usually packed in squares of size x by x cans for efficiency with just one can high.

# However, if x is a single digit, then sometimes the factory runs a special offer by adding a certain number of additional rows of cans for free to make a rectangle pack of dimensions x + a cans along by x cans wide.

# First input x, the length of the square packs being made.

# If and only if relevant, also input whether a special offer is running which will be indicated by a y for special offer and n for no special offer.

# If and only if it is a special offer, also input a, the number of additional rows which are being included for free. This input will only be available if there is a special offer running.

# Output the number of tin cans that each pack will contain.

# Input Format
# One line specifying a positive whole number x
# ... on some occasions followed by a second line of a single character (y or n)
# ... and on some occasions a third line specifying a positive whole number a

# Output Format
# One positive whole number

"""
Ask for and store x
If x is a single digit then
     Ask for and store valid special offer 
     If special offer is yes then
          Ask for and store the number of additional rows included for free
Calculate number of tin cans in pack
Output number of tin cans in pack

Ask for and store special offer
While special offer is not y and special offer is not n Do
    Output error message
    Ask for and store special offer
End While
"""

def getValid():
    enter = str(input("Is a special offer running? (y/n): "))
    while enter != "y" and enter != "n":
        print("Error. Please enter a valid input.")
        enter = str(input("Is a special offer running? (y/n): "))
    return enter

addRows = 0
x = int(input("Enter length of pack: "))
if len(str(x)) == 1:
    specialOffer = getValid()
    if specialOffer == "y":
        addRows = int(input("How many extra rows would you like to add?: "))
noCans = x*(x+addRows)
print(f"The number of cans in this pack will be {noCans}.")