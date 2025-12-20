def login(username: str, password: str) -> bool:
    is_aunthenticated = False
    
    if username == "admin" and password == "1234":
        is_aunthenticated = True
    
    return is_aunthenticated

user = input("Enter your username:")
passw = input("Enter your password:")


attempt = 1
max_attempt = 5
is_authenticated = False 

while login(user, passw) == False:
    attempt += 1
    # += is a shorthand for attempt = attempt + 1
    #that means we are incrementing the attempt by 1
    #incrementing means increasing the value of a variable by a certain amount
    if attempt > max_attempt: break
    #if attempt is greater than max_attempt, we break the loop
    #break is a keyword that is used to exit a loop 
    #break terminates the loop
    print("Login failed, check again")
    
    
    user = input("Enter your username:")
    passw = input("Enter your password:")
else:
    is_authenticated = True    
    print("Login successful")

if not is_authenticated:
    print("You have been blocked")



#summary:
#This code implements a simple login system with a maximum number of attempts
#The login function checks if the provided username and password are correct
#def is used to define a function in Python
# def function_name(parameters) -> return_type:
# is_authenticated variable tracks if the user has successfully logged in
#if username and password match, is_authenticated is set to True
#else, the user is prompted to try again until max attempts are reached
#while loop continues to prompt for login until successful or max attempts exceeded

#attempt variable counts the number of login attempts
#max_attempt variable sets the maximum allowed attempts
#is_authenticated variable indicates if the user is logged in

#while loop checks the login function
#while login(user, passw) == False:
#attempt += 1 is used to increment the attempt count
#+=1 is shorthand for incrementing by 1
#If login fails, attempt is incremented by 1
#If attempt is greater than max_attempt, the loop breaks
#and the user is blocked
#If login is successful, is_authenticated is set to True
#and a success message is printed
#If not authenticated after max attempts, a block message is printed