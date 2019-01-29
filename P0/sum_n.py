print("Program for adding the numbers")

def sum_n(number):
    total= 0
    for elem in range(number):
        total = total + elem + 1
    return total
# -- Main program
number = int(input("Insert a number"))
total_sum = sum_n(number)
print("The total sum is {}".format(total_sum))