import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

from collections import deque
# 정점의 개수, 간선의 개수
N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
# print(graph)

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
# print(graph)
def bfs(node):
    q = deque([node])
    visited[node]=1
    while q:
        current_node = q.popleft()
        for next_node in graph[current_node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                q.append(next_node)
    return 1


visited = [0]*(N+1)
cnt = 0
for node in range(1,N+1):
    if visited[node] == 0:
        cnt += bfs(node)
print(cnt)
