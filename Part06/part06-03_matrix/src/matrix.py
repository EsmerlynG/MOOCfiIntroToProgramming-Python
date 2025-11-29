# write your solution here
def matrix():
    matrix = []

    with open("src/matrix.txt") as m:
        for line in m:
            line = line.strip()
            row = list(map(int,line.split(",")))
            matrix.append(row)
             
    return matrix

def min_num():
    m = matrix()
    min_list = []
    for row in m:
        min_list.append(min(row))
    
    return min(min_list)


def matrix_sum():
    m = matrix()
    s = 0
    for row in m:
        s += sum(row)
    return s

def matrix_max():
    m = matrix()
    largest = min_num()

    for row in m:
        if largest < max(row):
            largest = max(row)
        
    return largest

def row_sums():
    m = matrix()
    sum_list = []

    for row in m:
        sum_list.append(sum(row))
    
    return sum_list

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
