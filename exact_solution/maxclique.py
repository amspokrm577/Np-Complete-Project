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
    for i in itertools.islice(range(n + 1), n + 1):
        k = i
        cliqueResult = getClique(k, nodes, graph)
        if isinstance(cliqueResult, tuple):
            maxclique = tuple(cliqueResult)
            continue
        if cliqueResult == False:
            return maxclique
        #keep incrementing as long check combo returns true. If it returns false, the previous on eis the answer
    return maxclique

#check the current combination
def getClique(k, nodes, graph):
    valid = False
    for combo in itertools.combinations(nodes, k):
        valid = validateCombo(combo, graph)
        if valid == True:
            return valid, combo
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
         

    """
    for j in range(len(combo)):
        vertex = combo[j]
        #neighbors do not include vertexes in combo but there are more combinations
        if checkNeighbors(graph, combo, vertex) == False and i < len(combos) - 1:
            break
        #neigbors do not include combo vertexes and this is the very last possible combination
        elif checkNeighbors(graph, combo, vertex) == False and i == len(combos) - 1:
            return False
        #combo vertexes are found in neighbors and there are more combo vertexes to go
        elif checkNeighbors(graph, combo, vertex) == True and j < len(combo) - 1:
            continue
        #combo vertexes are found in neighbors and this is the last vertex in combo
        elif checkNeighbors(graph, combo, vertex) == True and j == len(combo) - 1:
            return (True, combo)   
    """


"""
#main function called that iterates over entire list of vertices. gets the combination at i which is our k.
#if a cliquesize of i exists, then we increment to the next. if the next does not then we know our max clique
#is our previous one. 
def bruteforce(graph, n):
    temp = []
    for i in itertools.islice(range(n + 1), n + 1):
        combos = getCombos(graph, i)
        result = check(graph, n, combos)
        #if our check is valid
        if isinstance(result, tuple):
            temp = tuple(result)
            continue
        if result == False:
            return temp
    return temp 
        
#gets all combinations given graph and k which is our current clique size we are looking for
def getCombos(graph, k):
    combinations = []
    nodes = list(graph.keys())
    for combo in itertools.combinations(nodes, k):
        #cannot do this
        combinations.append(combo)
    return combinations

#iterates through all our combos and passes each combo to checkneighbors for validity purposes
def check(graph, k, combos):
    for i in range(len(combos)):
        combo = combos[i]
        for j in range(len(combo)):
            vertex = combo[j]
            #neighbors do not include vertexes in combo but there are more combinations
            if checkNeighbors(graph, combo, vertex) == False and i < len(combos) - 1:
                break
            #neigbors do not include combo vertexes and this is the very last possible combination
            elif checkNeighbors(graph, combo, vertex) == False and i == len(combos) - 1:
                return False
            #combo vertexes are found in neighbors and there are more combo vertexes to go
            elif checkNeighbors(graph, combo, vertex) == True and j < len(combo) - 1:
                continue
            #combo vertexes are found in neighbors and this is the last vertex in combo
            elif checkNeighbors(graph, combo, vertex) == True and j == len(combo) - 1:
                return (True, combo)   

#checks the values in combination to see if they are in the neighbors list (from adj_list) of current vertex in combo
def checkNeighbors(graph, combo, vertex):
    result = True
    neighbors = graph.get(vertex)
    #iterating through combo
    for i in range(len(combo)):
        #current number in combo
        curr = combo[i]
        #check to see if vertex is not curr because curr will not be in the neighbors
        if curr != vertex:
            if curr not in neighbors:
                result = False
    return result

"""

if __name__ == "__main__":
    main()