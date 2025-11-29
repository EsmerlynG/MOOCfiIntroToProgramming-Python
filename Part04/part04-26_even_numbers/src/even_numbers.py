# Write your solution here
def even_numbers(list):
    new_list = []
    for num in list:
        if num % 2 == 0:
            new_list.append(num)
    
    return new_list

if __name__ == "__main__":
    list = [1,2,3,4,5]
    new_list = even_numbers(list)
    print(f"original {list}")
    print(f"new {new_list}")