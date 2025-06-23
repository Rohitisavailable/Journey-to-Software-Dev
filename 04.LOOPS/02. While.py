#while expression:
    #Code block that runs if expression is true
#else:
    # If expression is flase,
    # run this codeand terminate loop
    
# while loop test a condition expression and runs the body of the loop while the condition remains true.
    

# Example of a while loop
# while login_not_successful:
    #ask for username and password
    
#example of a while loop with a condition

def login(username: str, password: str) -> bool:
    is_aunthenticated = False
    
    if username == "admin" and password == "1234":
        is_aunthenticated = True
    
    return is_aunthenticated
#login function checks if the username and password match the hardcoded values.
#it contains username and password as parameters.
#username has str which is string type and password has str which is string type.
#it return to boolean value which is True or False.

user = input("Enter your username:")
passw = input("Enter your password:")

while login(user, passw) == False:
    print("Login failed, check again")
    # If the login is unsuccessful, ask for username and password again
    user = input("Enter your username:")
    passw = input("Enter your password:")
    
print("Login successful")
# If the login is successful, print a success message

#while is used to repeatedly aske for login credentials until user provides with proper info 