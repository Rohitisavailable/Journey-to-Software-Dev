
#       | 0  1  2  3  4    5   6
primes =[2, 3, 5, 7, 79, 465,31]
#primes is now a list of the first ten prime numbers
#it contains some non-prime numbers for demonstration purposes
print(primes)
#first we print the original list


primes[1] = 17
#primes[1] accesses the element at index 1 of the list, which is 3
#we then assign the value 17 to that index, replacing 3 with 17
#primes[1] = 17 modifies the list by changing the second element to 17
print(primes)
#we print the modified list to see the change

    #primes[8] = 11
    #primes[8] accesses the element at index 8 of the list, which is 465
    #print(primes)
    #we get an IndexError because index 8 is out of range for the list

primes.append(13)
#append() is a list method that adds an element to the end of the list
#append means to add something to the end of a list

print(primes)


list =[]
#list is now an empty list
# list() is a built-in function that creates a list


list.append("apple")
#list is now a list with one string element "apple"
list.append("banana")
#list is now a list with two string elements "apple" and "banana"
list.append("cherry")
#list is now a list with three string elements "apple", "banana", and "cherry"
list.append("date")
#list is now a list with four string elements "apple", "banana", "cherry", and "date"
print(list)
print(len(list))
print(list[2])
#list[2] accesses the element at index 2 of the list, which is "cherry"
#so it will print only "cherry"


character = []


character.append("a")
print(len(character))
#len() is used to get the length of the list
#here it will print 1 because there is one element in the list

print(f" the length of the char is : {len(character)}")
#f"" is used for formatted string literals
#it allows us to embed expressions inside string literals using {}
#{} is used to evaluate the expression inside it and include the result in the string



list.insert(2, 19)
#insert() is a list method that adds an element at a specific index in the list
#list.insert(2, 19) adds the value 19 at index 2 of the list
#this shifts the elements at index 2 and beyond to the right by one position

print(list)

print("we can see that 19 has been added at 3rd position/ index 2")

#19 will be added at index 2
#the list will now be ["apple", "banana", 19, "cherry", "date"]
# it adds 19 at second position, but since the list has only one element,
# it will add 19 at the end of the list


list.insert(3, "z")
#list.insert(3, "z") adds the string "z" at index 3 of the list
#this shifts the elements at index 3 and beyond to the right by one position

print(list)
#the list will now be ["apple", "banana", 19, "z", "cherry", "date"]
n = list.pop(2)

#pop() is a list method that removes and returns the element at a specific index in the list
#list.pop(2) removes the element at index 2 of the list and returns it
#the removed element is stored in the variable n


integers =[2, 3, 5, 7, 79, 465,31]

print(integers)

n = integers.pop()
#list.pop(4) removes the element at index 4 of the list, which is 79
#the removed element 79 is stored in the variable n
print(integers)
print(f"the removed element is : {n} ,the new list is {integers}")

integers.remove(7)
#remove() is a list method that removes the first occurrence of a specified value from the list
#integers.remove(7) removes the first occurrence of the value 7 from the list
print(integers)
#the list will now be [2, 3, 5, 79, 465, 31]
#the number 7 has been removed from the list which was at index 3