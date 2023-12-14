"""
Task 1: Calculate Area with Conditions
Write a Python function calculate_area that takes two parameters: length and width. It
should calculate and return the area of a rectangle. However, add a condition: if the length
is equal to the width, return "This is a square!" instead of the area. Then, write a program to
input values for length and width from the user and call the calculate_area function to
display either the area or the message.
"""

def calculate_area(l,w):
    if l==w:
        return "This is a square"
    else:
        return l*w

length = float(input("Enter the length : "))
width = float(input("Enter the width : "))
c= calculate_area(length,width)
if type(c)==str:
    print(c)
else:
    print("Area of rectangle is : ",c)