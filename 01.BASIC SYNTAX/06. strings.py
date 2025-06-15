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