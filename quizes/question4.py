"""A school keeps student marks in a text file where each line contains a student’s name and their marks. The administration wants a program that reads this file and calculates the average marks, highest score, and lowest score among all students.

Design a Python program that reads data from the file, processes it, and displays a summary report. The results should also be saved into a new file called report.txt."""

# import os
import os

# files containing student marks
input_file = "student_records.txt"
output_file = "report.txt"

# checks if files exists
if os.path.exists(input_file):

    names = []
    marks =[]

    # read the file with student records
    with open(input_file, "r") as file:
        for line in file:
            data = line.strip().split()
            # data = ["john", 68]

            #  expected format Name, marks
            if len(data) == 2:
                name = data[0]
                mark = int(data[1])

                # store the marks and names in the lists
                names.append(name)
                marks.append(mark)

    # check if the data exist
    if marks:
        # calculate the total
        total = sum(marks)
        average = total / len(marks)
        highest_score = max(marks)
        lowest_score = min(marks)

        # match the students scores with thier name
        highest_student = names[marks.index(highest_score)]
        lowest_student = names[marks.index(lowest_score)]

        # display the report
        with open(output_file, "w") as file:
            file.write("Summary of the Scores")
            file.write(f"\nAverage is {average:.2f}")
            file.write(f"\nStudent with Highest score: name: {highest_student} marks: {highest_score}")
            file.write(f"\nStudent with lowest score name: {lowest_student} marks: {lowest_score}")
            print(f"\n\bSCORE SUMMARY REPORTS\n\bAverage marks {average:.2f}\n\bHighest Score student name: {highest_student} marks: {highest_score}\n\bLowest score student name: {lowest_student} marks: {lowest_score} \n That is all for today!")

        print("\nReport summary successfully saved!")
    
    else:
        print("There is no valid marks")

else:
    print("The file do not exist")






