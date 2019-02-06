from Bases import count_bases

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