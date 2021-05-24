# List input method from the user:
str = input("Enter the values seperated by commas: ").split(',') #The by-default value of split is space.
# since, we know that --> x,y = [datatype(variable)_For variable in input()]
tup = (eval(num) for num in str)  # we are using eval for taking input of a list from the user because list may contain different types of elements
lst = list(tup)
print(lst)
# Lists are mutable. (lists can be changed after declaration)


# Tuple input method from the user:
str = input("Enter the values seperated by commas: ").split(',')
lst = [int(num) for num in str.split()]
tup = tuple(lst)
print(tup)
# Tuples are immutable. (Tuples cannot be changed after declaration, Tuples are Read-only list)
