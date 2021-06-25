fname = input("Enter the file name: ")
l = input("Enter the letter to be searched: ")
count = 0
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter == l):
                    count += 1
print("Occurrences of the given letter is: ")
print(count)
