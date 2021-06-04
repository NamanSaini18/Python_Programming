def Fibonacci(n):  
   if n <= 1:  
       return n  
   else:  
       return(Fibonacci(n-1) + Fibonacci(n-2))  # --> This is the mathematical expression of Fibonacci sequence
# take input from the user
a = int(input("How many terms you want to print? "))  
if a <= 0:   # Validating the number of terms input by the user
   print("Invalid input, Please enter a positive integer")  
else:  
   print("Fibonacci sequence: ")  
   for i in range(a):  
       print(Fibonacci(i))
