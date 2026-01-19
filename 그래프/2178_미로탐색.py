import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline
from collections import deque


n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]
# for i in arr:
#     print(i)

visited = [[0]*m for _ in range(n)]
def bfs(ci, cj):
    q = deque([(ci, cj)])
    visited[ci][cj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<n and 0<=nj<m and visited[ni][nj] == 0 and arr[ni][nj]!=0:
                visited[ni][nj] = visited[ci][cj]+1
                q.append((ni,nj))
    # for i in visited:
    #     print(i)
    return visited[n-1][m-1]


print(bfs(0,0))