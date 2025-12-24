ssn_name_pairs = {"123-456-789":"Ray apple",
                  "000-000-001":"blue sins",
                  "000-000-002":"black",
                  "000-000-003":"Ray apple",
                  "000-000-004":"blue sins",
                  "000-000-005":"Ray apple",}

# Function to find duplicate names and their associated SSNs
#here ssn_name_dictionary is a dict type parameter 

def find_duplicate_name(ssn_name_dictionary: dict)-> dict:
#def function_name(parameter_name: parameter_type) -> return_type:    
#find_duplicate_name is the function name with one parameter ssn_name_dictionary having dict type which returns a dict type value
    
    result = {}
    
    #result is an empty dictionary which will store the final output
    
    names = list(ssn_name_dictionary.values())
    
    #names is a list containing all the names from the input dictionary which is obtained using the values() method

    for (ssn, name) in ssn_name_dictionary.items():
        
        #.items() method returns key-value pairs from the input dictionary
        
        if names.count(name) > 1:
            
            #.count() method counts how many times a name appears in the names list
            #here if a name appears more than once, it indicates a duplicate
            result[name] = result.get(name, [])

            #result[name] creates a new entry in the result dictionary for the duplicate name
            #result.get(name, []) retrieves the current list of SSNs for that name from the result dictionary
            
            result[name].append(ssn)
            
            #.append(ssn) adds the current SSN to the list of SSNs for that name in the result dictionary

    return result
    #return the result dictionary containing duplicate names and their associated SSNs

duplicate_name_ssns = find_duplicate_name(ssn_name_pairs)

#duplicate_name_ssns is a variable that stores the output of the find_duplicate_name function when called with ssn_name_pairs as the argument

for (name, ssns) in duplicate_name_ssns.items():
    #for name, ssns in duplicate_name_ssns.items(): iterates through each key-value pair in the duplicate_name_ssns dictionary
    #.items() method returns key-value pairs from the dictionary
    print(f"Found duplicates name {name} wiith SSNs: {ssns} ")