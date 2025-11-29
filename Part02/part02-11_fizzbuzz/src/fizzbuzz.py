# Write your solution here

# pompt user for number
num = int(input("Number: "))

# conditon statements
if num % 3 == 0 and num % 5 != 0:
    print("Fizz")
elif num % 5 == 0 and num % 3 != 0:
    print("Buzz")
else:
    print("FizzBuzz")