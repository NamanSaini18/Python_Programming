# Hackerrank solution of "Possibility Match of String " Contest Problem
lst=[]
lst1=[]
for i in range(int(input())):
    for j in range(2):
        lst.append(input())
    lst1.append(lst)
    lst=[]
a = 0
for i in range(len(lst1)):
    k=lst1[i][0].upper()
    j=lst1[i][1]
    for i in lst1[i][1]:
        if i in k:
            a += 1
        else:
            pass
    if a == len(j):
        print('YES')
    else:
        print('NO')
    a = 0
