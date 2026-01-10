part1 = "Stay hungry."
#part1 is a string variable
# "Stay hungry." is a string literal that contains the text to be printed
# part1 is a variable that stores the string "Stay hungry."
################################################################################################
part2 = "Stay foolish."
# part2 is a string variable
# "Stay foolish ." is a string literal that contains the text to be printed
# part2 is a variable that stores the string "Stay foolish."
################################################################################################

quote = part1 +" " + part2

#print(quote)
# The above line concatenates part1 and part2 with a space in between
################################################################################################
quote = f"{part1} {part2}"
# f-string is a way to format strings in Python
# It allows you to embed expressions inside string literals, using curly braces {}
# # The f-string is prefixed with the letter 'f'
# This allows you to include variables and expressions directly in the string'
print(quote)
################################################################################################

name = "Steve Jobs"
# name is a string variable that stores the name "Steve Jobs"

age = 56
# age is an integer variable that stores the age 56

work = "Apple Inc."
# work is a string variable that stores the name of the company "Apple Inc."
message = f"Your Name is {name} and your age is {age} and you work at {work}."
# message is a string variable that stores a formatted message
print(message)
################################################################################################

car = "Tesla"
# car is a string variable that stores the name of the car "Tesla"

model = "Model S"
# model is a string variable that stores the model of the car "Model S"

acceleration = 2.3
# acceleration is a float variable that stores the acceleration time 2.3 seconds

message = f"your {car} {model} can accelerate from 0 to 60 mph in {acceleration} seconds."
# message is a string variable that stores a formatted message about the car
print(message)
################################################################################################
pi = 3.14159
# pi is a float variable that stores the value of pi

message = f"The value of pi is approximately {pi:.5f}"
# message is a string variable that stores a formatted message about the value of pi
# The {:.5f} format specifier formats the float to 5 decimal places
#".0F" formats the float to 0 decimal places also display the float as a whole number
print(message)

print(len(message))
# The len() function returns the length of the string message
# In this case, it returns the number of characters in the message string
#len also includes spaces and punctuation in the count
####################################################################################################################################################################################################
message1 = "£▼€¥©©℉©⁂♪ª⁇¿"
# message1 is a string variable that stores a string with special characters and symbols
# The string contains various symbols including currency symbols, musical notes, and other special characters

print(f"The string {message1} has a length of {len(message1)} ")
## The len() function is used to find the length of the string message1
# It counts all characters, including special characters and symbols
####################################################################################################################################################################################################
message2 = " Stay hungry. Stay foolish. "
# message2 is a string variable that stores a quote with leading and trailing spaces
# The string contains the quote "Stay hungry. Stay foolish." with extra spaces at the beginning and end


uppercase_message = message2.upper()
# The upper() method is called on message2 to convert all characters to uppercase
# This method returns a new string with all characters in uppercase
# message2.upper() converts the string to uppercase
# uppercase_message is a new string variable that stores the uppercase version of message2

print(f" In Uppercase :  {uppercase_message }")
# The print() function is used to display the value of uppercase_message
#f"" is used to display the string with the variable value included
# The f-string allows you to embed the value of uppercase_message directly in the string
#f"" "

lowercase_message = message2.lower()
# The lower() method is called on message2 to convert all characters to lowercase
# This method returns a new string with all characters in lowercase
# message2.lower() converts the string to lowercase
# lowercase_message is a new string variable that stores the lowercase version of message2

print(f"In Lowercase : {lowercase_message } ")
# The lower() method is called on message2 to convert all characters to lowercase
#f"" is used to display the string with the variable value included

swappedcase_message = message2.swapcase()
# The swapcase() method is called on message2 to swap the case of all characters
# This method returns a new string with uppercase characters converted to lowercase and vice versa
## message2.swapcase() converts the string to swapped case
# swappedcase_message is a new string variable that stores the swapped case version of message2


print(f"In SwappedCase : { swappedcase_message } ")
# The swapcase() method is called on message2 to swap the case of all characters
#f string is used to display the string with the variable value included

stay_count = message2.count("Stay")
# The count() method is called on message2 to count the occurrences of the substring "Stay"
# This method returns the number of times "Stay" appears in the string


print(f"The word 'Stay' appears {stay_count} times in the message.")
#f"" is used to display the string with the variable value included


o_count = message2.count("o")
# The count() method is called on message2 to count the occurrences of the letter "o"
# This method returns the number of times "o" appears in the string
 

print(f"The letter 'o' appears {o_count} times in the message.")


print(f" standard message is :{message2}")
####################################################################################################################################################################################################