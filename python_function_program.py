# Question is 1/1! + 2^2/2! + 3^3/3! + 4^4/4! + ..................................... + n^n/n!
# We have to write the code for above question using functions 
def factorial(n):
    f = 1 
    if (n == 0 or n == 1):
        return 1
    else:
        for i in range(1,n+1):
            f = f*i
    return f
n = int(input())
s = 0
for i in range(1, n+1):
    s = s + (float(i**i)/factorial(i))
print(s)
