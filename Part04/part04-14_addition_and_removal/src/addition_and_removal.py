# Write your solution here
list = []
count = 0

while True:
    print(f"The list is now {list}")
    choice = input("a(d)d, (r)emove or e(x)it: ")
    
    if choice.lower() == "d":
        count += 1
        list.append(count)

    elif choice.lower() == "r":
        count -= 1
        list.pop(len(list) - 1)
        
    elif choice.lower() == "x":
        break
print("Bye!")

