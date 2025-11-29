# Write your solution here
# prompt user for input
number = int(input("Please type in a number: "))

# define variables
count = 1

# begin while loop
while count < number:
    print(count)
    print(number)
    
    count += 1
    number -= 1

# print final number
if count == number:
    print(count)