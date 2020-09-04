num = int(input("Enter number of nodes :-"))
graph = []
state = {}
value = []
incoming = {}
#Kamal Subedi(Kie ron)
#18BCE2479
print("Enter the adjacency matrix :-\n")
for i in range(num):
    count = 0
    print("Enter the outlinks of node-", i + 1)
    C = []
    for j in range(num):
        x = int(input())
        C.append(x)
        if x == 1:
            count = count + 1
    value.append(count)
    graph.append(C)
    state[i] = float(1 / num)
iter = int(input("Enter number of iterations :-"))
for c in range(num):
    inter = []
    for r in range(num):
        if graph[r][c] == 1:
            inter.append(r)
    incoming[c] = inter
x = {}
for i in range(iter):
    for node, i in zip(incoming.keys(), incoming.values()):
        z = 0
        for j in i:
            z = z + float(1 / value[j]) * state[j]
        x[node] = z
    state = x
print("\nPageRank values after", iter, "Iterations is :-")
for i, j in zip(state.keys(), state.values()):
    print("page rank value of", "Node", i + 1, j)
