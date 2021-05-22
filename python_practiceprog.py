# A student will not be allowed to sit in exam if his/her attendance is less than 75%
# Get total classes held in school
totalClassesHeld = int(input("Enter total number of classes held in the school : "))

# Get total classes attended by the student
totalClassesAttended = int(input("Enter total number of classes attended by the student : "))

# Get percent of the attendance
percent = (totalClassesAttended / totalClassesHeld) * 100

# Check if percent is above 75 i.e., eligible to sit in exam or not
if percent < 75:
    print("You cannot sit in the exams as your attendance is too low!, Better Luck Next time!")
else:
    print("You are eligible to sit in the exams as your attendance is fine.")
