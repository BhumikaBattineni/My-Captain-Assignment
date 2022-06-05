#Taking the input of the filename from the user
File_name=input("Enter the filename: ")
fe=File_name.split(".")

#Display
print("Extension of the file is " + fe[-1])
