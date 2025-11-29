# Write your solution here

# promt user for name
name = input("Please type in your name: ")

# conditon statement
if name.lower() == "Huey".lower() or name.lower() == "Dewey".lower() or name.lower() == "Louie".lower():
    print("I think you might be one of Donald Duck's nephews.")
elif name.lower() == "Morty".lower() or name.lower() == "Ferdie".lower():
    print("I think you might be one of Mickey Mouse's nephews.")
else:
    print("You're not a nephew of any character I know of.")

