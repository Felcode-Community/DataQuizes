with open("Report.pdf", "w+") as report:

    content = report.write("Hi! Art of Invisibility\n")

    output = report.read()

    print(output)