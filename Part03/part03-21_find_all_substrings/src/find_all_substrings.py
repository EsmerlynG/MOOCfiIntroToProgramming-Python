# Write your solution here
# prompt user for string and letter to be found
word = input("Please type in a word")
letter = input("Please type in a character: ")

# define variables
index = 0

# conditon statment printing only 3 character lengths
while True:
    index = word.find(letter)
    found = word[index: index+3]

    if len(found) == 3:
        print(found)

    word = word[index+1:]
    
    if word.find(letter) == -1:
        break

