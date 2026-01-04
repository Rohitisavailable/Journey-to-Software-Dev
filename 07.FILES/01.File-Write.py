def write_file(file_path: str, text: str) -> int:
    #def function_name(parameters: type, parameters: type) -> return_type:
    #definition of a function that writes text to a file and returns the number of characters written
    file = None
    try:
        file = open(file_path, 'w')  # Open the file in write mode
        return file.write(text)          # Write the text to the file
    except OSError:
        print(f"Error! couldn't open the file: {file_path}")
    finally:
        if file != None:
            file.close()                # Ensure the file is closed

filename = "myfile.txt"
count = write_file(filename, "Hello, World!")

if count != None:
    print(f"{count} characters were written to {filename}")
