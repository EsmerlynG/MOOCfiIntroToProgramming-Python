# Write your solution here
# initialize list
list = []

# define accumalator to count words in list
count = 0

# begging simple while loop
while True:
    word = input("Word: ")

    if word in list:
        break

    list.append(word)
    count += 1

print(f"You typed in {count} different words")



