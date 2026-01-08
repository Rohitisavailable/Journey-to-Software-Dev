def solve_eqn(a: float, b : float, c:float) -> float:
    try:

#def funtion_name(parm1: type, parm2: type, param3: type) -> return_type:

        return(float(c) - float(b)) / float(a)

    #return to c - b divided by a
    #x = (c - b) / a

    except ZeroDivisionError:
        #we used ZeroDivisionError to handle division by zero error
        #we used ValueError to handle invalid input error
        print("error 'a' cant be zero enter valid")
    except ValueError:
        print("error enter numeric value")


    finally:
       
        #finally block will always execute regardless of whether an exception occurred or not
       #it will execute after try and except blocks
        print("Leaving solve_eqn function")
print("ax + b = c linear eqn")


#we used ax for coefficient of x
#example: 2x + 3 = 7
#x = (c - b) / a

a = input("Enter a: ")
if float(a) == 0:
    raise ValueError("a cant be zero")

b = input("Enter b: ")
c = input("Enter c: ")

try:
    x = solve_eqn(a, b, c)
#x is assigned the return value of solve_eqn function

except Exception:
    #except block to catch any other exceptions that may occur
    print("Something bad happened")
else:
    print(f"X is {x} ")

#summary:
#error handling is a way to manage and respond to errors that may occur during the execution of a program.
#there are different types of errors like syntax errors, runtime errors, logical errors etc.


