
# Write your solution here
# initialize variable
limit = int(input("Limit: "))
num = 1
sum = 0
string = ""


while sum < limit:
    sum += num
    if num == 1:
        string = f"{num}"
    elif num > 1:
        string += f" + {num}" 
    num += 1

print(f"The consecutive sum: {string} = {sum}")