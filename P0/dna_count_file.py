def read_file_dna(file):
    f = open(file, "r")
    total_length = 0
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for line in f:
        line = line.replace("\n","")
        total_length += len(line)
        count_a += line.count("A")
        count_c += line.count("C")
        count_g += line.count("G")
        count_t += line.count("T")

    print("Total length:",total_length)
    print("A:",count_a)
    print("C:", count_c)
    print("G:", count_g)
    print("T:", count_t)


read_file_dna("dna.txt")