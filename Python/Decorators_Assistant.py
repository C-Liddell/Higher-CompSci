def user_input():
    length = int(input("Enter length of room: "))
    breadth = int(input("Enter breadth of room: "))
    height = int(input("Enter height of room: "))
    return(length, breadth, height)

def area(length, breadth, height):
    floor_area = length*breadth
    wall_area = 2*(height*length) + 2*(height*breadth)
    return(floor_area, wall_area)

def calculations():
    pass
user_input()
area(length, breadth, height)