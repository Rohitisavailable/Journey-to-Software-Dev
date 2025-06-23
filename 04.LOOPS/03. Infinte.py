def login(username: str, password: str) -> bool:
    is_aunthenticated = False
    
    if username == "admin" and password == "1234":
        is_aunthenticated = True
    
    return is_aunthenticated

user = input("Enter your username:")
passw = input("Enter your password:")

while login(user, passw) == False:
    print("Login failed, check again")
    # If the login is unsuccessful, ask for username and password again
    
    user = input("Enter your username:")
    passw = input("Enter your password:")
    
print("Login successful")