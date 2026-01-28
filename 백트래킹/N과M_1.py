import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline


N, M = map(int, input().split())
visited = [False] * (N+1)
result = []
def dfs():
    if len(result) == M: # 종료 조건
        print(*result)
        return
    
    for i in range(1, N+1):
        if not visited[i]: # 아직 쓰지 않은 숫자라면 
            visited[i] = True
            result.append(i)
            dfs()

            # 다시 제거
            result.pop()
            visited[i] = False
dfs()