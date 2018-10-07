from collections import deque

''' 寻找从s到t的最大流量 '''

class edge():
    def __init__(self,fro,to,cap):
        self.fro = fro
        self.to = to
        self.cap = cap
        self.flow = 0

def addedge(fro,to,cap):
    edges.append(edge(fro,to,cap))
    edges.append(edge(to,fro,0))
    m = len(edges)
    G[fro].append(m-2) # G[i][j]为第i个结点的第j条边在edges中的序号
    G[to].append(m-1)

def EdmondsKarp():
    # Edmonds-Karp算法
    flow = 0
    while True:
        Q.clear()
        Q.append(s)
        a = [0]*n
        a[s] = float('inf')
        while len(Q) is not 0:
            x = Q.popleft()
            for i in range(len(G[x])):
                e = edges[G[x][i]]
                if not a[e.to] and e.cap>e.flow:
                    p[e.to] = G[x][i]
                    a[e.to] = min(a[x],e.cap-e.flow)
                    Q.append(e.to)
            if a[t] : break
        if not a[t] : break
        u = t
        while u!=s:
            edges[p[u]].flow += a[t]
            edges[p[u]^1].flow -= a[t]
            u = edges[p[u]].fro
        flow += a[t]
    return flow


if __name__ == '__main__':
    # 初始化图结构
    n = 4
    edges = []
    G = []
    for _ in range(n):G.append([])
    addedge(0,1,6)
    addedge(0,2,12)
    addedge(1,2,5)
    addedge(1,3,8)
    addedge(2,3,9)
    addedge(0,3,10)

    # 初始化算法参数
    s = 0             # 起始结点
    t = n-1           # 终止结点
    p = [0]*n         # 记录路劲
    Q = deque()
   
    print(EdmondsKarp())
