"""
A school wants to develop a simple attendance tracking system using Python.
The system should store student names in a text file and allow the teacher
to mark attendance daily.

Each day’s attendance should be recorded in the same file without deleting
previous records.

The program should also be able to read the file and display how many times
each student has been marked present.

This solution uses:
- File handling
- Functions
- Dictionaries
- Append mode
- Automatic file creation
"""

# import os module for checking if file exists
import os

# import datetime module for recording current date
from datetime import datetime


# file used to store attendance records
STUDENT_RECORDS = "attendance.txt"


# function to create the file if it does not exist
def initialize_file():

    # check whether the attendance file exists
    if not os.path.exists(STUDENT_RECORDS):

        # create an empty attendance file
        with open(STUDENT_RECORDS, "w") as file:
            pass


# function for marking attendance
def mark_attendance():

    # ensure the attendance file exists
    initialize_file()

    # get today's date
    date = datetime.now().strftime("%Y-%m-%d")

    print("\n--- MARK ATTENDANCE ---")

    # allow user to enter many names separated by commas
    student_names = input(
        "Enter student names separated by commas: "
    ).split(",")

    # open the file in append mode
    # append mode prevents overwriting previous records
    with open(STUDENT_RECORDS, "a") as file:

        # loop through all entered student names
        for student in student_names:

            # remove extra spaces from student name
            name = student.strip()

            # ensure empty names are not saved
            if name:

                # save attendance record in file
                # format: date,name,status
                file.write(f"{date},{name},present\n")

    # display success message
    print("Attendance recorded successfully!")


# function for viewing attendance summary
def view_attendance():

    # ensure the file exists before reading
    initialize_file()

    # dictionary used to count attendance
    attendance_data = {}

    # open attendance file in read mode
    with open(STUDENT_RECORDS, "r") as file:

        # read each line from the file
        for line in file:

            # remove unnecessary spaces/newlines
            line = line.strip()

            # skip empty lines
            if line == "":
                continue

            # split line into parts using comma
            parts = line.split(",")

            # check if line has correct format
            if len(parts) == 3:

                # unpack the data
                date, name, status = parts

                # check if student was marked present
                if status.lower() == "present":

                    # count attendance for each student
                    attendance_data[name] = (
                        attendance_data.get(name, 0) + 1
                    )

    # display attendance summary
    print("\n--- ATTENDANCE SUMMARY ---")

    # check whether records exist
    if not attendance_data:

        print("No attendance records found.")

    else:

        # display each student and attendance count
        for student, count in attendance_data.items():
            print(f"{student} : {count} times present")


# main menu function
def menu():

    # keep program running until user exits
    while True:

        print("\n===== SCHOOL ATTENDANCE SYSTEM =====")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Exit")

        # get user's menu choice
        user_choice = input("Enter your choice: ")

        # option for marking attendance
        if user_choice == "1":
            mark_attendance()

        # option for viewing attendance summary
        elif user_choice == "2":
            view_attendance()

        # option for exiting the system
        elif user_choice == "3":
            print("Bye!")
            break

        # handle invalid inputs
        else:
            print("Invalid input! Try again.")


# start the attendance system
menu()