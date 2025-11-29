# Write your solution here

# intialize variables
neg = 0
pos = 0 
count = 0
sum = 0

print("Please type in integer numbers. Type in 0 to finish.")

# beggin simple while loop
while True:
    num= int(input("Numbers: "))
    sum += num

    if num == 0:
        break

    if num > 0:
        pos += 1
    else:
        neg += 1

    
    count += 1

mean = sum / count
print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {sum}")
print(f"The mean of the numbers is {mean}")
print(f"Positive numbers {pos}")
print(f"Negative numbers {neg}")

