# file handling -> state where python as language allows you create files
# modes - 4
# r - read (the file must exist )
# w - write (the current of the file must be overwritten)
# a - append (adding data )
# x - create

with open("close.py", "x") as file:
    file.write('# the read mode of files')