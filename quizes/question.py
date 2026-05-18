"""
A school wants to develop a simple attendance tracking system using Python. The system should store student names in a text file and allow the teacher to mark attendance daily. Each day’s attendance should be recorded in the same file without deleting previous records. The program should also be able to read the file and display how many times each student has been marked present.

Design a Python program that uses file handling to implement this system. Your solution should also ensure that the file is created automatically if it does not exist and that data is safely appended without overwriting previous records.
"""

import os
from datetime import datetime

# file to store the students records
STUDENT_RECORDS = 'attendance.txt'

# ensure that file which will used to store the student records exits
def initialize_file():
    if not os.path.exists(STUDENT_RECORDS):
        with open(STUDENT_RECORDS, 'w') as file:
            pass

# mark the attendance
def mark_attendance():
    # call the function that checks if the file exits
    initialize_file()

    # record the date of the attendance
    date = datetime.now().strftime("%Y-%m-%d")

    print('\n--- MARK ATTENDANCE ---')

    # STORE THE STUDENT NAME
    student_name = input("Enter your name separating by commas: ").split(",")

    # open the file and store the student name
    with open(STUDENT_RECORDS, 'a') as file:
        for student in student_name:
            # create a variable to stored the formatted student name
            name = student.strip()

            if name:
                file.write(f"{date}, {name} present\n")
    
    # print the success message
    print("Student added successfully!")


# function to display the records per student
def view_attendance():
    # check if the attendance file exist with your system
    initialize_file()

    # create dictionary to display the student record
    attendance_data = {} # empty dictionary

    # open the file that we want to read from 
    with open(STUDENT_RECORDS, "r") as file:
        for line in file:
            # create a variable to hold the parts of each line in the file
            parts = line.strip().split(",")

            # check the length of parts
            if len(parts) == 3:
                date, name, status = parts

                # check on how the status is stord
                if status.lower() == 'present':
                    # add the student record to the dictionary
                    attendance_data[name] = attendance_data.get(name, 0) + 1

    # print the summary of the records
    print("\n ---Attendance summary---")
    # check if any records exist in the attendance data
    if not attendance_data:
        print("No records were found the attendance history")
    else:
        # print the students records
        for student, count in attendance_data.items():
            print(f"{student} : {count} times present")



# menu for our system
def menu():
    while True:
        print("\n===== SCHOOL ATTENDANCE SYSTEM =====")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")


        # let the user enter their choice
        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            mark_attendance()
        elif user_choice == "2":
            view_attendance()
        elif user_choice == "3":
            print("Bye!")
            break
        else:
            print("Invalid input! Try again")



# call the menu function to start your program
menu()