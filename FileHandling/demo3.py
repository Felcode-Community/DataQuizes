notes = open("pythonNotes.txt", "r+")
# the mode above allows us to read and write into file at same time

# write to file
notes.write("Welcome to the data science course. It entails alot")

# read the file
print(notes.read())

# write to the file
notes.write("\nBye done!")

# close the file file
notes.close()