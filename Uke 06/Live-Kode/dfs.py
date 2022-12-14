
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