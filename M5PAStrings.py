# Aaron Mairel
# 10/22/2025
# CIS150AB 22096
# This program is going to preform 3 tasks which are formatting a float, advanced slicing, and splitting and joining strings,
# all based off of user inputted data.

# Task 1:
print("") # new line to separate task outputs
# Prompt the user for a float so we can perform our first task.

temp = float(input("Input the Air Temperature as a float"))
# Now, we print the required output
print(f"Task 1 Output: {temp:.1f}" + "F")

# Task 2:
print("") # new line to separate task outputs
# Prompt the user for four 8-letter words

word1 = input("Input an 8-letter word")
word2 = input("Input a second 8-letter word")
word3 = input("Input a third 8-letter word")
word4 = input("Input a fourth 8-letter word")

# Next, Slice the four strings.

print("Task 2 Output: " + word1[0:3] + word2[-4::] + word3[3:6] + word4[-3::])

# Task 3:
print("") # new line to separate task outputs
# Use the same four strings and join word 1 and 3, and join word 2 and 4.

# Combine the words into one string with the delimiter as "."
combined= ".".join([word1, word2, word3, word4])
# Then we need to split the string into a list.
word_list = combined.split(".")

# Now, we can join the words together
joined1 = "".join([word_list[0], word_list[2]])
joined2 = "".join([word_list[1], word_list[3]])

# After we have created the variables of the joined words, we can now output it.
print("Task 3 Output:")
print(joined1)
print(joined2)