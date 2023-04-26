"""
Max Clique Exact Solution (Bruteforce method)
By: Justin Park
"""
import itertools

def main():
    n = int(input())
    #checks to see if there is at least one vertice
    if n > 0:
        graph = {}
        #check to make sure that there exists a max clique
        hasAtLeastOneEdge = False
        
        for i in itertools.islice(range(n), n):
            lst = input().split()
            for j in itertools.islice(range(len(lst)), len(lst)):
                lst[j] = int(lst[j])
            lst.pop(0)
            if len(lst) > 0:
                hasAtLeastOneEdge = True
            graph[i] = lst
        if hasAtLeastOneEdge:
            result = bruteforce(graph, n)
            if result is not None and result[1] is not None:
                clique = result[1]
                print("The size of max clique is:", len(clique))
                print("These are the vertices:", clique)
        else:
            print("There are no edges in the graph")
    else:
        print("Invalid number of vertices")


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


if __name__ == "__main__":
    main()
