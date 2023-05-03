"""
Approximation for max clique

Author: Ross Amspoker

Problem type: Greedy

source: 
https://courses.engr.illinois.edu/cs598csc/sp2011/lectures/lecture_7.pdf


"""


def greedy(graph, val):
    s = set()
    s.add(str(val))
    for u in graph[val]:
        del graph[u]
    del graph[val]
    while graph:
        curr = min(graph, key=lambda k: len(graph[k]))
        for u in graph[curr]: 
            if u in graph: 
                del graph[u]
        del graph[curr]
        s.add(str(curr))
    return s


def main():
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
    complement = {i:{j for j in verts if j not in adj_list[i] and j != i} for i in verts}
    arr = sorted(complement, key=lambda k: len(complement[k]))
    curr_m_clique = set()
    for a in range(len(arr) // 4):
        curr = greedy(complement.copy(), arr[a])
        curr_m_clique = max(curr_m_clique, curr, key=len)
    print(" ".join(curr_m_clique))
    

if __name__ == "__main__":
    main()
