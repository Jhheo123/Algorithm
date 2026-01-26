import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

from collections import deque
def bfs(ci, cj):
    q = deque([(ci,cj)])
    visited[ci][cj] = 1
    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<h and 0<=nj<w and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                q.append((ni,nj))
    

while(True):
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    # print(arr)
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i,j)
                cnt+=1
    print(cnt)
            