# Write your solution here

# input statements
word1 = input("Please type in the 1st word: ")
word2 = input("Please type in the 2nd word: ")

# conditon statements

if word1.lower() > word2.lower():
    print(f"{word1} comes alphabetically last.")
elif word2.lower() > word1.lower():
    print(f"{word2} comes alphabetically last.")
elif word1.lower() == word2.lower():
    print("You gave the same word twice.")