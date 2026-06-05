# file handling - is a processing of creating, reading, writing and managing files on a computer
# python allows to stores programs permanently on the computer

# the functions to help us work with files
# open()

# syntax of function when either of process happens
# file_name = open("nameOfFileToOpen", "mode")

# modes -> r, x, a, w, 
# r+ => read write 
# w+ => read, write, create, delete
# a+ -> read, write, creat

students_data = open("student_performance.xlsx", "x")