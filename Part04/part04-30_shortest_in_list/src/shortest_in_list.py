# Write your solution here
def shortest(list):
    shortest = ""
    length = 100

    for string in list:
        if len(string) <= length:
            length = len(string)
            shortest = string
    return shortest

if __name__ == "__main__":
    list = ["first", "second", "fourth", "eleventh"]
    print(shortest(list))
    list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    print(shortest(list))