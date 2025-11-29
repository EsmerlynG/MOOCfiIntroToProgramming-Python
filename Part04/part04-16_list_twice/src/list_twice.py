# Write your solution here
list = []

while True:
    item = int(input("New item: "))
    if item == 0:
        break

    list.append(item)
    sorted_list = sorted(list)
    print(f'The list now: {list}')
    print(f'The list in order: {sorted_list}')

print("Bye!")