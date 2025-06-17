#Comparision Operators are used to compare two values.
# They return a boolean value (True or False) based on the comparison.
# The most common comparision operators are:
# == (equal to)
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)
# These operators can be used in conditional statements to control the flow of the program.
## Example of Comparision Operators

#1. greater than (>)
# The > operator is used to compare two values.
# The > operator checks if the left operand is greater than the right operand.
## If the condition is True, it returns True; otherwise, it returns False.
print("1. greater than (>)")
balance = 100
money = 1000
if balance > money:
    #> is used to check if balance is greater than money
    balance -= money
    # If the balance > money, it deducts the amount of money from the balance.
    print(f"Current balance: {balance}")
    print("Transaction successful.")
else:
    #if the balance is not greater than money, it prints a message indicating insufficient balance.
    # It prints a message indicating insufficient balance.
    print("Insufficient balance for this transaction.")
    print(f"Current balance: {balance}")
#it prints "Insufficient balance for this transaction." and "Current balance: 1000" because 1000 is not greater than 1000.

print("2. Greater than (>=)")
      
#2.Greater than (>=)
# The >= operator checks if the left operand is greater than or equal to the right operand.
if balance >= money:
    #>= is used to check if balance is greater than or equal to money
    balance -= money
    # If the balance >= money, it deducts the amount of money from the balance.
    print(f"Current balance: {balance}")
    print("Transaction successful.")
else:
    #if the balance is not greater than or equal to money, it prints a message indicating insufficient balance.
    # It prints a message indicating insufficient balance.
    print("Insufficient balance for this transaction.")
    print(f"Current balance: {balance}")
#it prints "Current balance: 0" and "Transaction successful." because 1000 is greater than or equal to 1000.
print("3. less than (<)")

#3.less than (<)
# The < operator checks if the left operand is less than the right operand.
if balance < money:
    #< is used to check if balance is less than money
    balance -= money
    # If the balance < money, it deducts the amount of money from the balance.
    print(f"Current balance: {balance}")
    print("Transaction successful.")
else:
    #if the balance is not less than money, it prints a message indicating insufficient balance.
    # It prints a message indicating insufficient balance.
    print("Insufficient balance for this transaction.")
    print(f"Current balance: {balance}")
#it prints "Insufficient balance for this transaction." and "Current balance: 0" because 0 is not less than 1000.
print("4. Less than (<=)")
#4.Less than (<=)
# The <= operator checks if the left operand is less than or equal to the right operand.
if balance <= money:
    #<= is used to check if balance is less than or equal to money
    balance -= money
    # If the balance <= money, it deducts the amount of money from the balance.
    print(f"Current balance: {balance}")
    print("Transaction successful.")
else:
    #if the balance is not less than or equal to money, it prints a message indicating insufficient balance.
    # It prints a message indicating insufficient balance.
    print("Insufficient balance for this transaction.")
    print(f"Current balance: {balance}")
#it prints "Current balance: 0" and "Transaction successful." because 0 is less than or equal to 1000.
print("5. Equal to (==)")
#5.Equal to (==)
# The == operator checks if the left operand is equal to the right operand.
if balance == money:
    #== is used to check if balance is equal to money
    balance -= money
    # If the balance == money, it deducts the amount of money from the balance.
    print(f"Current balance: {balance}")
    print("Transaction successful.")
else:
    #if the balance is not equal to money, it prints a message indicating insufficient balance.
    # It prints a message indicating insufficient balance.
    print("Insufficient balance for this transaction.")
    print(f"Current balance: {balance}")
#it prints "Insufficient balance for this transaction." and "Current balance: 0" because 0 is not equal to 1000.
print("6. Not equal to (!=)")
#6.Not equal to (!=)
# The != operator checks if the left operand is not equal to the right operand.
if balance != money:
    #!= is used to check if balance is not equal to money
    balance -= money
    # If the balance != money, it deducts the amount of money from the balance.
    print(f"Current balance: {balance}")
    print("Transaction successful.")
else:
    #if the balance is equal to money, it prints a message indicating insufficient balance.
    # It prints a message indicating insufficient balance.
    print("Insufficient balance for this transaction.")
    print(f"Current balance: {balance}")
#it prints "Current balance: -1000" and "Transaction successful." because 0 is not equal to 1000.


#example 


number = 11

if number % 2 == 0:
    # % is a modulus operator that checks if the number is even.
    # If the number is even, it prints a message indicating that the number is even.
    # It prints a message indicating that the number is even.
    # modulus operator is a mathematical operator that returns the remainder of a division operation.

    print(f"{number} is even.")
if number > 10:
    print(f"{number} is greater than 10.")
if number == 12:
    print(f"{number} is equal to 12.")
# This code checks if the number is even, greater than 10, or equal to 12 and prints the corresponding messages.
# The output will be:
# 12 is even.
# 12 is greater than 10.
# 12 is equal to 12.