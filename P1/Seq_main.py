from seq import Seq

seq_1 = Seq("AGTACACTGGT")
seq_2 = Seq("CGTAAC")
seq_3 = seq_1.complement()
seq_4 = seq_3.reverse()

list_seq = [seq_1, seq_2, seq_3, seq_4]

# Main program

for i,sequence in enumerate(list_seq):
    print("Sequence",i+1,":", sequence.strbases)
    print("  Length:", sequence.len())
    print("  Bases count: A:", sequence.count("A"), ", T:", sequence.count("T"), ", C:", sequence.count("C"), ", G:", sequence.count("G"))
    print("  Bases percentage: A:", sequence.perc("A"), "%", ", T:", sequence.perc("T"), "%", ", C:", sequence.perc("C"), "%", ", G:", sequence.perc("G"), "%")
    print()
