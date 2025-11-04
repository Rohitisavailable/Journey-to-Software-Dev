for index in range(10):
    #print("Called from within a for-in loop")
    if index == 5: break
    #break statement is used to exit the loop when index is equal to 5
    #it will stop the loop when index is equal to 5
    # This will stop the loop when index is equal to 5
    print(f"{index} - iteration count {index +1}")

print("-------------------------------------------------------------------------")

for index in range(10):
    #print("Called from within a for-in loop")
    if index % 2 == 0: continue
    #continue statement is used to skip the number which is divisible by 2
    #% is used to divide the number by 2 and check the remainder
    #if the remainder is 0, it means the number is even
    #it will skip the even numbers and only print the odd numbers
    # This will skip the even numbers and only print the odd numbers
    print(f"{index} - iteration count no: {index +1}")
    #{index} is used to print the index of the loop
    #index is the variable that holds the current iteration count
    #{index +1} is used to print the iteration count starting from 1

    




#break exits the loop immediately
#while continue shortcuts the current iteration and continues with the next one
print("-------------------------------------------------------------------------")

for print_numbers in range(5):
    
    if print_numbers < 5:
        print(f"{print_numbers}")


print("-------------------------------------------------------------------------")

#The following program aims to print numbers 1 to 10 but skips 5 and stops after 7. However, there's an issue in the loop control statements that causes it not to work as expected. Can you find the problem and correct it?
for i in range(1, 11):
    if i == 5: break
    elif i > 7: continue
    print(i)









# for-in loop is used to iterate over a sequence (list, tuple, string, etc.)
# range(10) generates a sequence of numbers from 0 to 9
#it is used to generate a sequence of numbers
#the range function is used to generate a sequence of numbers
#range function takes 3 parameters: start, stop, step
#start is the first number in the sequence, stop is the last number in the sequence,
#and step is the increment between each number in the sequence
#if step is not provided, it defaults to 1
#for example range(1,5,2) the squence starts at 1 and step is 2, so the sequence will be 1, 3
# after reaching 5, the loop will stop

#range(start, stop, step)

print("_____________________________________________________________________________________________________________________________________________")

for i in range(1, 11):
    if i == 5:
        continue 
    elif i > 7:
        break
    print(i)
