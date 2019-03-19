import json
import termcolor

f = open("exercise1.json", 'r')

# It will create the object "person" with all the info we have in the file
list_people = json.load(f)

print("Total people in the database: ", len(list_people))
for i, dict in enumerate(list_people):
    person = dict
    termcolor.cprint("Name: ", 'green', end='')
    print(person['Firstname'], person['Lastname'])
    termcolor.cprint("Age:", 'green', end='')
    print(person['age'])
    for index, num in enumerate(person['phoneNumber']):
        termcolor.cprint("  Phone {}".format(index), 'blue')
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])

