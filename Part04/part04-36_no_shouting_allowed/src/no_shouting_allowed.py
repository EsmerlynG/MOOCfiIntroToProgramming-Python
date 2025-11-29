# Write your solution here
def no_shouting(list):
    new_list = []
    for word in list:
        if not word.isupper():
            new_list.append(word)

    return new_list
if __name__ == "__main__":
    my_list = ['FIRST', 'SECOND', 'third', 'fourth', 'fifth']
    pruned_list = no_shouting(my_list)
    print(pruned_list)