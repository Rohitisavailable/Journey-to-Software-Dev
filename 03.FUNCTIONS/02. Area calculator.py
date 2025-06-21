def calculate_square_area(side: float):
    return side * side
# Function to calculate the area of a square


def calculate_rectangle_area(length: float, width: float):
    return length * width
# Function to calculate the area of a rectangle

def calculate_circle_area(radius: float):
    pi = 3.14
    return pi * radius ** 2
# Function to calculate the area of a circle


print("""
--------------
Area Calculator
--------------
Select a shape
""")

selection = input("""\t'S' - Square
                  \t'R - Rectangle)
                  \t'C' - Circle
                  """)

area = 0

if selection ==  