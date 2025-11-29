# Write your solution here
# define mean function and take list as perameter
def mean(list):
    # find length of list
    length = len(list)
    # find sum of list
    list_sum = sum(list)
    # calculate meanby deviding sum / length
    mean = list_sum / length
    # return mean
    return mean

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = mean(my_list)
    print(f'mean value is {result}')