# Write a program to copy the contents of students.txt into a new file called backup.txt.

source = open("students.txt", "r")

content = source.read()

source.close()

my_backup = open("backup.txt", "w")

my_backup.write(content)

my_backup.close()