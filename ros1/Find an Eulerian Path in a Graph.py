def FindStartNode(graph):
    indegree = {}
    for u,vs in graph.items():
        for v in vs:
            try:
                indegree[v] += 1
            except:
                indegree[v] = 1
    for u,degrees in indegree.items():
        if u in graph and len(graph[u]) == degrees+1:
            return u

def EulerPath(graph):
    stack = [FindStartNode(graph)]
    res = []
    while stack:
        v = stack[-1]
        if v not in graph or not graph[v]:
            stack.pop()
            res.append(v)
        else:
            u = graph[v].pop()
            stack.append(u)
    return res[::-1]
graph = {}
print("input graph:")
while True:
    inp = input().strip().split()
    if inp == []:
        break
    graph[inp[0]] = inp[2].split(',')
print ('->'.join(EulerPath(graph)))