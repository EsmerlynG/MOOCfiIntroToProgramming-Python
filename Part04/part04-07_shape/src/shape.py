# Copy here code of line function from previous exercise and use it in your solution
def line(size, tree_character):
    print(tree_character * size)

def triangle(size, tree_character):
    # You should call function line here with proper parameters
    i = 1
    while i <= size:
        line(i, tree_character)
        i += 1

def stump(size, height, stump_character):
    i = 0
    while i < height:
        if height == 0:
            break
        print(stump_character * size)
        i += 1

def shape(size, tree_character, height, stump_character):
    triangle(size, tree_character)
    stump(size, height, stump_character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 5, "o")