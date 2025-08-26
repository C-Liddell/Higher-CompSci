# Input a sequence of single characters, one per line, each A or B, to indicate a series of tennis points won in a single game.

# An input of A indicates that the server won the point, whilst B indicates that the receiver won the point.

# The scores in a game of tennis are awarded for each player as:
# 0, 15, 30, 40, game
# where each point won increases the player's score to the next score. 

# However if the score reaches 40-40, the game is said to be at deuce. 

# In this case, the player who wins the next point is said to be at advantage but does not immediately win the game.

# If the player with advantage wins the next point, they win the game otherwise the game returns to deuce.

# Output the number of deuces that occurred in the game.

# Input Format
# A sequence of single characters, one per line, each A or B

# Output Format
# A single non-negative whole number

# Example Input
# A
# A
# B
# A
# B
# B
# A
# B
# B
# A
# B
# B
# Example Output
# 3
# Example Explanation
# The game progressed as follows:
# 15-0, 30-0, 30-15, 40-15, 40-30, 40-40 (deuce), Advantage A, 40-40 (deuce), Advantage B, 40-40 (deuce), Advantage B, Game to B.
# A,A,B,A,B,B,A,B,B,A,B,B

# In total there were 3 deuces so the output is 3.

# Constraints
# All input sequences will lead to a game win for one of the two players
# There will be a maximum of 10 deuces

"""
1.1 Set playerA to 0
1.2 Set playerB to 0
1.3 Set gameNotOver to True
1.4 Set noDeuces to 0



5.1 If playerA == “0” then
5.2      Set playerA to “15”
5.3 Else if playerA == “15” then
5.4      Set playerA to "30"
5.5 Else if playerA == "30" then
5.6      Set playerA to "40"
5.7 Else if playerA == "40" then
5.8      If playerB == “40” then
5.9           Set playerA to “A”
5.10    Else
5.11         Set gameNotOver to False
5.12    End if
5.13 Else if playerA == "A" then
5.14      Set gameNotOver to False
5.15 End if
5.16 If playerA == “40” and playerB == "40" then
5.17      Increase noDeuces by 1
5.18 End if



7.1 If playerB == “0” then
7.2      Set playerB to “15”
7.3 Else if playerB == “15” then
7.4      Set playerB to "30"
7.5 Else if playerB == "30" then
7.6      Set playerB to "40"
7.7 Else if playerB == "40" then
7.8      If playerA == “40” then
7.9           Set playerB to “A”
7.10    Else
7.11         Set gameNotOver to False
7.12    End if
7.13 Else if playerB == "A" then
7.14      Set gameNotOver to False
7.15 End if
7.16 If playerB == “40” and playerA == "40" then
7.17      Increase noDeuces by 1
7.18 End if



1.Set up variables
2.While gameNotOver and noDeuces < 10 do
3.     Ask for and store a valid letter
4.     If letter = “A” then
5.          Change player score (A)
6.     Else
7.          Change player score (B)
8.     End if
9.End while
10.Output the number of deuces that occurred in the game
"""


def init():
    pA = 0
    pB = 0
    gNO = True
    nD = 0
    return pA, pB, gNO, nD


def getValidLetter():
    enter = str(input("Enter a valid letter (A/B): "))
    while enter != "A" and enter != "B":
        print("Error.")
        enter = str(input("Enter a valid letter (A/B): "))
    return enter


def scorePlayerA(pA, pB, gNO, nD):
    if pA == 0:
        pA = 15
    elif pA == 15:
        pA = 30
    elif pA == 30:
        pA = 40
    elif pA == 40:
        if pB == 40:
            pA = "A"
        else:
            gNO = False
    elif pA == "A":
        gNO = False

    if pA == 40 and pB == 40:
        nD += 1

    return pA, gNO, nD 


def scorePlayerB(pA, pB, gNO, nD):
    if pB == 0:
        pB = 15
    elif pB == 15:
        pB = 30
    elif pB == 30:
        pB = 40
    elif pB == 40:
        if pA == 40:
            pB = "A"
        else:
            gNO = False
    elif pB == "A":
        gNO = False

    if pA == 40 and pB == 40:
        nD += 1

    return pB, gNO, nD 



playerA, playerB, gameNotOver, noDeuces = init()
while gameNotOver and noDeuces < 10:
    letter = getValidLetter()
    if letter == "A":
        playerA, gameNotOver, noDeuces = scorePlayerA(playerA, playerB, gameNotOver, noDeuces)
    if letter == "B":
        playerB, gameNotOver, noDeuces = scorePlayerB(playerA, playerB, gameNotOver, noDeuces)
print(f"The number of deuces is {noDeuces}.")