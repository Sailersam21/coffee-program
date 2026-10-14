# Error checking
# Sam Francis_Stead
# 14 oct 2026

# Code that tests whether a valid input was given (v1)
'''done = True # Boolean variable set to true 
while done:
    num = int (input ( "Please enter your value as an inteher: "))
    done = False

    print (f"The number you entered was {num}")'''

# Using a try and except method to check for valid input.
# Use try and except method to catch errors

'''done = True
while done:
    try: # This method tries for a valid input
        num =float (input("Please enter a number: "))
        done = True

    except ValueError:
        print("That is not a number: ")

print(f"The number you have entered is {num}.")'''

# Checking for valid input and recycling code with function (V1.2)
# Create a function to call every time I ask the user
# for a number. A function is a chunk of code that dose somthing
# Functions can be used over and over again.
# To use a function (Call it), write out its name with parenthesis at the end.
# To creat a function, start with word (DEF).

def input_check():
    while True:
        try:
            num = float (input("Please enter a number: "))
            break
        except ValueError:
            print("That is not a valid float number. \n")

    print (f"The number you entered is {num}")
# Main routine
input_check() # this is the function to be used