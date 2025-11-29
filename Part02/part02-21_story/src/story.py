# Write your solution here
# initialize variables
words = ""
old_word = ""

# beggin simple while loop
while True:
    # promt user for word
    word = input("Please types in a word")

    if old_word == word:
        break
    elif word == "end" or word == "End":
        break

    words += word + " "
    old_word = word

print(words)
