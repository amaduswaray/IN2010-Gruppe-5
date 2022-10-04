class Edge:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    
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
    