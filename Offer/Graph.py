class Vertex:
    def __init__(self, key):
        self.connectedTo = {}
        self.id = key
    # 添加邻居节点设置权重
    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    # 获取所有的邻居节点
    def getConnections(self):
        return self.connectedTo.keys()
    # 当前节点的value
    def getId(self):
        return self.id
    # 节点与邻居节点的权重
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph: # 无向图
    # v 顶点个数
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0    # 顶点的个数
    # 添加节点
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    # 获取节点
    def getVertex(self, n):
        if n in self.vertList: return self.vertList[n]
        else: return None

    def __contains__(self, n):
        return n in self.vertList
    # 添加为邻居节点
    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)
    # 获取所有节点
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    # 广度优先遍历
    def bsf(self, s, t):
        if s == t: return None
        visited = {}
        for key in self.vertList.keys():
            visited[key] = False
        visited[s] = True
        queue = []
        queue.append(self.getVertex(s))
        pre = {}
        while len(queue) != 0:
            w = queue.pop()
            for q in w.getConnections():
                if not visited[q.id]:
                    pre[q.id] = w.id
                    if q.id == t:
                        self.bsf_print(pre, s, t)
                        return
                    visited[q.id] = True
                    queue.append(q)

    # 输出广度优先遍历的路径
    def bsf_print(self, pre, s, t):
        if t in pre and (str(s) != str(t)):
            self.bsf_print(pre, s, pre[t])
        print(str(t) + '')





if __name__ == "__main__":

    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)

    print(g.vertList)
    g.bsf(1, 5)