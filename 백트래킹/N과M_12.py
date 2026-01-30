import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

N, M = map(int, input().split())
lst = sorted(list(set(map(int, input().split()))))

result = []
def dfs(n):
    if len(result) == M:
        print(*result)
        return
    
    for i in range(n, len(lst)):
        result.append(lst[i])
        dfs(i)
        result.pop()

dfs(0)
