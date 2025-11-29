# Write your solution here
def list_sum(a,b):
    i = 0
    new_list = []

    for num in a:
        sum = a[i] + b[i]
        new_list.append(sum)
        i += 1

    return new_list

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    
    print(list_sum(a,b))
