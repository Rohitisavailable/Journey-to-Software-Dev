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

selection = input("""
---------------------
\t'S' - Square
\t'R' - Rectangle
\t'C' - Circle
---------------------

""")



#Function to calculate the area based on user selection
def calculate_area(selection):
    area = 0

    if selection == 'S':
        side = input("Enter the side:")
        area = calculate_square_area(float(side))
    #float() converts the input string to a float for calculation

    elif selection == 'R':
        length = input("Enter the length:")
        width = input("Enter the width:")
        area = calculate_rectangle_area(float(length), float(width))
    #float() is used to convert the input strings to floats for calculation
    
    elif selection == 'C':
        radius = input("Enter the radius:")
        area = calculate_circle_area(float(radius))
    else:
        print("Invalid choice. Please select S, R, or C.")
    return area
    return area

#Function to get the shape name based on the tag 
def get_shape_name(tag):
    shape = "Unknown"
    if tag == 'S':
        shape = "square"
    elif tag == 'R':
        shape = "rectangle"
    elif tag == 'C':
        shape = "circle"
    return shape
        





area = calculate_area(selection)
print(f"The area of the {get_shape_name(selection)} is {area}")
