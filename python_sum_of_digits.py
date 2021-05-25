a = int(input("Enter a number: "))
sum = 0
while a>0:
    b = a % 10
    sum = sum + b
    a = int(a/10)
# display the required sum 
print("The sum of all digits of the given number is: ", sum)
