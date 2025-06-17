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

#1. Equal to (>)
# The > operator checks if the left operand is greater than the right operand.
## If the condition is True, it returns True; otherwise, it returns False.
print("1.")
balance = 1000
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

print("2.")
      
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
print("3.")