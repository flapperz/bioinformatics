s = 'GTTATCCGTCGTTAGCGGTCGCCGTCTGGACATACCACGTAGGACCCTTTTGCCCGTTCCTCGTCAGTTGCTCCGTAGATCGATATCCATCAGCCCTAACGCCAGAGCTACCGGTGGAAACTTTCGGGTGCTGGGTGAAGCCCACTCTATACGTTAGCGTTAGCCGCAACCTACAGCGCCGATTTAAAATATGGCCGCAACTGCTTAGTGAAGTTCGGATAGTACCAGAATATAGCTACTTTGTACGCCCACCTCCCAACGTTGCAGCTCTCTGATATTGATAAAGGGGAATATTGTAACTAAGCTGATCCGGCGGTGTGGAGACTGGGCGGACGCGTAAAGTAACCAAGAGCTCAAAACCGCTGGAAGTGTGGCCTGCACGCCTCCCGCAGATAGGCCGTGACCTTTTCGGAGTCATCGTATATGTTGCGAGTCGACCGGGTAAATACTCACCCTTCACAATAGAACCTGCCTTACGTGCTATGCTACGCATCCTGATAAATTAGTGAAGCGTCTCTATCTAGTCAAACATCGCCATGTTAAGGCGTATTAATTTTGGTGCTGTCTGGTGCAGTCCCGGTACTTGCCACCAAGCACCGACACTTGCTTCGTTTTTAAAGCGAGTAGTGACGCAACGCCGGGGCGGTTCTCAATCACTCGGCGGCCAGAGTTGGTCTAAGGGTCATACTGTACGTTTACGCATAACGCTAGGGCTTTTCGACGCTGATCGCGTCTGTGTGCGATTGCATATTAAGAGAACGCATGTTCCAGGGGACCGGAGACTTAAAGGGGCTCACCCAAATGTAGCTGTGTGAACTTGGCAGACAGCTCCATTATGTAACATGGTGTCTCTGCCGATCGGGGATATATTGGTAAGAAGCAATTCTAGTGGAATGGGCTAAATGGTCGCATGTGGTGGGGGACCTGTACCGGGGTGACATGATTTAAATGATGTGGTCCGGAGCCATCTTAACATGCCATACTGC'

alphabet = ['A','T','C', 'G']

print(' '.join(str(s.count(a)) for a in sorted(alphabet)))