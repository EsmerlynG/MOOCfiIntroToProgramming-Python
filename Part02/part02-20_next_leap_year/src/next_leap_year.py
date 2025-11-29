# Write your solution here
# Prompt user for a year
year = int(input("Year: "))

# assigning inputed year to ne variable so it can be altered
loop_year = year

# beggin simple while loop
while True:
    # increase year plus 1 in order to find next leap year after given ammount
    # we are not checking if the inputted year itself is a leap year only when
    # the next leap year is.
    loop_year += 1
    # conditional statement checking if year is a leap year
    if loop_year % 4 == 0 and loop_year % 100 != 0:
        # response printend if condition is meet
        print(f"The next leap year after {year} is {loop_year}")
        # ends while loop if condition is meet
        break
    
    # checkes if year given is a leap year
    elif loop_year % 100 == 0:
        # checkes if year given is a leap year
        if loop_year % 400 == 0:
            # response printed if conditon is meet
            print(f"The next leap year after {year} is {loop_year}")
            # end loop if condition is meet
            break
        
