# major of the code is bring and learn from https://github.com/Butskov/Bioinformatics-Algorithms/blob/master/week5-6/13%20-%20String%20Reconstruction%20from%20Read-Pairs%20Problem.py
def string_reconstruction_from_read_pairs(patterns, d):
    return genome_path_problem(eulerian_path_problem(debruijn_from_read_pairs(patterns)), d)

def genome_path_problem(path, d):
    text = path[0][0]
    for pair in path[1: d + 2]:
        text += pair[0][-1]

    text += path[0][1]
    for pair in path[1:]:
        text += pair[1][-1]

    return text


def eulerian_path_problem(dict):
    stack = []
    random_vertex = sorted(dict.keys())[0]
    stack.append(random_vertex)
    path = []
    while stack != []:
        u_v = stack[-1]
        # print(u_v)
        try:
            w = dict[u_v][0]
            stack.append(w)
            dict[u_v].remove(w)
        except:
            path.append(stack.pop())
    return path[::-1]


def paired_prefix(pair):
    return (pair[0][:-1], pair[1][:-1])

def paired_suffix(pair):
    return (pair[0][1:], pair[1][1:])


def debruijn_from_read_pairs(read_pairs):
    read_pairs = list(read_pairs)

    dict = {}

    for pair in read_pairs:
        pair = pair.split('|')

        suffix = paired_suffix(pair)
        prefix = paired_prefix(pair)

        if prefix in dict.keys():
            dict[prefix].append(suffix)
        else:
            dict[prefix] = [suffix]
    return dict

if __name__ == "__main__":
    print('input:')
    data = []
    while True:
        inp = input().strip()
        if inp == '':
            break
        data.append(inp)
    print(string_reconstruction_from_read_pairs(data[1:], int(data[0].split()[1])))
