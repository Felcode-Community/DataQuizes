# function contains the following
# function name
# set of parenthesis
# full stop
# keyword def
# functions returns a value
# for a function to used it must be called

# example

# create a function that prompts the user to enter their name and reverse the name

def reverse_username():
    # let the user enter their name
    username = input("Please enter your name ")

    # reverse the name e.g john -> nhoj
    reversed_name = username[ : : -1] # slicing
    print(f"Reversed name is {reversed_name}")

# call the function
reverse_username()
