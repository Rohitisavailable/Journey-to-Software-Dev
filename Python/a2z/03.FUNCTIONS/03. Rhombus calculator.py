def calculate_square_area(side: float):
    return side * side
#this function calculates the area of a square given the length of one side

def calculate_rectangle_area(length: float, width: float):
    return length * width
#this function calculates the area of a rectangle given its length and width

def calculate_circle_area(radius: float):
    pi =3.14
    return pi * radius ** 2
#this function calculates the area of a circle given its radius

def calculate_rhombus_area(p:float, q:float):
    return (p * q)/2
#this function calculates the area of a rhombus given its diagonals p and q
#this function calculates the area of a rhombus given the lengths of its diagonals p and q


print("""
--------------
Area Calculator
--------------
Select a shapeH
""")

selection = input("""
---------------------
\t'S' - Square
\t'R' - Rectangle
\t'C' - Circle
\t"H' - Rhombus
---------------------
""")

def calculate_area(selection):
    area = 0
    if selection == 'S':
        side = input("Enter the side")
        area = calculate_square_area(float(side))
    elif selection == 'R':
        length = input("Enter the length")
        width = input("Enter the width")
        area = calculate_rectangle_area(float(length), float(width))
    elif selection == 'C':
        radius = input("Enter the radius")
        area = calculate_circle_area(float(radius))
    elif selection == 'H':
        p = input("Enter the length of diagonal p:")
        q = input("Enter the length of diagonal q:")
        area = calculate_rhombus_area(float(p), float(q))
    else:
        print("Invalid choice. Please select S, R, C, or H.")
    return area

def get_shape_name(tag):
    shape = "Unknown"
    if tag == 'S':
        shape = "Square"
    elif tag == 'R':
        shape = "Rectangle"
    elif tag == 'C':
        shape = "Circle"
    elif tag == 'H':
        shape = "Rhombus"
    return shape

area = calculate_area(selection)
print(f"The area of the {get_shape_name(selection)} is {area}.")