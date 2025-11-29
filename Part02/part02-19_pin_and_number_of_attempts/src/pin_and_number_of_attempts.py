# Write your solution here
# set variables
pin = ("4321")
attempts = 0

# begging while loop
while True:
    code = input("Pin: ")
    attempts += 1

    if code != pin:
        print("Wrong")
    else:
        break

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")
