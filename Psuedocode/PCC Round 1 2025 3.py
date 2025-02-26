# Everyone likes as many Saturdays as possible in a year.

# A year has 365 days unless it is a leap year which gives it an extra day.

# The number of Saturdays in a year can be calcuated from the day of the week which 1st January lies on and whether it is a leap year or not.

# Input the week day for January 1st in uppercase two letter format (MO / TU / WE / TH / FR / SA / SU).

# Also input whether it is a leap year or not as y (for yes) or n (for no).

# Output the number of Saturdays which that year will contain.

# Input Format
# A line specifying a week day using two uppercase letters
# A second line with a single character (y or n)

# Output Format
# One positive whole number

"""
Ask for and store a valid day of the week
Ask for and store leap year
Calculate number of saturdays in year
Output saturdays in year

Ask for and store day of the week
    While day of the week not in list (MO, TU, WE, TH, FR, SA, SU) Do
    Output error message
    Ask for and store day of the week
End While
"""

def vaildDOW():
    validInputs = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"]
    d = str(input("Enter a day of the week in format (MO/ TU/ WE/ TH/ FR/ SA/ SU): "))
    while d not in validInputs:
        print("Error")
        d = str(input("Enter a day of the week in format (MO/ TU/ WE/ TH/ FR/ SA/ SU): "))
    return d

DOW = validDOW()