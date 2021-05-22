#Printing simple half pyramid pattern using loops
#Firstly enter the no of rows for half pyramid pattern
rows = int(input("Enter the number of rows: "))
for i in range(0,rows):
#nested loops for each column  
    for j in range(i+1):
        print("*",end='')
    print("\r")
   
#Downward half pyramid of stars using loops
rows = int(input("Enter the number of rows: "))
for i in range(rows+1,0,-1):
    for j in range(0,i-1):
        print("*", end = ' ')
    print("\r")

  
