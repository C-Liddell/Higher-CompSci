# A lot of action can occur in the second-half of a hockey match as teams get tired.

# Input the half-time score as 2 whole numbers on 2 separate lines.

# Input the full-time score as 2 whole numbers on 2 separate lines.

# Output the number of goals scored after the half-time break.

# Input Format
# Four lines each containing one non-negative whole number

# Output Format
# One non-negative whole number

"""
Ask for and store home team half time score
Ask for and store away team half time score
Ask for and store home full time score
Ask for and store away full time score
Calculate the total number of goals scored after the half time break
Output the number of goals scored after the half time break
"""

home_halfTimeScore = int(input("Enter home team half time score: "))
away_halfTimeScore = int(input("Enter away team half time score: "))
home_fullTimeScore = int(input("Enter home team full time score: "))
away_fullTimeScore = int(input("Enter away team full time score: "))

postHalfTimeGoals = (home_fullTimeScore - home_halfTimeScore) + (away_fullTimeScore - away_halfTimeScore)
print(f"The number of goals scored after half time were {postHalfTimeGoals}.")
