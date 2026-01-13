import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

from collections import deque

# 컴퓨터 수 = 노드 수
n = int(input())
# 에지
m = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0]*(n+1) # 방문 여부
def bfs(v):
    q = deque([v])
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i]==0: # 미방문
                visited[i] = 1
                q.append(i)
    return visited
ans = bfs(1)
# print(ans)
print(sum(ans)-1)



