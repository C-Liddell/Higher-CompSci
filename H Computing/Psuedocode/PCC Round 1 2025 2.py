# For a circus act, chairs of a certain type can be stacked as shown in which pairs of chairs fit together with one rotated.

# In this situation with 2 chairs there are 8 chair legs for every chair height.

# Other pairs of chairs are then stacked directly on top to form a tower so that every pair of chairs that the tower gets higher adds another 8 further chair legs.

# Input the height of one chair in cm.

# Input also the overall height of the stacked pair tower in cm.

# Output the total number of chair legs present in the tower.

# Input Format
# Two lines each containing one non-negative whole number

# Output Format
# One positive whole number (with no decimal point)

"""
Ask for and store height of one chair
Ask for and store height of tower
Calculate number of chair legs in tower
Output number of chair legs in tower
"""

chairHeight = int(input("Enter height of one chair in cm: "))
towerHeight = int(input("Enter height of the chair tower in cm: "))

noChairLegs = int((towerHeight/chairHeight)*8)
print(f"The number of legs in the chair tower is {noChairLegs}.")