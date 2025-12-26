#z = 10 / 0
#  
# This will raise a ZeroDivisionError because division by zero is not allowed in mathematics.
#a zero division error occurs when you try to divide a number by zero.

#eg:
x = 10
for i in range(100):
    x-= 2
    print(1 / x)

#This will eventually raise a ZeroDivisionError when x becomes 0 during the loop.
#In this example, we start with x = 10 and decrement x by 2 in
#each iteration of the loop. When x reaches 0, the expression 1 / x will attempt to divide by zero, causing a ZeroDivisionError.