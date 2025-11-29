# Write your solution here
# prompt user for string
s = input("Please type a string: ")
neg_i = -1
pos_i = 0


# begin while loop
while len(s) > pos_i:
    print(f"{s[neg_i]}")
    neg_i -= 1
    pos_i += 1