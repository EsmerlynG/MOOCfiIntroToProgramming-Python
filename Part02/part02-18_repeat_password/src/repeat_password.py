# Write your solution here

# prompt user for a password
password = input("Password: ")

# begin simple while loop
while True:
    # prompt user to repeate password
    reapeat = input("Repeate password")

    # begin condition statements
    if password != reapeat:
        print("They do not match!")
    else:
        print("User account created!")
        break