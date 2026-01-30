import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(set(map(int, input().split()))))
# visited = [False]*N
result = []

def dfs():
    if len(result) == M:
        print(*result)
        return
    
    # prev = 0
    for i in range(len(lst)):
        # if not prev != lst[i]:
            # visited[i] = True
        result.append(lst[i])
        # prev = lst[i]
        dfs()
        # visited[i] = False
        result.pop()
dfs()