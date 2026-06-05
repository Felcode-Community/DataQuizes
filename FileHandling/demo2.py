# create file called notes.txt

my_notes = open("pythonNotes.txt", "a")

# add some notes inside the file
my_notes.write("\nData Science Notes")
my_notes.write("\n\nFile Handling")

# close the file
my_notes.close()