from collections import namedtuple

'''
求无向图桥
'''

def addedge(fro,to):
    Edges.append(edge(fro,to))
    Edges.append(edge(to,fro))
    m = len(Edges)
    G[fro].append(m-2)
    G[to].append(m-1)

def DFS(u,fa):
    global dfs_clock
    dfs_clock += 1
    lowu = pre[u] = dfs_clock
    child = 0
    for i in G[u]:
        e = Edges[i]
        if not pre[e.to]:
            child += 1
            lowv = DFS(e.to,u)
            lowu = min(lowu,lowv)
            if lowv > pre[u]:
                isbridge[i] = 1  # 记录一个桥
        elif pre[e.to] < pre[u] and e.to != fa: # 反向边更新low(不能为父节点)
            lowu = min(lowu,pre[e.to])
    low[u] = lowu
    return lowu

if __name__ == '__main__':
    # 构建图
    n = 5
    edge = namedtuple('edge',['fro','to'])
    Edges = []
    G = []
    for _ in range(n):G.append([])
    addedge(0,1)
    addedge(0,2)
    addedge(1,3)
    addedge(1,4)
    addedge(3,4)

    m = len(Edges)
    
    dfs_clock = 0 
    pre = [0]*n
    low = [0]*n
    isbridge = [0]*m

    for i in range(n):
        if not pre[i]:DFS(i,-1)
    print([Edges[i] for i in range(m) if isbridge[i]])

    
