class Node:
    def __init__(self, name):
        self.name = name
        self.edges = []
    
    def __eq__(self, node):
        if isinstance(node, Node):
            return self.name == node.name
        return False
    
    def __hash__(self):
        return ord(self.name)
    
    def addEdge(self, edge):
        self.edges.append(edge)
    
    def getEdges(self):
        return self.edges