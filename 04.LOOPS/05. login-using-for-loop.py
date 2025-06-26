def login(username: str, password: str) -> bool:
    is_aunthenticated = False
    
    if username == "admin" and password == "1234":
        is_aunthenticated = True
    
    return is_aunthenticated

user = input("Enter your username:")
passw = input("Enter your password:")

is_authenticated = False 

for attempt in range(4):
    if login(user, passw) == True:
        is_authenticated = True
        print("Login successful")
        break
    else:
        print("Login failed, check again")
        user = input("Enter your username:")
        passw = input("Enter your password:")
    
print("login successful" if is_authenticated else "You have been blocked")