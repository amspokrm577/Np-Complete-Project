"""
Approximation for max clique

Author: Ross Amspoker

"""

"""

"""
def greedy(graph, val):
    s = set()
    s.add(val)
    for u in graph[val]: # O(deg(v))
        del graph[u]
    del graph[val]
    while graph: # O(n)
        curr = min(graph, key=lambda k: len(graph[k])) # O(n)
        for u in graph[curr]: # O(deg(curr))
            if u in graph: 
                del graph[u]
        del graph[curr]
        s.add(curr)
    return s


def main():
    # example usage:
    n = int(input())
    adj_list = {}
    for _ in range(n):
        arr = [int(i) for i in input().split()]
        if arr[0] not in adj_list:
            adj_list[arr[0]] = set()
        if arr[1] not in adj_list:
            adj_list[arr[1]] = set()
        adj_list[arr[1]].add(arr[0])
        adj_list[arr[0]].add(arr[1])

    verts = adj_list.keys()
    complement = {i:{j for j in verts if j not in adj_list[i] and j != i} for i in verts} # O(v^2)
    arr = sorted(complement, key=lambda k: len(complement[k])) 
    # print("Upper bound:", len(adj_list[max(adj_list, key=lambda k: len(adj_list[k]))]))
    curr_m_clique = set()
    for a in range(len(arr) // 4): # O(v / 4)
        curr = greedy(complement.copy(), arr[a]) # O(v^2)
        curr_m_clique = max(curr_m_clique, curr, key=len)
    for c in curr_m_clique:
        for j in curr_m_clique:
            if c != j and j not in adj_list[c]:
                print("error", c, adj_list[c], j)
    print("Approximate max clique:", curr_m_clique)
    

if __name__ == "__main__":
    main()


