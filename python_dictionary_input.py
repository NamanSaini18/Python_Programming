# taking input of the dictionary from the user
x = {}
print("How many elements are to be inserted: ")
n = int(input())
for i in range(n):
    print("Enter key: ")
    a = input()           # We can modify it in any method such as if there are multiple values of a key then we can take its values in the form of list or tuple.
    print("Enter the value: ")
    b = int(input())
    x.update({a:b})
print(x)
# The elements of dictionary are unordered, elements can be printed in any order.
