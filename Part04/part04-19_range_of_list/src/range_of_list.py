# Write your solution here
# define function and take list as a parameter
def range_of_list(list):
    #find largest number in list
    largest = max(list)
    #find smallest number in list
    smallest = min(list)
    #find diffrence of smallest and largest with subtraction
    diffrence = largest - smallest

    return diffrence
# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)