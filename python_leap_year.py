# python program to check if a year is a leap year or not
# Take input from the user of the year he/she want to check:
year = int(input("Enter the year you want to check: "))

# Leap Year Check
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a Leap Year")
# if year is divisible by 100, then it is not a leap year
elif year % 100 == 0:
    print(year, "is not a Leap Year")
# if year is divisible by 400 then it is a leap year else not
elif year % 400 == 0:
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")
