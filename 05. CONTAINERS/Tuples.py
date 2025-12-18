chars = ("a", "b", "c")

even_nums = (2, 4, 6, 8)
print(even_nums)

voids = ()
#voids is an empty tuple
truths = (True,)
#truths is a single-element tuple containing the boolean value True

#truths.append(False)
#this will raise an AttributeError because tuples do not have an append() method

print(even_nums[2])
#even_nums[2] accesses the element at index 2 of the tuple, which is 6

print(even_nums[3])
#this will print 8, the element at index 3 of the tuple
#print(even_nums[6])
#this will raise an IndexError because index 6 is out of range for the tuple