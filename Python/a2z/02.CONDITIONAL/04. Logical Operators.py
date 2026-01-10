#logical operators contain 'and', 'or', and 'not'.
# Logical operators are used to combine conditional statements.
## 'and' returns True if both statements are true
# 'or' returns True if one of the statements is true
# 'not' returns True if the statement is false

#AND operator takes two values and returns True if both are True
#otherwise it returns False
#expression1 and expression2
####################################################################################################
#example:
#1. AND operator
success = True
result_code = 200

if success == True and result_code == 200:
    #and is used to check if both conditions are True
    print("Success: Operation completed successfully.")
else:
    print("Error: Operation failed.")
#############################################################################################
#2. OR operator
#OR operator uses two values and returns True if at least one of them is True
#otherwise it returns False

first_name = "Ellen"
last_name  = "Smith"

if first_name == "Ellen" or last_name == "Smith":
    #or is used to check if at least one condition is True
    print(f"Welcome, {first_name } {last_name}!")
else:
    print("Access denied. You are not Ellen or Smith.") 
    
#############################################################################################
#second example of OR operator
first_name = "John"
last_name  = "Doe"

if len(first_name) == 0 or len(last_name) == 0:
    #len is used to check if first_name equals 0 resulting in False
    #last_name equals 0 resulting in False
    #if either first_name or last_name is empty, the condition is True
    #or is used to check if at least one condition is True
    #we have first_name and last_name as false ---->false which evaluates to false
    print("Please provide your name.")
else:
    print(f"Hello, {first_name} {last_name}!")
#############################################################################################
#3. NOT operator
#NOT operator takes one value and returns True if the value is False
#otherwise it returns False

admin_user = True

if not admin_user:
    #not is used to check if admin_user is False
    print("Access denied. You are not an admin user.")
else:
    print("Welcome, admin user!")