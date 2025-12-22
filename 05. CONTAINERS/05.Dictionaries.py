ssn_name_pairs = dict()
#dict() creates an empty dictionary
#dictionaries store data in key-value pairs
#ssn_name_pairs is the name of the dictionary
#here ssn_name_pairs will store social security numbers as keys and names as values

ssn_name_pairs["123-45-6789"] = "Alice Smith"
#this adds a key-value pair to the dictionary

ssn_name_pairs["987-65-4321"] = "Bob Johnson"
#adding another key-value pair

ssn_name_pairs["555-55-5555"] = "Charlie Brown"
#adding a third key-value pair

ssn_name_pairs = {
    "123-45-6789": "Alice Smith",
    "987-65-4321": "Bob Johnson",
    "555-55-5555": "Charlie Brown",
    "000-000-002": "Diana Prince"
}
#this is another way to create the same dictionary using a dictionary literal
#it initializes the dictionary with three key-value pairs
#dictionary literals are enclosed in curly braces {}

print(ssn_name_pairs)
#the output will show the entire dictionary with all key-value pairs
#output: {'123-45-6789': 'Alice Smith', '987-65-4321': 'Bob Johnson', '555-55-5555': 'Charlie Brown'}

print(ssn_name_pairs["987-65-4321"])
#this retrieves the value associated with the key "987-65-4321"
#output: Bob Johnson

print(ssn_name_pairs["555-55-5555"])
#this retrieves the value associated with the key "555-55-5555"
#output: Charlie Brown

# name = ssn_name_pairs["999-999-9999"]
#this line will raise a KeyError because "999-999-9999" is not a key in the dictionary
# it demonstrates that trying to access a non-existent key results in an error

#ssn_name_pairs["123-45-6789"] = "Alice Johnson"
#this updates the value for the existing key "123-45-6789"
#ssn_name_pairs["123-45-6787"] = "David Wilson"
#this adds a new key-value pair to the dictionary

#print(ssn_name_pairs["123-45-6789"])
#this retrieves the updated value associated with the key "123-45-6789"
#output: Alice Johnson
print(ssn_name_pairs)


#del dictionary[key]
#this deletes the key-value pair with the specified key from the dictionary
del ssn_name_pairs["987-65-4321"]
#deletes the key-value pair where the key is "987-65-4321"
#
print(ssn_name_pairs)
#this prints the dictionary after deleting the key-value pair with key "987-65-432
#output: {'123-45-6789': 'Alice Smith', '555-55-5555': 'Charlie Brown'}

#del ssn_name_pairs["121-131-3131"]
#this line will raise a KeyError because "121-131-3131" is not a key in the dictionary

print(ssn_name_pairs)


key = "000-000-002"
#key is a variable storing the key to be deleted
#"000-000-002" is a valid key in the dictionary
if key in ssn_name_pairs:
    #if the key exists in the dictionary(ssn_name_pairs)
    del ssn_name_pairs[key]
    #delete the key-value pair(ssn_name_pairs) with the specified key[key]
else:
    print(f"Key {key} not found in dictionary.")
    #else, print a message indicating the key was not found
print(ssn_name_pairs)

#this checks if the key exists in the dictionary before attempting to delete it

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#summary:
#Dictionaries store data in key-value pairs
#They are created using the dict() function or dictionary literals {}
#Key-value pairs are added using the syntax: dictionary_name[key] = value
#Values are accessed using their keys with the syntax:
# value = dictionary_name[key]


# to create a dictionary:
# dictionary_name = dict()
# or
# dictionary_name = {key1: value1, key2: value2, ...}


#to add key-value pairs:
# dictionary_name[key] = value


#to modify existing values:
# dictionary_name[key] = new_value


#to delete key-value pairs:
# del dictionary_name[key]


#example:
# name = ssn_name_pairs["123-45-6789"]
# name will be "Alice Smith"
#ssn_name_pairs is the dictionary name
#"123-45-6789" is the key used to access the corresponding value "Alice Smith"