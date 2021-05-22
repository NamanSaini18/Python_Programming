Take input of age of three people from user and determine oldest and youngest among them:
a = int(input("Enter the age of first person: "))
b = int(input("Enter the age of second person: "))
c = int(input("Enter the age of third person: "))
#checking oldest person
if a>b and a>c:
    print("a is the oldest person")
elif b>a and b>c:
    print("b is the oldest person")
elif c>a and c>b:
    print("c is the oldest person") 
#checking youngest person
if a<b and a<c:
  print("a is the youngest person")
elif b<a and b<c:
  print("b is the youngest person")
elif c<a and c<b:
  print("c is the youngest person")
