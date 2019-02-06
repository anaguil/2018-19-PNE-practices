from Bases import count_bases

s1 = input("Enter the sequence 1: ")
s2 = input("Enter the sequence 2: ")

sequences = [s1,s2]


for s in sequences:
    dictionary_bases = count_bases(s)
    tl = len(s)

    print("The sequence is {} bases in length".format(tl))

    for key, value in dictionary_bases.items():
        print(key)
        print("  Counter:", value)
        if tl > 0:
            perc = round(100 * value / tl, 1)
        else:
            perc = 0
        print("  Percentage: {}".format(perc))
    print()
