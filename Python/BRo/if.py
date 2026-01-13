# if = Do some code only if some condition is true, else do nothing

age = int(input("Enter Your Age: "))

if age == 18:
    print(f"You can enter")
elif age < 0:
    print("You haven't been born")
else:
    print("You cannot enter")