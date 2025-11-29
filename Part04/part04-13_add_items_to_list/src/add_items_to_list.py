# Write your solution here
# initialize list
items = []

# prompt user for number of items
number_of_items = int(input("How many items: "))

# add acumalator to count items added to list
count = 0
while count < number_of_items:
    items_to_list = int(input(f"Item {count + 1}: "))
    items.append(items_to_list)
    count += 1

print(items)
