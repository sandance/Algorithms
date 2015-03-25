
import py.test 


def find(C, u):
    if C[u] != u:
        C[u] = find(C, C[u])                    # Path compression
    return C[u]

def union(C, R, u, v):
    u, v = find(C, u), find(C, v)
    if R[u] > R[v]:                             # Union by rank
        C[v] = u
    else:
        C[u] = v
    if R[u] == R[v]:                            # A tie: Move v up a level
        R[v] += 1

def kruskal(G):
    E = [(G[u][v],u,v) for u in G for v in G[u]]
    T = set()
    C, R = {u:u for u in G}, {u:0 for u in G}   # Comp. reps and ranks
    for _, u, v in sorted(E):
        if find(C, u) != find(C, v):
            T.add((u, v))
            union(C, R, u, v)
    return T


def test_kruskal():
    """
    >>> G = {
    ...   0: {1:1, 2:3, 3:4},
    ...   1: {2:5},
    ...   2: {3:2},
    ...   3: set()
    ... }
    >>> print list(kruskal(G))
    [(0, 1), (2, 3), (0, 2),(0,4)]
    """

if __name__=='__main__':
	test_kruskal()
