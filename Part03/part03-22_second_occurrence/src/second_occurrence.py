# Write your solution here
# prompt user for string and substring
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

# define variables
index1 = string.find(substring)
index2 = -1

# condition statments
if index1 != -1:
    string = string[index1+len(substring):]
    index2 = string.find(substring)

# calculate second substring index location
index = index1+len(substring)+index2

# condition statment printing outputs
if index2 == -1:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {index}.")
