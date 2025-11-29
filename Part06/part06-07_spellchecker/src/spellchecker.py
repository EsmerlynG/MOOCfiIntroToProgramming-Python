# write your solution here
def word_list():
    words_list = []
    with open("wordlist.txt") as wl:
        
        for line in wl:
            words_list.append(line.strip())
    
    return words_list


def main():
    words = word_list()

    # ask user for a string
    text = input("Write text: ").split()
    
    """
       Here I will go through the sentence find the incorect words, highlight them with ** if incorrect
       then at the same time reform the sentence using my setence variable
    """

    for i in text:       
        if i.lower() not in words:
            print("*" + i + "* ", end="")
        else:
            print(i + " ", end="") 
        
main()
