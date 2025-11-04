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
#\t is used for tab space
selection = input("""
---------------------------------------
\t'1' - BMW 
\t'2' - Ferrari
\t'3' - Lamborgini
---------------------------------------
""")

def select_color(selection):
    #unkown is used as a default value to avoid errors
    color = "Unknown"
    if selection == '1':
        color = input("Enter the color for your BMW:") #input function to take user input
    elif selection == '2':
        color = input("Enter the color for your Ferrari:")
    elif selection == '3':
        color = input("Enter the color for your Lamborgini:")
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
    return color

def get_car_name(tag): #def is used to define a function, get_car_name is the function name, tag is the parameter
    car = "Unknwn"
    if tag == '1':
        car = "BMW"
    elif tag == '2':
        car = "Ferrari"
    elif tag == '3':
        car = "Lamborgini"
    return car

print(f"Your {get_car_name(selection)} with color {select_color(selection)} will be delivered in 7-10 days.")
 #f-string is used to format the string with variables,get_car_name(selection) calls the function to get the car name based on user selection