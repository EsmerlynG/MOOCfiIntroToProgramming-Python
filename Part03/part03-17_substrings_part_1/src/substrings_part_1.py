# Write your solution here
# prompt user for string
word = input("Please type in a string: ")

# define variables
index_length = len(word) + 1
index = 1

# begin while loop
while index_length > index:
    
    print(word[0:index])
    index += 1