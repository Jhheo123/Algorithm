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
    for i in range(n, N+1):
        result.append(i)
        dfs(i)
        result.pop()
dfs(1)

