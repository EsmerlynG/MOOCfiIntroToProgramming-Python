# Write your solution here

#prompt user for grade
grade = int(input("How many point [0-100]: "))

if grade < 0:
    print("Grade: impossible!")
elif grade <= 49:
    print("Grade: fail")
elif grade <= 59:
    print("Grade: 1")
elif grade <= 69:
    print("Grade: 2")
elif grade <= 79:
    print("Grade: 3")
elif grade <= 89:
    print("Grade: 4")
elif grade <= 100:
    print("Grade: 5")
else:
    print("Grade: impossible!")