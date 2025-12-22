primes = [2, 3, 4, 7, 11, 13, 18, 19, 22, 28]
#primes is a variable that holds a list of prime numbers




#to print all numbers:

#for number in primes:
    #for loop to iterate through each number in the primes list
#   print(number)
    #print the current number

#to print numbers from index:

#index = 0
#while index < len(primes):
 #   print(primes[index])
  #  index += 1

#to print odd or even numbers:
even_numbers = []
odd_numbers = []

for number in primes:
    if number % 2 == 0:
        #print(f"{number} is even.")
        even_numbers.append(number)    
    else:
        #print(f"{number} is odd.")
        odd_numbers.append(number)

print("Even numbers")
for i in even_numbers:
        print(i)

print("Odd numbers")
for i in odd_numbers:
        print(i)


ssn_name_pairs = {"123-456-789":"Ray apple",
                  "000-000-001":"blue sins",
                  "000-000-002":"black nigger",}

keys = ssn_name_pairs.keys()
#this returns all keys as set

values = ssn_name_pairs.values()

print("Dictionary keys")

for key in keys:
      print(key)

for value in values:
      print(value)