import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline


N, M = map(int, input().split())


result = []

def dfs(n):
    if len(result) == M:
        print(*result)
        return
    for i in range(n, N+1):
        if i not in result:
            result.append(i)
            dfs(i+1)
            result.pop()
            
n=1         
dfs(n)
    