#Typecasting = The process of converting a variable from one data type to another
# str(), int(), bool(), float()

name = "Dawg"
age = 25
gpa = 8.4
is_student = True


print(f"the name is a {type(name)}")
print(f"the age is a {type(age)}")
print(f"the gpa is a {type(gpa)}")
print(f"the is_student is a {type(is_student)}")
#Converting

gpa = int(gpa)

print(gpa)
#it converts 8.4 into a whole i.e 8

age2 = float(age)
print(age2)
#it converted age i.e 25 and added it a decimal making it 25.0

age1 = str(age)

print(age1)
#it will convert it into string not in integer
print(type(age1))

age3 = str(age)

age3 += "1"
print(age3)
#THIS WILL ADD 1 AT THE END MAKING 25 INTO 251


name = bool(name)

print(name)
#it will print true, if the string was empty it will print false