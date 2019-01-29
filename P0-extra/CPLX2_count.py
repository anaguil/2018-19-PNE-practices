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
            count= line.count("A")
            counter_a += count

