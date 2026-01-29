import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))

result = []
visited = [False]*N
def dfs(n):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(n, N):
        # if not visited[i]:
        # visited[i] = True
        result.append(lst[i])
        dfs(i)
        # visited[i] = True
        result.pop()
dfs(0)
    