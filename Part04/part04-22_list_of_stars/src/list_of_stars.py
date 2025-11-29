# Write your solution here
# define print star row function
def list_of_stars(list):

    for num in list:
        print(num * "*")

if __name__ == "__main__":
    list = [3, 7, 1, 1, 2]
    list_of_stars(list)
