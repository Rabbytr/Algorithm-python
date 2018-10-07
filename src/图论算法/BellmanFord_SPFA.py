from collections import deque

'''
Shortest Path Faster Algorithm
Bellman-Ford算法-SPFA
能够寻找单源负权图的最短路及判断是否存在负环
'''

class edge():  # 考虑是否可修改，如果不可变可以用namedtuple更简洁
    def __init__(self,fro,to,w):
        self.fro = fro
        self.to = to
        self.w = w

def addedge_(fro,to,w):  # 有向图
    edges.append(edge(fro,to,w))
    m = len(edges)
    G[fro].append(m-1)

def bellmanford():
    d[s] = 0
    inq[s] = 1
    Q.append(s)
    while len(Q) is not 0:
        u = Q.popleft()
        inq[u] = 0
        for i in range(len(G[u])):
            e = edges[G[u][i]]
            if d[u]<INF and d[u]+e.w < d[e.to]:
                d[e.to] = d[u] + e.w
                p[e.to] = u
                if not inq[e.to]:
                    Q.append(e.to)
                    inq[e.to] = 1
                    count[e.to] += 1
                    if count[e.to] > n:
                        return False   # 有负环
    return True

if __name__ == '__main__':
    INF = float('inf')

    # 构建初始化图
    n = 4
    s = 0
    t = n-1
    G = []
    edges = []
    for _ in range(n) : G.append([])
    addedge_(0,1,1)
    addedge_(0,2,9)
    addedge_(1,3,2)
    addedge_(2,3,-8)
    #addedge_(3,1,1) # 构建一个负环

    # 初始化相关变量
    Q = deque()
    inq = [0]*n     # 判断结点i是否在队列中
    count = [0]*n   # 记录通过结点i的路径数量
    d = [INF]*n     # s到其余结点的距离
    p = [0]*n       # 记录路径

    print(d) if bellmanford() else print('有负环')
            
    
