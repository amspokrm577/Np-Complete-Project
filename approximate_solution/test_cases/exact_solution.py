"""
Max Clique Exact Solution (Bruteforce method)
By: Justin Park
"""
import itertools

def main():
    graph, n = createAdjList()
    if n <= 0:
        print("Not valid")
    else:
        result = bruteforce(graph, n)
        if result is not None:
            clique = result[1]
            output = ' '.join([str(vertex) for vertex in clique])
            print(output)

def createAdjList():
    adj = {}
    n = int(input())
    if n > 0:
        for _ in itertools.islice(range(n), n):
            s1, s2 = input().split()
            s1 = int(s1)
            s2 = int(s2)
            if s1 not in adj:
                adj[s1] = set()
            if s2 not in adj:
                adj[s2] = set()
            adj[s1].add(s2)
            adj[s2].add(s1)
        return adj, n
    return adj, n


def bruteforce(graph, n):
    maxclique = []
    nodes = list(graph.keys())
    #len(nodes) + 1 to include the last node.
    for i in range(len(nodes) + 1):
        k = i
        cliqueResult = getClique(k, nodes, graph)
        if isinstance(cliqueResult, tuple):
            maxclique = tuple(cliqueResult)
            continue
        if cliqueResult == False:
            return maxclique
        #keep incrementing as long check combo returns true. If it returns false, the previous one is the answer
    return maxclique

#check the current combination
def getClique(k, nodes, graph):
    valid = False
    for combo in itertools.combinations(nodes, k):
        valid = validateCombo(combo, graph)
        if valid == True:
            return (valid, combo)
    return valid


def validateCombo(combo, graph):
    for i in range(len(combo)):
        vertex = combo[i]
        if checkNeighbors(combo, vertex, graph) == True and i < len(combo) - 1:
            continue
        if checkNeighbors(combo, vertex, graph) == True and i == len(combo) - 1:
            return True
        if checkNeighbors(combo, vertex, graph) == False:
            return False

#iterate through our combination. checks to see if our current num in combo is in the neighbors list for our current vertex
def checkNeighbors(combo, vertex, graph):
    valid = True
    neighbors = graph.get(vertex)
    for i in range(len(combo)):
        curr = combo[i]
        if curr != vertex:
            if curr not in neighbors:
                valid = False
                return valid
    return valid
         

if __name__ == "__main__":
    main()
