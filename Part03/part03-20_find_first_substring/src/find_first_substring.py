# Write your solution here
# prompt user for a string
word = input("Please type in a word")
letter = input("Please type in a character: ")

# define variables
index = word.find(letter)
range = index + 3
found = word[index: range]

# conditon statment printing only 3 character lengths
if len(found) == 3:
    print(found)


    