# for loop to create five files at go

list1 = [1, 2, 3, 4, 5]

for file in list1:
    # print(file)
    with open("Report" + str(file) + ".pptx", "w") as docs:
        added_notes = docs.write("This file is created successfully")
print("Process is done!")
