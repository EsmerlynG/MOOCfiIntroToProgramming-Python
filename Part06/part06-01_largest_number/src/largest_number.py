# write your solution here
def largest():
    with open("src/numbers.txt") as num_file:
        largest_num = 0
        for num in num_file:
            num_int = int(num)
            if num_int > largest_num:
                largest_num = num_int
    return largest_num

if __name__ == "__main__":
    print(largest())
