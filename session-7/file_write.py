# Example of reading a file located in our local filesystem

NAME = "mynotes.txt"

# Open the file
myfile = open(NAME, 'r')   # myfile is an object

print("File opened: {}".format(myfile.name))

contents = myfile.read()

print("The file contents are: {}".format(contents))

myfile.close()

# We open again the file, you can call the object the same as before or different
f = open(NAME, 'a')
f.write("\n\n**THIS IS A TEXT EXAMPLE FOR ADDING TO MY FILE**")
f.close()
print("The end")