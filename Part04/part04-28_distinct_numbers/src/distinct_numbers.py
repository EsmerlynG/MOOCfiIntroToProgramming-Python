# Write your solution here
#defin function and pass list as parameter
def distinct_numbers(list):
    # sort the list to make it easier to track repeating numbers
    orderd_list = sorted(list)
    #track the last number added to the list
    last_num = 0
    #create empty new list to return
    new_list = []
    # for loop iterating through list
    for num in orderd_list:
        if last_num != num:
            new_list.append(num)

        last_num = num
    
    return new_list


if __name__ == "__main__":
    list = [3, 2, 2, 1, 3, 3, 1, 5, 23, 12, 18, 9, -1, -2, -500]
    print(distinct_numbers(list))