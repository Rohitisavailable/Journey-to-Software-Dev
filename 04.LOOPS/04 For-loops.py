for index in range(10):
    #print("Called from within a for-in loop")
    print(f"{index} - iteration count {index +1}")

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