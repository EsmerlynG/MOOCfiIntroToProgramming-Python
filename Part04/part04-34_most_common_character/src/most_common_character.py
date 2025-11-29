# Write your solution here
def most_common_character(string):
    highest_count = 0
    most_common = ""
    for i in string:
        count = string.count(i)
        
        if count > highest_count:
            highest_count = count
            most_common = i
    
    return most_common
    
if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))
    string2 = "exemplaryelementary"
    print(most_common_character(string2))