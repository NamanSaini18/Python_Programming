#Program to print the factorial of a number:
a = int(input("Enter the number you want to check the factorial: "))
factorial = 1
if a<0:
    print("Factorial does not exist for a negative number, Please enter a +ve number")
elif a==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1, a+1):
        factorial = factorial*i
    print(factorial)
    
