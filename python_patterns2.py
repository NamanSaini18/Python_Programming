def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*", end = " ")
        print("\r")
m = int(input("Enter the no of lines of the pattern u want to print: "))
pattern(m)
