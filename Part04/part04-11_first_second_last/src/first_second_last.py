# Write your solution here
def first_word(sentence):
    i = 0
    word = ""

    while i < len(sentence):
        if sentence[i] == " ":
            break
        word += sentence[i % len(sentence)]
        i += 1
    return word

def second_word(sentence):
    i = 0
    word = ""
    count = 0
    sentence = sentence + " "

    while i < len(sentence):
        if sentence[i] == " ":
            count += 1

            if count == 2:
                return (word)

            word = ""
            i += 1
        
        word += sentence[i % len(sentence)]
        i += 1

def last_word(sentence):
    i = 0 
    word = ""
    while i <= len(sentence):
        if i == len(sentence):
            return word

        if sentence[i] == " ":
            word = ""
            i += 1
        
        word += sentence[i % len(sentence)]
        i += 1



# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))