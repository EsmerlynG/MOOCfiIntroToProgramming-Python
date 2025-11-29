# Write your solution here
# prompt user for interger
number = int(input("Please type in a number: "))

# define variables
opp1 = 1
opp2 = 1
limit = number + 1
while opp1 < limit:
    print(f"{opp1} x {opp2} = {opp1*opp2}")
    if opp2 >= number :
        opp2 = 0
        opp1 += 1
    opp2 += 1

    
    
