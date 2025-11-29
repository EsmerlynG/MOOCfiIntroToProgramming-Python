from math import sqrt
# Write your solution here

# begins simple while loop
while True:
    num = float(input("Please type in a number: "))

    if num < 0:
        print("Invalid number")
    elif num == 0:
        print("Exiting...")
        break
    else:
        print(sqrt(num))
    