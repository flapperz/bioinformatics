s = 'TAGTTGGTGTCGCATGATGGGTTAGCAGCTACGGAGCGAAGGAGATTTATTGCGAAGTGACCACACAGAGGCTCACCATACTTGTCTAATTAGGTACGATCTTGCTAATACTGACTTATGCAGAAGGTAAAGCAGGGATAACAGGAATCAGTGGCGTCCTCGCGTCGGAGCATTTGGTCGGCGCTAGGCATAGAGATTACCTAACGGTCTAGGAAGAACTCTCAACACCTCGGACGGGTATCGGTGATCTACTTAGTGGATCATTGCATCGCGGACGTGCTGGTTCGAGATAACGAACAAAAAGCTCGAGTTCTCTCATCCGGTTAACGTTGCTTTAGCCCCCCTGGCCCTGTATGCGCGCGGTGCATATTATTTGTGGGAAACACTATTGCATTTGCACCAGAAGCTTGAAGCTATGATGACTATTGGGGTCGGCGCTTGTGATTCGTCCCGTTGATAACCGAAAAGTACGGGCACGGATACAAATGGGAAAAAGGTTACCCTGGGACCTGCGGAGATATTGGTGGAGCGTGACTAACTGCTTCACAACTAGCACGCTTCTGCCCCCGAGGTAGCCCTGGTTTCAGCGATTTGTAGGGCTGTGTATTCGGCAACACAAGATGTGGTTTAACGTTCCGAAAAGACCCGAGCGTAGCAAACGCCGGTTTAATTAGTGGAATGTACTAGGTGACTGAAAAGCAGTGTTTTTATATGGCGACTCTGTCGCTGGTATACTTGATTGCTGAGGTGCTCAACTTATCGTATTGTGGGGTGACGGTGGTATAACGCATACTATATGACTCCGTGACGACTTTATGGCACAGTGAAAATAATAGAAATGGGCCGTAGGGATGCTGAGCTACCGGTCGCGCGGTGGAGGGCCTCTTTACGCGGGTTAGGCAACATGATCTAGCCATTCAGCCGGTGGCGATGACCTTGGAC$'

matrix = []
for i in range(len(s)):
    matrix.append(s)
    s = s[-1] + s[:-1]

print(
    ''.join([x[-1] for x in sorted(matrix)])
)