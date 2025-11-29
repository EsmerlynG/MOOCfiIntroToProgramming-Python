# Write your solution here
# prompt user for string
word = input("Please type in a string: ")

# define variables
length_word = len(word)
index = length_word 
count = 0

# begin while loop
while count < length_word:
    index -= 1
    print(word[index:length_word])
    count += 1
    

    
    
