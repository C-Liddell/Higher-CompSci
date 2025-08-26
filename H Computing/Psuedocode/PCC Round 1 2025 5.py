# An outline ASCII image can be made just using symbols for the outline and spaces elsewhere.

# For this batch of images, the first and last line must be entirely made of non-space symbols. The remaining lines must each contain exactly two non-space symbols, to mark the left and right side of the outline, but contain spaces for all other characters.

# Acceptable outline ASCII images, of a factory and a sand timer, are shown below.

# Input a single positive whole number to specify how many lines the image will contain. Then input that number of lines.

# Output the number of symbols, excluding spaces, that have been used to make the image.

# Input Format

# One line specifying a positive whole number n
# ... followed by n lines of text

# Output Format
# One positive whole number

# Example Input 1
# 6
# +-+
# | |
# |  \
# |   |
# |   |
# +---+
# Example Output
# 16
# Example Input 2
# 8
# +-------+
# \      /
#  \    /
#   \  /
#   /  \
#  /    \
# /      \
# +-------+
# Example Output 2
# 30

"""
Ask for and store a valid  number of lines
Set up an empty array called image
Loop number of lines times
     Ask for and store image line as a new item in the image array
End Loop
Calculate number of non-space symbols
Output number of non-space symbols

Ask for and store a valid number of lines
While number of lines < 1 Then
    Display error message
    Ask for and store a valid number of lines
End While

Set count to 0
Loop for each line in the image array
      Loop for each character in the current line
           If current character is not a space then
                Increment count by 1
           End if
      End loop
End loop
"""

def getNoLines():
    no = int(input("Enter a valid number of lines: "))
    while no < 1:
        print("Error. Please enter a valid input")
        no = int(input("Enter a valid number of lines: "))
    return no

def getNoSymbols(image):
    count = 0
    for line in image:
        for character in line:
            if ord(character) != 32:
                count += 1
    return count

noLines = getNoLines()
image = []
for i in range(noLines):
    line = str(input(f"Enter line {i+1}: "))
    image.append(line)
noSymbols = getNoSymbols(image)
print(f"The number of symbols in the image that aren't space is {noSymbols}.")