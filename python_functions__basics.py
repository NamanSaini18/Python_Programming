# Simple Function program of type - Argument with return type : Whether to check a number is positive, negative or zero
def sum(n):
    if n>0:
        return 1
    if n<0:
        return -1
    if n==0:
        return 0
m = int(input("Please input the number you want to check: "))
n = sum(m)
if n == 1:
    print("Given number is positive")
elif n == 0:
    print("Given number is zero")
else:
    print("Given number is negative")
