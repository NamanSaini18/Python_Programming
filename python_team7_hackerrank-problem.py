# solution in python of Team 7 hackerrank problem
n = int(input())   # Constraints 1<=n<=1000  # n is the  no of problems the friends will implement in the contest
sum = 0
for i in range(0,n):
    """ sample input is
        3
        1 1 0
        1 1 1
        1 0 0 """
    x,y,z = map(int, input())
    if (x+y+z>=2):
        sum = sum + 1
print(sum)
#sample output is 2
