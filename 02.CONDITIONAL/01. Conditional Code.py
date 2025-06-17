#if (condition) :
    # Code to run when condition is True
#else : 
    # Code to run when condition is False
    
    
    
# Example of a conditional statement
#######################################################################################################################################################################################################
balance = 10
#balance is a variable that holds the current amount of money in an account.
# It is set to 1000, meaning the account has 1000 units of currency available.
money = 100
#money is a variable that holds the amount of money to be withdrawn or used in a transaction.
# It is set to 100, meaning the user wants to withdraw or use 100 units of currency.
#######################################################################################################################################################################################################
if balance > money:
# The condition checks if the current balance is greater than the amount of money to be withdrawn.
    balance -= money
    # If the condition is True, it deducts the amount of money from the balance.
    #-= is a shorthand operator that subtracts the value of money from balance and assigns the result back to balance.
    print(f"Current balance: {balance}")
    print("Transaction successful.")
else:
    # If the condition is False, it means there is not enough balance for the transaction.
    # It prints a message indicating insufficient balance.
    print("Insufficient balance for this transaction.")
    print(f"Current balance: {balance}")
#######################################################################################################################################################################################################

