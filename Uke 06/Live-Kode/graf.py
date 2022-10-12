from node import Node
from edge import Edge

def lesFil(filnavn):
    f = open(filnavn, "r")
    nodes = []
    edges = []

    matrix = []
    
    linje1 = f.readline().split()
    for noder in linje1:
        node = Node(noder)
        nodes.append(node)

    for linjer in f:
        matrix.append(linjer.split())
    
    for i in range(len(nodes)): #Index 0 representerer A, Index 1 representerer B, osv osv
        for j in range(len(nodes)):
            
            if matrix[i][j] == "1": #I matrisen vil det si at det er en kant mellom node i og node j
                kant = Edge(nodes[i], nodes[j])
                if kant not in edges:
                    nodes[i].addEdge(kant)
                    nodes[j].addEdge(kant)
                    edges.append(kant)
    f.close()
    
    return (nodes, edges)
#Utfordring: Lag graf ved å lese inn fra en fil som er naboliste(graf.txt)

def DFSVisit(G, s, visited): #G er grafen, s er stsrtnode, visited er en liste med besøkte noder
    stack = [s] # I python er stack en liste. bruker vi pop() og append funkjonene så legger vi til/fjerner vi elementer som  en stack
    while len(stack) != 0:
        u = stack.pop()
        if u not in visited:
            visited.add(u)
            print(u.name)
            for kanter in u.getEdges(): #Går gjennom alle kantene til noden
                #Her skal alle kanter som går fra u legges til i stacken
                stack.append(kanter.getOther(u)) #Pusher den andre noden på kanten

def DFSFull(G):
    visited = set()
    for v in G[0]: #index 0 er noder, index 1 er kanter
        if v not in visited:
            DFSVisit(G, v, visited)


def BFSVisit(G, s, visited):
    queue = [s] # I python er en queue en liste, vi kan bruke append() og pop(0) funksjonene for å simulere en queue(FIFO)
    visited.add(s)
    print(s.name)
    while len(queue) != 0:
        u = queue.pop(0)
        for kanter in u.getEdges(): #Går gjennom kantene til en node.
            #if u in kanter.getNodes():
            v = kanter.getOther(u)
            if v not in visited:
                print(v.name)
                visited.add(v)
                queue.append(v)


def BFSFull(G):
    visited = set()
    for v in G[0]: #Index 0 er noder, index 1 er kanter
            if v not in visited:
                BFSVisit(G, v, visited)



graf = lesFil("graf2.txt")

print("DFS:")
DFSFull(graf)
print("")
print("")
print("BFS:")
BFSFull(graf)

