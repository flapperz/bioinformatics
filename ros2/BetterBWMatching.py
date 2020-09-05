
alphabet = ['A','T','C', 'G', '$']
# last to first from https://github.com/saishsali/cse549/blob/master/hw2/last_to_first_mapping.py
def find_occurences(text, ch):
    # Find all occurences of character ch in string text
    return [i for i, letter in enumerate(text) if letter == ch]

def last_to_first(transform, i):
    # Get position LastToFirst(i) in first column in the Burrows-Wheeler matrix for a given transform
    ch = transform[i]
    occurence = find_occurences(transform, ch).index(i)
    return sorted(transform).index(ch) + occurence

def CreateCountDict(lastcolumn):
    count_dict = dict()
    for eacha in alphabet:
        count_dict[eacha] = [0] * (len(lastcolumn) + 1)
    for i in range(len(lastcolumn)):
        a_acid = lastcolumn[i]
        for eacha in alphabet:
            if eacha == a_acid:
                count_dict[eacha][i + 1] = count_dict[eacha][i] + 1
            else:
                count_dict[eacha][i + 1] = count_dict[eacha][i]
    return count_dict

def BetterBWMatching(firstCol, lastCol, pattern, firstOccur, countDict):
    top = 0
    bottom = len(lastCol) -1
    while top <= bottom:
        if len(pattern):
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in lastCol[top : bottom+1]:
                top = firstOccur[symbol] + countDict[symbol][top]
                bottom = firstOccur[symbol] + countDict[symbol][bottom + 1] - 1
            else:
                return 0

        else:
            return bottom - top + 1

with open('bwmatching_data.txt','r') as file:
    split_raw = file.read().replace('\n',' ').strip().split()
    bwt = split_raw[0]
    patterns = split_raw[1:]

firstCol = ''.join(sorted(bwt))
firstOccur = {k: firstCol.find(k) for k in alphabet}
countDict = CreateCountDict(bwt)

ans = ' '.join([str(BetterBWMatching(firstCol, bwt, pattern, firstOccur, countDict)) for pattern in patterns])

with open('ans.txt','w+') as file:
    file.write(ans)
print(ans)