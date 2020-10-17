import numpy as np
# traceback and dotwrite from https://bayesianneuron.com/2019/02/nussinov-predict-2nd-rna-fold-structure-algorithm/

def _isPair(a,b):
    if a == 'A' and b == 'U':
        return True
    if a == 'G' and b == 'C':
        return True
    if a == 'G' and b == 'U':
        return True
    return False

def isPair(a,b):
    if _isPair(a,b) or _isPair(b,a):
        return 1
    return 0

def nussinov(rna):

    N = len(rna)
    
    matrix = np.zeros((N,N))

    for k in range(1, N):
        for i in range(N - k):
            j = i + k
            if j - i >= 1:
                matrix[i][j] = max(matrix[i + 1][j],
                                    matrix[i][j - 1],
                                    matrix[i + 1][j - 1] + isPair(rna[i], rna[j]),
                                    max([matrix[i][t] + matrix[t + 1][j] for t in range(i, j)]))
            else:
                matrix[i][j] = 0
    return matrix

def traceback(matrix, rna, fold, i, L):
    """
    Traceback through complete Nussinov matrix to find optimial RNA secondary structure solution through max base-pairs
    """
    j = L
    if i < j:
        if matrix[i][j] == matrix[i + 1][j]: # 1st rule
            traceback(matrix, rna, fold, i + 1, j)
        elif matrix[i][j] == matrix[i][j - 1]: # 2nd rule
            traceback(matrix, rna, fold, i, j - 1)
        elif matrix[i][j] == matrix[i + 1][j - 1] + isPair(rna[i], rna[j]): # 3rd rule
            fold.append((i, j))
            traceback(matrix, rna, fold, i + 1, j - 1)
        else:
            for k in range(i + 1, j - 1):
                if matrix[i][j] == matrix[i, k] + matrix[k + 1][j]: # 4th rule
                    traceback(matrix, rna, fold, i, k)
                    traceback(matrix, rna, fold, k + 1, j)
                    break
    return fold

def dot_write(rna, fold):
    dot = ["." for i in range(len(rna))]
    for s in fold:
        dot[min(s)] = "("
        dot[max(s)] = ")"
    return "".join(dot)

def getSecondaryStructure(rna):
    
    return dot_write(rna, traceback(nussinov(rna), rna, [], 0, len(rna)-1))

if __name__ == "__main__":
    rna = 'GUCAGCAGUGCCUUAGCAGCACGUAAAUAUUGGCGUUAAGAUUCUAAAAUUAUCUCCAGUAUUAACUGUGCUGCUGAAGUAAGGUUGAC' #1
    rna = 'AUGACUGAUUUCUUUUGGUGUUCAGAGUCAAUAUAAUUUUCUAGCACCAUCUGAAAUCGGUUAU' #2
    rna = 'CCTAGTGGTGATAGCGGAGGGGAAACACCCGTTCCCATCCCGAACACGGAAGTTAAGCCCTCCAGCGCCGATGGTAGTTGGGGCCAGCGCCCCTGCAAGAGTAGGTCGCTGCTAGGC' #3

    # rna = input().strip()
    print(rna)
    print(getSecondaryStructure(rna))
