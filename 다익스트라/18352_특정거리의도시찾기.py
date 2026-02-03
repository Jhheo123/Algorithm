import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# print(graph)

# 최단 거리 K, 시작 위치 X
from collections import deque

def bfs(X):
    q = deque([(X, 0)])
    ans = []
    visited = [False]*(N+1)
    visited[X] = True
    while q:
        node, cnt = q.popleft()
        if cnt == K:
            ans.append(node)
        for next_node in graph[node]:
            if not visited[next_node]:
                q.append((next_node, cnt+1))
                visited[next_node] = True
    return ans
ans = bfs(X)
if len(ans) == 0:
    print(-1)
else:
    ans.sort()
    for i in ans:
        print(i)