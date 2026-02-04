import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline

N, M, K = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(K)]

arr = [[0 for _ in range(M)] for _ in range(N)]
for ci, cj in lst:
    arr[ci-1][cj-1] = 1    


from collections import deque
def bfs(ci, cj):
    q = deque([(ci,cj)])
    visited[ci][cj] = True
    cnt = 1
    while q:
        ci, cj  = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj  = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and not visited[ni][nj] and arr[ni][nj] == 1:
                visited[ni][nj] = True
                cnt +=1
                q.append((ni,nj))
    return cnt
visited = [[False for _ in range(M)] for _ in range(N)]
result = []
for i in range(N):
    for j in range(M):
        if not visited[i][j] and arr[i][j] == 1:
            result.append(bfs(i,j))
print(max(result))