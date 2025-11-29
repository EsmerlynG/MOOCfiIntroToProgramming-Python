# Write your solution here
# prompt user for word
word = input("Word: ")

# set variables
frame_width = 30

# calculations for madding
total_padding = frame_width - 2 - len(word)
left_paddig = total_padding // 2
right_padding = total_padding - left_paddig

# print frame with word
print(frame_width * "*")
print("*" + " " * left_paddig + word + " " * right_padding + "*")
print(frame_width * "*")