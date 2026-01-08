primes = list()
#primes is now an empty list
# list() is a built-in function that creates a list
print(primes)

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#primes is now a list of the first ten prime numbers
#[2, 3, 5, 7, 11, 13, 17, 19, 23, 29] is a list literal that creates a list with the specified values

primes.append(2)
primes.append(3)
primes.append(5)
primes.append(7)
#append() is a list method that adds an element to the end of the list
#Here we are adding the first four prime numbers to the list


print(primes)

name = list()

name = ["sam", "cody", "dave", "tom"]
#in "sam" "" is used to denote that it is a string value
#if we do not use "" python will think we are referring to a variable named sam


print(name)



list  = ["Ram" , "CPU", "GPU", "SSD"]
#list is now a list with one string element

Hardware = list[2]
#Hardware is now assigned the value at index 2 of the list, which is "GPU"

#Hardware = list[5]
#This will cause an IndexError because there is no index 5 in the list

def is_valid_index(index: int, list) -> bool:
    #def is used to define a function
    # is_valid_index is the name of the function
    # index: int indicates that the parameter index is expected to be of type int
    # list is the second parameter of the function 
    # -> bool indicates that the function is expected to return a value of type bool which is either True or False

    result = False
    #result is initialized to False which means the index is not valid by default

    if 0 <= index and index < len(list):
        #if statement checks if the index is within the valid range of the list
        #<= is used to check if index is greater than or equal to 0
        #here index is a parameter passed to the function
        #and index < len(list) checks if index is less than the length of the list
        #if both conditions are true the index is valid
        #if index is not < 0 or index is not < len(list) the index is invalid
        result = True
        #result is set to True indicating the index is valid
        
    return result
    #return statement returns the value of result to the caller of the function
    #here it will return either True or False based on the validity of the index
    #if its true the index will print as valid otherwise it will print as not valid

index = 3
#here index is assigned the value 3 manually for testing purposes
#if we put 4 it will print as not valid because the list has only 4 elements which are 0,1,2,3
#it prints not valid because index 4 is out of range for the list
print(f"Index {index} is valid" if is_valid_index(index, list) else f"Index {index} is not valid")

#print statement uses an f-string to format the output
#{index} is a placeholder that will be replaced with the value of index
#is_valid_index(index, list) calls the function to check if the index is valid
#if the function returns True it will print "Index 3 is valid"
#else it will print "Index 3 is not valid"