# Write your solution here
def palindromes(word: str):
    return word == word[::-1]

def main():
    
    while True:
        word = input("Please type in a palindrome: ")

        if palindromes(word) == True:
            print(f"{word} is a palindrome!")
            break

        print("that wasn't a palindrome")

main()


    



