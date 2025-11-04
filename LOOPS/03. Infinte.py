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

