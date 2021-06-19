# File Handling basic question
import os,sys
fname = input("Enter the file name: ")    # Here we'll enter the file name which we wanna read
if os.path.isfile(fname):           # This is the syntax
    f = open(fname,'r')    # Here we are using r mode which is used to read a data from a file. The file pointer is pointed at the beginning of the file
else:
    print("File does not exist ")  # If the file entered by the user doesn't exist then this will be printed and program will be closed
    sys.exit()
str = f.read()
print(str)
f.close()    # mandatory step to close the file after performing a function,else the program will not run
