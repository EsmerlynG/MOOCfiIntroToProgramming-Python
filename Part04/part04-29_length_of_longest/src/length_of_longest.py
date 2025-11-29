# Write your solution here
def length_of_longest(list):
    longest = 0
    for string in list:
        if len(string) > longest:
            longest = len(string)
    return longest


if __name__ == "__main__":
    list = ["first", "second", "fourth", "eleventh"]
    print(length_of_longest(list))
    list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(length_of_longest(list))