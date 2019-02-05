def count_a(seq):
    """Counting the number of As in the sequence"""
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for b in seq:
        if b == "A":
            count_a += 1
        elif b == "C":
            count_c += 1
        elif b == "G":
            count_g += 1
        elif b == "T":
            count_t += 1

    # Return the result
    return result


# Main program
s = input("Please enter the sequence: ")
na = count_a(s)
print("The number of As is: {}".format(na))

# Calculate the total length
tl = len(s)

# Calculate the percentage of As in the sequence
if tl > 0:
    perc = round(100.0 * na / tl, 1)
else :
    perc = 0

print("The total length is: {}".format(tl))
print("The percentages of As is {}%".format(perc))
