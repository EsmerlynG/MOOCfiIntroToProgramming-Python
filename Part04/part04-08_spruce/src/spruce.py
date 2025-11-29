# Write your solution here
# Build tree top
def line(i, size):
    space = (size - i) * " "
    star_count = 2 * i - 1
    print(space + "*" * star_count)

# Build stump
def stump(size):
    spaces = (size - 1) * " "
    print(spaces + "*")

# Build tree
def spruce(size):
    print("a spruce!")
    i = 1
    while i <= size:
        line(i, size)
        i += 1
    stump(size)
    

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(4)