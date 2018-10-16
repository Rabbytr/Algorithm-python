from collections import namedtuple

'''
Tarjan算法，寻找有向图中的强连通分量
'''


def addedge(fro,to):
    Edges.append(edge(fro,to))
    m = len(Edges)
    G[fro].append(m-1)

def Tarjan(u): # Tarjan算法
    global index,cur
    index += 1
    DFN[u] = Low[u] = index
    Stack.append(u)
    for i in G[u]:
        e = Edges[i]
        if not DFN[e.to]:
            Tarjan(e.to)
            Low[u] = min(Low[u],Low[e.to])
        elif e.to in Stack:
            Low[u] = min(Low[u],DFN[e.to])
    if DFN[u] == Low[u]:
        cur += 1
        while True:
            v = Stack.pop()
            Belong[v] = cur
            if u == v:break

if __name__ == '__main__':
    # 构建图
    n = 5
    edge = namedtuple('edge',['fro','to'])
    Edges = []
    G = []
    for _ in range(n):G.append([])
    addedge(0,1)
    addedge(1,2)
    addedge(2,1)
    addedge(1,3)
    addedge(3,4)
    addedge(4,3)
    addedge(4,2)
    
    DFN = [0]*n
    Low = [0]*n
    Belong = [0]*n

    Stack = []
    index = 0
    cur = 0
    Tarjan(0)

    print(Belong)
