# Ahoy, matey! To become a pirate, ye need to learn how to speak like one.

# Your task is to write a program that translates a sentence into pirate speak.

# To do this, you should replace the following words with their pirate speak equivalents provided, leaving all other words unchanged:

# "hello" -> "ahoy"
# "friend" -> matey
# "my" -> "me"
# "you" -> "ye"
# "yes" -> "aye"
# Input a positive whole number n followed by n lines, each containing a single word from the original sentence.

# Output the sentence translated into pirate-speak as a single line of space-separated words with no punctuation.

# Input Format
# A positive whole number n
# ...followed by n lines each consisting of a single lowercase word

# Output Format
# One single line of space-separated words

# Example Input
# 4
# hello
# my
# good
# friend
# Example Output
# ahoy me good matey
# Constraints
# n will be between 1 and 20 inclusive
# All inputted words will only contain the lowercase letters a-z

"""
Ask for and store a valid  number of lines
Set up an empty array called sentence
Loop number of lines times
     Ask for and store word as a new item in the sentence array
End Loop
Translate words into pirate-speak
Output pirate-speak

Ask for and store a valid number of lines
While number of lines < 1 Then
    Display error message
    Ask for and store a valid number of lines
End While

Loop for each word in the sentence array
    If current word = “hello” then
        Change the current word to “ahoy”
    Else if current word = “friend” then
        Change the current word to “matey”
    Else if current word = "my" then
        Change the current word to "me"
    Else if current word = "you" then
        Change the current word to "ye"
    Else if current word = "yes" then
        Change the current word to "aye"
    End if
End loop
"""


def getNoLines():
    no = int(input("Enter a valid number of lines: "))
    while no < 1:
        print("Error. Please enter a valid input")
        no = int(input("Enter a valid number of lines: "))
    return no


def translate(sentence):
    for i in range(0, len(sentence)):
        if sentence[i] == "hello":
            sentence[i] = "ahoy"
        elif sentence[i] == "friend":
            sentence[i] = "matey"
        elif sentence[i] == "my":
            sentence[i] = "me"
        elif sentence[i] == "you":
            sentence[i] = "ye"
        elif sentence[i] == "yes":
            sentence[i] = "aye"
    return sentence


noLines = getNoLines()
sentence = []
for i in range(noLines):
    word = str(input(f"Enter word number {i+1}: "))
    sentence.append(word)
sentence = translate(sentence)
print(' '.join(sentence))


