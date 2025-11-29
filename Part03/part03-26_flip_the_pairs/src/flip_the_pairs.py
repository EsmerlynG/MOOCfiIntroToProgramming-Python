# Write your solution here
# prompt user for input
number = int(input("Please type in a number: "))
count = 1

while number >= count:

    if count % 2 == 0:
        print(count)
        print(count - 1)
    elif count % 2 != 0 and count == number:
        print(number)


    count += 1
    
    
    
    









    
