# with + open -> automatically it closes the file that was being

with open("students.txt", "r") as myfile:

    data = myfile.read()

    print(data)