# Creating a coffee program that a user will be able to interact with.
# Sam Francis-Stead
# 23 Sep 2026
# Version 1

# TODO: check an input (store the answer)
#   check for valid answer (input checker)
#   Ask questions and respond

# Version 1
'''# Ask the user wether they like coffee or not
like_coffee = input ("Do you like coffee? ")
print (like_coffee) # checking the input is stored 
print(f"Your answer was '{like_coffee}")

#
if like_coffee == "Yes" or "yes" or "y" or "Y":
    print("That is great! I like coffee to")
else:
    print("You are missing out! Why not give it a go?")'''

# Version 2
# While loop to test the program

keep_going =""
while keep_going == "":
    like_coffee = input ("do you like coffee? ")
    # print (like_coffee)  # checking the input is stored
    print (f"your answer was '{like_coffee}'.")

    # Check the input and respond (to be fixed next time)
    if like_coffee == "Yes" or like_coffee == "yes" or like_coffee == "y" or like_coffee== "Y":
        print("That is great! I like coffee to")
        print("Finish") 
    elif like_coffee == "no" or like_coffee == "no" or like_coffee == "N" or like_coffee == "n":
        print("You are missing out! Why not give it a go?")
        keep_going = "serdtfghyuijvhgf"
    else:
        print ("I dont understand! pls try again.")
    keep_going = input ("press <Enter> to try again or any other key to exit")
