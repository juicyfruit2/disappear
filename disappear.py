# A program that strips a set of characters from a string.

# Created a variable for user to input a string 
user_input = input("Create a string:")

# created a variable for the user to input 
characters = input("Which characters would you like to make disapear?:")

# used the for loops and the .replace string method 
for str_char in characters:
    user_input = user_input.replace(str_char,"")

print(user_input)

#  used Discord L1T15 to give me an idea when i was stuck 









