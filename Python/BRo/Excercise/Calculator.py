response = input("Select the operation (+ - * /):")

num1 = float(input("Enter value of A: "))
num2 = float(input("Enter value of B: "))

if response == "+" :
    result = num1 + num2
    print(f"The Answer is: {result} ")
elif response == "-":
    result = num1 - num2
    print(f"The Answer is: {result} ")
elif response == "*":
    result = num1 * num2
    print(f"The Answer is: {result} ")

elif response == "/":
    result = num1 / num2
    print(f"The Answer is: {result} ")
else:
    print("Error")
