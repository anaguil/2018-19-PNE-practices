file = "CPLX2.txt"

with open(file) as f:
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for line in f:
        if line.startswith(">"):
            pass
        else:
            count_a += line.count("A")
            count_c += line.count("C")
            count_g += line.count("G")
            count_t += line.count("T")
    print("The number of bases in this file is:\nA:", count_a, "\nC:", count_c, "\nG:", count_g, "\nT:", count_t)

