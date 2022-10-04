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