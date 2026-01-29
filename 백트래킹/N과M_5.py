import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
# print(lst)

visited = [False]*(N)
result = []
def dfs():
    if len(result) == M:
        print(*result)
        return
    
    for i in range(len(lst)):
        if not visited[i]:
            visited[i] = True
            result.append(lst[i])
            dfs()
            visited[i] = False
            result.pop()

dfs()