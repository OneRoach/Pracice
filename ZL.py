class Edge:
    def __init__(self, u, v, w, id):
        self.u = u
        self.v = v
        self.w = w
        self.flag = -1 #flag为1表示选入最小树形图
        self.id = id

    def __str__(self):
        return str(self.u) + str(self.v) + str(self.w)
    def printedges(self):
        print(self.u,self.v,self.w)

class Inderees:
    def __init__(self):
        self.inderee = 9999999999
        self.edge = -1 #代表入边序号

class Cancle:
    def __init__(self):
        self.id = 0
        self.pre = 0

def zhuliu(edges, n, m, root):
    res = 0
    Ans = []
    cancle = []
    k = m
    n_star = n
    Used =  [0 for i in range(100)]
    preid = [0 for i in range(100)]
    for i in range(100):
        cancle.append(Cancle())
    for i in range(m):
        Ans.append(Edge(edges[i].u, edges[i].v, edges[i].w,0))
    while True:
        pre = [-1]*n
        visited = [-1] * n
        circle = []
        inderee = []
        for i in range(n):
            inderee.append(Inderees())
        # 寻找最小入边
        inderee[root].inderee = 0
        for i in range(m):
            if edges[i].u != edges[i].v and edges[i].w < inderee[edges[i].v].inderee:
                pre[edges[i].v] = edges[i].u
                inderee[edges[i].v].inderee = edges[i].w
                inderee[edges[i].v].edge = i
                preid[edges[i].v] = edges[i].id   #将更新边加入
        # 有孤立点，不存在最小树形图
        for i in range(n):
            if i != root and inderee[i].inderee== INF:
                return -1
        # 找有向h环
        tn = 0  # 记录环的个数
        circle = [-1] * n
        for i in range(n):
            res += inderee[i].inderee
            if i != root:
                Used[preid[i]] +=1
                # Ans[inderee[i].edge].flag += 1
            # total = 0
            # for x in range (m):
            #     if Ans[x].flag == 1:
            #         total += 1
            # if total >= n_star - 1 & inderee[i].edge!= -1:          #删边的条件 边数>= n-1 且该边存在
            #     for x in range (m):
            #         if Ans[x].v == Ans[inderee[i].edge].v:      #找到加入边的原头,删去该点所有的入边
            #             Ans[x].flag = -1
            # if inderee[i].edge != -1:
            #     Ans[inderee[i].edge].flag = 1
            # for w in range(m):
            #     print(Ans[w].flag)
            # print(str(res)+" "+str(i) + " " +str(inderee[i].edge) + "\n")
            v = i
            # 向前遍历找环，中止情况有：
            # 1. 出现带有相同标记的点，成环
            # 2. 节点属于其他环，说明进了其他环
            # 3. 遍历到root了
            while visited[v] != i and circle[v] == -1 and v != root:
                visited[v] = i
                v = pre[v]
            # 如果成环了才会进下面的循环，把环内的点的circle进行标记
            if v != root and circle[v] == -1:
                while circle[v] != tn:
                    circle[v] = tn
                    v = pre[v]
                tn += 1
        # 如果没有环了，说明一定已经找到了
        if tn == 0:
            break
        # 否则把孤立点都看作自环看待
        for i in range(n):
            if circle[i] == -1:
                circle[i] = tn
                tn += 1
        # 进行缩点，把点号用环号替代
        for i in range(m):
            v = edges[i].v
            edges[i].u = circle[edges[i].u]
            edges[i].v = circle[edges[i].v]
            # 如果边不属于同一个环
            if edges[i].u != edges[i].v:
                edges[i].w -= inderee[v].inderee
                cancle[k].id = edges[i].id
                cancle[k].pre = preid[v]
                k += 1
                edges[i].id = k - 1
        n = tn
        root = circle[root]
    k -= 1
    while(k >= m):
        if Used[k]:
            Used[cancle[k].id] += 1
            Used[cancle[k].pre] -= 1
        k -= 1
    for i in range(m):
        if Used[i] == 1:
            Ans[i].flag = 1
    print(Used[0:22])
    return res,Ans


INF = 9999999999
if __name__ == '__main__':
    # n, m, root = [3,4,1]
    # edges = []
    # u, v, w = [1, 2, 8]
    # edges.append(Edge(u - 1, v - 1, w))
    # u, v, w = [1, 3, 8]
    # edges.append(Edge(u - 1, v - 1, w))
    # u, v, w = [2, 3, 4]
    # edges.append(Edge(u - 1, v - 1, w))
    # u, v, w = [3, 2, 3]
    # edges.append(Edge(u - 1, v - 1, w))

    n, m, root = [6,9,4]
    edges = []
    u, v, w = [1, 2, 3]
    edges.append(Edge(u - 1, v - 1, w,0))
    u, v, w = [6, 1, 2]
    edges.append(Edge(u - 1, v - 1, w,1))
    u, v, w = [2, 6, 3]
    edges.append(Edge(u - 1, v - 1, w,2))
    u, v, w = [2, 3, 5]
    edges.append(Edge(u - 1, v - 1, w,3))
    u, v, w = [6, 3, 3]
    edges.append(Edge(u - 1, v - 1, w,4))
    u, v, w = [5, 6, 2]
    edges.append(Edge(u - 1, v - 1, w,5))
    u, v, w = [3, 5, 1]
    edges.append(Edge(u - 1, v - 1, w,6))
    u, v, w = [4, 3, 5]
    edges.append(Edge(u - 1, v - 1, w,7))
    u, v, w = [5, 4, 6]
    edges.append(Edge(u - 1, v - 1, w,8))

    res,Ans = zhuliu(edges, n, m, root-1)
    print(res)
    for i in range(m):
        if Ans[i].flag == 1:
            Ans[i].printedges()
