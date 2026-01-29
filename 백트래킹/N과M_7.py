import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

visited = [False] * N
result = []

def dfs(n):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(N):
        result.append(lst[i])
        dfs(i+1)
        result.pop()
dfs(0)
