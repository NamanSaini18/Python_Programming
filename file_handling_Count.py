f = open("12345.txt",'r')   # Here you have to enter the file name in which you want to check the occurence of a character
text = f.read()
char = input("Enter the character you want to check in the file: ")   # Enter the character whose occurence you have to find
count = 0
for i in text:
    for c in i:
        if c == char:
            count += 1
print("The character {} is found {} times in the text file".format(char,count))
