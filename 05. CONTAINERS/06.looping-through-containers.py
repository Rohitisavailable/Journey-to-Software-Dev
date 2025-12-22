primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
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

for number in primes:
    if number % 4 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")