# Write your solution here
while True:
    s = input("Please type in a string: ")
    if s != "":
        line = "-" * len(s)
        print(f"{s}\n{line}")
    else:
        break