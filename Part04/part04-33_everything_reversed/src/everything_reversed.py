# Write your solution here
# function to reverse lists
def everything_reversed(list):
    #create a new list to hold the reversed string in reverse order
    new_list = []
    # for loop to iterate through the reversed list
    for word in list[::-1]:
        # take the strings in the list reverse them and place them into the new list
        new_list.append(word[::-1])
    # return the new list with the reversed strings in the reverse order
    return new_list

if __name__ == "__main__":
    list = ["Hi", "there", "example", "one more"]
    print(everything_reversed(list))