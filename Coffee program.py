# Creating a coffee program that a user will be able to interact with.
# Sam Francis-Stead
# 23 Sep 2026
# Version 1

# TODO: check an input (store the answer)
#   check for valid answer (input checker)
#   Ask questions and respond

# Ask the user wether they like coffee or not
like_coffee = input ("Do you like coffee? ")
print (like_coffee) # checking the input is stored 
print(f"Your answer was '{like_coffee}")

#
if like_coffee == "Yes" or "yes" or "y" or "Y":
    print("That is great! I like coffee to")
else:
    print("You are missing out! Why not give it a go?")