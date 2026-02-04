import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline

N = int(input())
lst = [0] + [int(input()) for _ in range(N)]
result = [] 

## 사이클이 있는지 확인하는 문제

def dfs(v, start):
    visited[v] = True
    next_node = lst[v]

    if not visited[next_node]:
        dfs(next_node, start)
    elif visited[next_node] and next_node == start:
        # 이미 방문 했는데 그게 시작점 이라면 
        result.append(start)

for i in range(1, N+1):
    visited = [False] * (N+1)
    dfs(i, i)

print(len(result))
for x in sorted(result):
    print(x)

