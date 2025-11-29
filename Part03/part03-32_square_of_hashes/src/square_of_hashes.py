# Write your solution here
# You can test your function by calling it within the following block
def hash_square(length):
    height = length
    while 0 < height:
        print("#" * length)
        height -= 1

if __name__ == "__main__":
    hash_square(5)