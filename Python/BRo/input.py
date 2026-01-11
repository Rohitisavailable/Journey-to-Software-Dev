#input() = is a funtion used to prompt user to input data and return the entered data as a string

name = input("what is your name: ")
age = int(input(f"What is Your age {name}? "))
#we can also solve the issue by typecasting it in input function

# The age got saved as string and strings cannot be incremented so we need to convert it into integer first

#age = int(age)
age = age + 1


print(f"Hello {name}")

print(f"{name} is {age} years old")