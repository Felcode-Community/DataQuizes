"""
Session 1 — Bus fare calculator (if / elif / else)

Q1. Write a Python program that asks the user for a passenger's age and prints the correct bus fare. Use these rules: under 5 = free, age 5–17 = KSh 30, age 18–59 = KSh 60, age 60 and above = KSh 20.

Q2. Modify your program to reject any age below zero and print an error message instead of a fare.

Q3. Ask the user how many tickets they want and calculate the total fare for that number of passengers of the same age.

Stretch: Add a weekend surcharge of KSh 10 for adult passengers only, using a nested if statement inside the adult condition.

--------------------------------------------------"""

# prompt for the user age 
user_age = int(input("Please enter the passanger age: "))




# create the conditions that assist us tell the amount the passenger is to pay
if user_age >= 0 and user_age < 5:
    
    print("You are not supposed to pay any amount, enjoy your journey")
    

elif user_age >= 5 and user_age <= 17:
    
    print("You are supposed to pay Ksh. 30")
    
elif user_age >= 18 and user_age <= 59:
    number_of_tickets = int(input("How many tickets do you want? "))

    # check on the day
    day = input("Enter the day of the week? ")
    if day == "Saturday" or day == "Sunday":
        print("Fare is ksh. 70")
        amount = 70 * number_of_tickets
        # print("Your fare is Ksh. 60")
        print(f"Based on the number of tickets entered, total amount you are supposed pay is Ksh. {amount}")
    else:
        amount = 60 * number_of_tickets
        print("Your fare is Ksh. 60")
        print(f"Based on the number of tickets entered, total amount you are supposed pay is Ksh. {amount}")


    
elif user_age >= 60:
    
    print("Your fare is ksh. 20")
    
else:
    print("Invalid user age!")