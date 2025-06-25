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
    if attempt > max_attempt: break
    #break terminates the loop
    print("Login failed, check again")
    
    
    user = input("Enter your username:")
    passw = input("Enter your password:")
else:
    is_authenticated = True    
    print("Login successful")

if not is_authenticated:
    print("You have been blocked")

