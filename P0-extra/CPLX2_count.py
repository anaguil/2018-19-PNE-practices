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
            counter_a = line.count("A")
            count_a += counter_a
            counter_c = line.count("C")
            count_c += counter_c
            counter_g = line.count("G")
            count_g += counter_g
            counter_t = line.count("T")
            count_t += counter_t
    print("The number of bases in this file is: \n A: ", count_a, "\nC: ", count_c, "\nG: ", count_g, "\nT: ", count_t)

