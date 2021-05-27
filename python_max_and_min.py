#  Python program to print the maximum and minimum values of a tuple without using max and min functions 
t = tuple()
# Enter the total no of elements in the tuple
n = int(input("Total no of elements in the tuple are: "))
for i in range(n):
# Enter the elements of the tuple  
    a = input("Enter elements: ")
    t = t+(a,)
print("maximum value of the given tuple= ", max(t))
print("minimum value of the given tuple= ", min(t))
