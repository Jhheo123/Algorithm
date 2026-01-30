import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))


visited = [False]*N
result = []

def dfs(n):
    if len(result) == M:
        print(*result)
        return
    
    prev = 0
    for i in range(n, N):
        if not visited[i] and prev != lst[i]:
            visited[i] = True
            result.append(lst[i])
            prev = lst[i]
            dfs(i+1)
            visited[i] = False
            result.pop()
dfs(0)