kmers = []
print("input kmers")
while True:
    inp = input().strip()
    if inp == '':
        break
    kmers.append(inp)

def deBruijinGraph(kmers):
    k = len(kmers[0])
    graph = {}
    for i in range(len(kmers)):
        try:
            graph[kmers[i][:-1]].append(kmers[i][1:])
        except:
            graph[kmers[i][:-1]] = [kmers[i][1:]]
    return graph

graph = deBruijinGraph(kmers)

for key, value in sorted(graph.items()):
    print(
        '{} -> {}'.format(
            key, ','.join(sorted([v for v in value]))
        )
    )