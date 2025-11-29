# Write your solution here
# prompt user for sentence
sentence = input("Please type in a sentence: ")
words = sentence.split()

count = 0
while len(words) > count:

    string = words[count]
    print(string[0])
    count += 1