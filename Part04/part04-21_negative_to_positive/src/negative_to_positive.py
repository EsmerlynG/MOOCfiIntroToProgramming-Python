# Write your solution here
n = int(input("Please type in a positive integer: "))
pos_n = n + 1
neg_n = n * (-1)

for number in range(neg_n, pos_n):
    if number == 0:
        continue

    print(number)