def select_car_bmw():
    return

def select_car_ferrari():
    
    return

def select_car_lamborgini():
    return


print("""
--------------
Select a Car
--------------
""")

selection = input("""
---------------------
\t'1' - BMW
\t'2' - Ferrari
\t'3' - Lamborgini
---------------------
""")

def select_color(selection):
    color = "Unknown"
    if selection == '1':
        color = input("Enter the color for your BMW:")
    elif selection == '2':
        color = input("Enter the color for your Ferrari:")
    elif selection == '3':
        color = input("Enter the color for your Lamborgini:")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
    return color

def get_car_name(tag):
    car = "Unknwn"
    if tag == '1':
        car = "BMW"
    elif tag == '2':
        car = "Ferrari"
    elif tag == '3':
        car = "Lamborgini"
    return car

print(f"Your {get_car_name(selection)} with color {select_color(selection)} will be delivered in 7-10 days.")