# Write your solution here
def no_vowels(string):
    vowls = ["a", "e", "i", "o", "u"]
    list = []
    new_string = ""
    for letter in string.lower():
        if letter not in vowls:
            list.append(letter)
    
    for non_vowl in list:
        new_string += non_vowl

    return new_string


if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))