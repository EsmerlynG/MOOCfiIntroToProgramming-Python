# Write your solution here
def formatted(list):
    new_list = []

    for num in list:
        formated_num = f"{num:.2f}"
        new_list.append(formated_num)
    return new_list

if __name__ == "__main__":
    list = [1.234, 0.3333, 0.11111, 3.446]
    print(formatted(list))
