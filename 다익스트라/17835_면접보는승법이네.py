import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()
    
visited1 = [False]*(N+1)
visited2 = [False]*(N+1)

def dfs(node):
    visited1[node] = True
    print(node, end=" ")
    for next_node in graph[node]:
        if not visited1[next_node]:
            dfs(next_node)

from collections import deque
def bfs(node):
    q = deque([node])
    visited2[node] = True
    while q:
        node = q.popleft()
        print(node, end=" ")
        for next_node in graph[node]:
            if not visited2[next_node]:
                visited2[next_node] = True
                q.append(next_node)
dfs(V)
print()
bfs(V)