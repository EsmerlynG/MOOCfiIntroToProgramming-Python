# Write your solution here
# prompt user for string
word = input("Please type is a string: ")

#assign variable
vowls = "aeo"
length_vowls = len(vowls)
index = 0

#simple while loop
while index < length_vowls:
    search = vowls[index]
    
    if search in word:
        print(f"{search} found")
    else:
        print(f"{search} not found")
    index += 1
   