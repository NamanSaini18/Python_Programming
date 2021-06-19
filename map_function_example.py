def square(x):
    return x*x
list1 = [5,7,9,11,13]
list1 = tuple(map(square,list1))
print(list1)
