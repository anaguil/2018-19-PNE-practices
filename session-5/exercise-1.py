def count_bases(seq):
    """Counting the number of bases in the sequence"""
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    dictionary_bases = dict()
    for b in seq:
        if b == "A":
            count_a += 1
        elif b == "C":
            count_c += 1
        elif b == "G":
            count_g += 1
        elif b == "T":
            count_t += 1
    dictionary_bases = {"Base A": count_a, "Base C": count_c, "Base G": count_g, "Base T": count_t}

    # Return the result
    return dictionary_bases


# Main program
s = input("Please enter the sequence: ")
dictionary_bases = count_bases(s)
# Calculate the total length
tl = len(s)

print("The total length is: {} bases".format(tl))

for key, value in dictionary_bases.items():
    print(key)
    print("  Counter:", value)
    if tl > 0:
        perc = round(100 * value / tl, 1)
    else:
        perc = 0
    print("  Percentage: {}".format(perc))