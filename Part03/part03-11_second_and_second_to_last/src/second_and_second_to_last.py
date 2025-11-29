# Write your solution here
# prompt user for a string
s = input("Please type in a string: ")

if s[1] == s[-2]:
    print(f"The second and the second to last characters are {s[1]}")
else:
    print("The second and the second to last characters are different")