import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [False]*(N+1)
result = []

def dfs(n):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(1, N+1):
        # if not visited[i]:
        visited[i] = True
        result.append(i)
        dfs(i)
        visited[i] = False
        result.pop()

dfs(1)