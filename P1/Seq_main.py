from seq import Seq

seq_1 = Seq("AGTACACTGGT")
seq_2 = Seq("CGTAAC")
seq_3 = seq_1.complement()
seq_4 = seq_3.reverse()

list_seq = [seq_1, seq_2, seq_3, seq_4]

# Main program

for sequence in list_seq:
    print("Sequence:", sequence.strbases)
    print("  Length:", sequence.len())
    print("  Bases count: A:", sequence.count("A"), ", C:", sequence.count("C"), ", G:", sequence.count("G"), ", T:", sequence.count("T"))
    print("  Bases percentage: A:", sequence.perc("A"), "%", ", C:", sequence.perc("C"), "%", ", G:", sequence.perc("G"), "%", ", T:", sequence.perc("T"), "%")