class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second

        #Added
        self.weight = weight
        first.edges.append(self)
        second.edges.append(self)

    
    def __eq__(self, edge):
        if isinstance(edge, Edge): # Siden vi jobber med urettede grafer, så vil en kant være lik så legge begge nodene er like.
            return (self.first == edge.first and self.second == edge.second) or (self.first == edge.second and self.second == edge.first)
        return False


    def getNodes(self):
        return [self.first, self.second]
    
    def getOther(self, node):
        if node == self.first:
            return self.second
        return self.first

class Node:
    def __init__(self, name):
        self.name = name

        self.edges = []

        #Added
        self.dist=1e6
        self.prev=None
    
    def __eq__(self, node):
        if isinstance(node, Node):
            return self.name == node.name
        return False
    
    def __hash__(self):
        return ord(self.name)
    
    def addEdge(self, edge):
        self.edges.append(Edge(edge))
    
    def getEdges(self):
        return self.edges

    #Added
    def getNeighbours(self):
        neighbours=[]
        for edge in self.getEdges():
            neighbours.append(edge.getOther(self))
        return neighbours

#Build example graph
nodes=[]
for i in range(9):
    nodes.append(Node(i))
edges=[]

edges.append(Edge(nodes[0],nodes[1],4))
edges.append(Edge(nodes[0],nodes[7],8))

edges.append(Edge(nodes[1],nodes[2],8))
edges.append(Edge(nodes[1],nodes[7],11))

edges.append(Edge(nodes[2],nodes[3],7))
edges.append(Edge(nodes[2],nodes[5],4))
edges.append(Edge(nodes[2],nodes[8],2))

edges.append(Edge(nodes[3],nodes[4],9))
edges.append(Edge(nodes[3],nodes[5],14))

edges.append(Edge(nodes[4],nodes[5],10))

edges.append(Edge(nodes[5],nodes[6],2))

edges.append(Edge(nodes[6],nodes[8],6))
edges.append(Edge(nodes[6],nodes[7],1))

edges.append(Edge(nodes[7],nodes[8],7))

#Dijkstra algorithm
def minDist(Q):
    s=1e7
    for v in Q:
        if v.dist<s:
            u=v
            s=v.dist
    return u

def Dijsktra(nodes,source,target):
    Q=[]
    for v in nodes:
        Q.append(v)
    source.dist=0
    while len(Q)>0:
        u=minDist(Q)
        Q.remove(u)
        neighbors=u.getNeighbours()
        edges=u.getEdges()
        for i in range(len(neighbors)):
            if neighbors[i] in Q:
                alt=u.dist+edges[i].weight
                if alt<neighbors[i].dist:
                    neighbors[i].dist=alt
                    neighbors[i].prev=u
    S=[]
    u=target
    if u.prev!=None or u==source:
        while u!=None:
            S.insert(0,u.name)
            u=u.prev
    return S

print(Dijsktra(nodes,nodes[0],nodes[5]))

