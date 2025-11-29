# Write your solution here
# prompt user for number

while True:
    number = int(input("Please type in a number: "))
    count = number
    if number <= 0:
        print("Thanks and bye!")
        break
    
    sum = 1
    while count > 0:
        sum *= count
        count -= 1
    
    print(f"The factorial of the number {number} is {sum}")
