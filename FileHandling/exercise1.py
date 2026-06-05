# Write a program to count how many lines are in students.txt

# create a variable to store the file 
file1 = open("students.txt", "r")

# add the following on the file after creation
# file.write("Students are required to work hard in their studies.\nThey must always remain disciplined throughout their study period.\nThey responsibly for their own lives.")

# count the number of lines
lines = file1.readlines()

# print number of lines
print("Number of lines are ", len(lines))

# close 
file1.close()
