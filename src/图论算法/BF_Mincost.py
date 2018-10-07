from collections import deque

'''
最小费用最大流
基于 Bellman-Ford 算法
'''

class edge():
    def __init__(self,fro,to,cap,cost):
        self.fro = fro
        self.to = to
        self.cap = cap
        self.cost = cost
        self.flow = 0

def addedge(fro,to,cap,cost):
    edges.append(edge(fro,to,cap,cost))
    edges.append(edge(to,fro,0,-cost))
    m = len(edges)
    G[fro].append(m-2)
    G[to].append(m-1)


if __name__ == '__main__':
    INF = float('inf')

    n = 4
    s = 0
    t = n-1
    edges = []
    G = []
    for _ in range(n) : G.append([])
    addedge(0,1,2,2)
    addedge(0,2,1,5)
    addedge(1,2,1,2)
    addedge(1,3,1,3)
    addedge(2,3,1,1)

    a = [0]*n
    p = [0]*n

    flow = 0   # 总流动
    cost = 0   # 总费用
    while True:
        d = [INF]*n
        inq = [0]*n
        
        a[s] = INF   # s到每个结点的最小残量
        d[s] = 0
        inq[s] = 1

        Q = deque()
        Q.append(s)
        while len(Q) is not 0:
            u = Q.popleft()
            inq[u] = 0
            for i in range(len(G[u])):
                e = edges[G[u][i]]
                if e.flow<e.cap and d[u]+e.cost < d[e.to]:
                    d[e.to] = d[u] + e.cost
                    a[e.to] = min(a[u],e.cap-e.flow)
                    p[e.to] = G[u][i]
                    if not inq[e.to]:
                        Q.append(e.to)
                        inq[e.to] = 1
        if d[t] == INF : break         # 残量网络不连通t结点
        flow += a[t]
        cost += d[t]*a[t]
        u = t
        while u!=s:
            edges[p[u]].flow += a[t]
            edges[p[u]^1].flow -= a[t]
            u = edges[p[u]].fro
    
    print('Max flow: {}, Min cost: {}'.format(flow,cost))




        
