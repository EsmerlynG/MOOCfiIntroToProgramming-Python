# Write your solution here
def determain_longest_length(list):
    longest = 0
    for word in list:
        if len(word) > longest:
            longest = len(word)
    
    return longest


def all_the_longest(list):
    longest = determain_longest_length(list)

    new_list = []

    for string in list:
        if len(string) == longest:
            new_list.append(string)

    return new_list



if __name__ == "__main__":
    list = ["first", "second", "fourth", "eleventh"]
    print(all_the_longest(list))
   