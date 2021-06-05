# conversion of time : Hours into minutes where input is given by the user using FUNCTIONS
def time_conversion(hrs,min):
    min = hrs*60 + min
    return min
a = int(input("Enter the hours: "))
b = int(input("Enter the minutes: "))
b = time_conversion(a,b)
print("Total minutes = ",b)
