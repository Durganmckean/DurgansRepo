# CS 16X Git Assignment

# Project requires TWO functions:
# 1. rect_area (length, width) which will return the area of a rectangle
# 2. rect_solid_area (length, width, height) which will return the area of a solid rectangular object

# The following four lines are just there to make the code work without errors until functions are added
'''def rect_solid_area(x, y, z):
    return 1
length = 1; width = 1; height = 1
rect_solid_area (length, width, height)'''


# I (Durgan) wrote both functions on this


# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as in integer: "))
width = int(input("Enter the width of the the object as in integer: "))
height = int(input("Enter the height of the the object as in integer: "))

rect_area = length * width

rect_surface_area = 2*rect_area + 2*length*height + 2*width*height

surface_area = rect_surface_area

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", surface_area)