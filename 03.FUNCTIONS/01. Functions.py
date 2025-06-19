#funcions are reusable pieces of code that can be called with different arguments to perform a specific task.

print("Rectangle Area Calculator")

length = 5
#length is a variable that stores the length of the rectangle
width = 4 
#width is a variable that stores the width of the rectangle

area = length * width
#area is a variable that stores the area of the rectangle calculated by multiplying length and width
# * is the multiplication operator in Python
# The area of a rectangle is calculated as length multiplied by width

print(f"The area of the rectangle with lenght {length} and width {width} is {area}.")
# f-string is used to format the string with the values of length, width, and area
#{} is used to insert the value of a variable into a string
################################################################################################################################################################################################################################
#def is a keyword used to define a function in Python
#def function_name(parameters1, parameters2, .... parameters_n):
#function body 
  #return value
#put space after def and specify the function name 
#funtion name should be lowercase 
#use underscores to separate words 
#name should be descriptive 
#start function name with a verb like :
# 1. authenticate,
# 2. calculate,
# 3. get,
# 4. set,
# 5. update,
# 6. delete,
# 7. create,
# 8. find,
# 9. print,
# 10. show
################################################################################################################################################################################################################################
# Add a noun for clarity like:
# 1. authenticate_user,
# 2. calculate_area,
# 3. get_user_info,
# 4. set_user_password,
# 5. update_user_profile,
# 6. delete_user_account,
# 7. create_new_user,
# 8. find_user_by_id,
# 9. print_report,
# 10. show_user_details
################################################################################################################################################################################################################################
#the funtion name is followed by parentheses ()
#parameters are the inputs to the function, they are optional
#inside the parentheses, you can define parameters that the function will accept
#we can leave the parentheses empty if the function does not require any parameters
#if your paramenters are more than one, you can separate them with commas like : def calculate_area(length, width):
    #funtion body contains the code that will be executed when the function is called
    # a function can have multiple statements
    #if a function need to return a value, you can use the return statement

def calculate_square_area(side):
  #side is a parameter that represents the length of one side of the square
  
  return side * side

area = calculate_square_area(5)
#calling the function with an argument of 5
#5 is argument passed to the function

print(f"The area of the square is {area}.")