from queue import PriorityQueue
from collections import namedtuple

'''
采用优先队列优化的迪杰斯特拉算法
寻找正权图上的单源最短路
'''

class edge():  # 考虑是否可修改，如果不可变可以用namedtuple更简洁
    def __init__(self,fro,to,w):
        self.fro = fro
        self.to = to
        self.w = w

def addedge(fro,to,w):  # 无向图
    edges.append(edge(fro,to,w))
    edges.append(edge(to,fro,w))
    m = len(edges)
    G[fro].append(m-2)
    G[to].append(m-1)

def addedge_(fro,to,w):  # 有向图
    edges.append(edge(fro,to,w))
    m = len(edges)
    G[fro].append(m-1)

if __name__ == '__main__':
    INF = float('inf')

    # 图的初始化
    n = 4
    s = 0
    t = n-1
    G = []
    edges = []
    for _ in range(n):G.append([])
    addedge(0,1,1)
    addedge(0,2,9)
    addedge(1,3,2)
    addedge(2,3,3)

    # 算法相应的变量初始化
    d = [INF]*n  # 记录当前s到i结点的最短距离d[i]
    d[s] = 0     # 初始结点到自身距离为0
    vis = [0]*n  # 结点是否已经求得
    p = [0]*n    # 记录路径
    
    Q = PriorityQueue()  # 优先队列
    node = namedtuple('PNode',['w','fro']) # PriorityQueue默认根据PNode[0]排序

    Q.put(node(0,s))
    while not Q.empty():
        x = Q.get()
        u = x.fro
        if vis[u] : continue
        vis[u] = True
        for i in range(len(G[u])):
            e = edges[G[u][i]]
            if d[u]+e.w < d[e.to]:          # 有更好的路径选择，更新
                d[e.to] = d[u]+e.w
                Q.put(node(d[e.to],e.to))
                p[e.to] = u                  # u = edges[G[u][i]].fro

    print(d)

