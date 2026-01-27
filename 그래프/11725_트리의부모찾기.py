import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

from collections import deque
N = int(input())
graph = [[] for _ in range(N+1)]

# print(graph)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph)

visited = [0]*(N+1)
def bfs(node):
    q = deque([node])
    visited[node] = 1
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if visited[next_node] == 0:
                visited[next_node] = node
                q.append(next_node)
    return visited

ans = bfs(1)
# print(ans)
for parent in ans[2:]:
    print(parent)

