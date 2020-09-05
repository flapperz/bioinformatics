
# last to first from https://github.com/saishsali/cse549/blob/master/hw2/last_to_first_mapping.py
def find_occurences(text, ch):
    # Find all occurences of character ch in string text
    return [i for i, letter in enumerate(text) if letter == ch]

def last_to_first(transform, i):
    # Get position LastToFirst(i) in first column in the Burrows-Wheeler matrix for a given transform
    ch = transform[i]
    occurence = find_occurences(transform, ch).index(i)
    return sorted(transform).index(ch) + occurence

def inverseBWT(s):
    table = ['' for i in range(len(s))]
    for i in range(len(s)):
        table = [s[i] + x for i,x in enumerate(table)]
        table.sort()
    for e in table:
        if e[-1] == '$':
            return e
    return

def BWMatching(firstCol, lastCol, pattern, last2First):
    top = 0
    bottom = len(lastCol) -1
    while top <= bottom:
        if len(pattern):
            symbol = pattern[-1]
            pattern = pattern[:-1]
            if symbol in lastCol[top:bottom+1]:
                occur = find_occurences(lastCol[top:bottom+1],symbol)
                topIdx = min(occur) + top
                bottomIdx = max(occur) + top
                top = last2First[topIdx]
                bottom = last2First[bottomIdx]
            else:
                return 0
        else:
            return bottom - top + 1
with open('bwt.txt','r') as file:
    bwt = file.read().replace('\n','').strip()
with open('patterns.txt','r') as file:
    patterns_raw = file.read().replace('\n','').strip()
patterns = patterns_raw.split()
firstCol = sorted(bwt)
last2First = [last_to_first(bwt,i) for i in range(len(bwt))]
ans = ' '.join([str(BWMatching(firstCol, bwt, pattern, last2First)) for pattern in patterns])  
print(ans)