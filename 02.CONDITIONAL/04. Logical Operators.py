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