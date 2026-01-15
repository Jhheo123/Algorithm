import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline
from collections import deque

x, y = map(int, input().split())
arr = []
for _ in range(x):
    arr.append(list(input().rstrip()))

visited = [[0]*y for _ in range(x)]
def check():
    print("==============")
    for i in visited:
        print(i)
# - -> 좌우 / | -> 상하

def bfs(i,j):
    q = deque([(i,j)])
    visited[i][j] = 1
    if arr[i][j] == "-":
        dr = 1
    elif arr[i][j] == "|":
        dr = 2
    while q:
        ci, cj = q.popleft()
        if dr == 1:
            for di, dj in ((0,-1), (0,1)):
                ni, nj = ci+di, cj+dj
                if 0<=ni<x and 0<=nj<y and visited[ni][nj]==0 and arr[ni][nj] == "-":
                    visited[ni][nj] =1
                    q.append((ni,nj))
        else:
            for di, dj in ((1,0),(-1,0)):
                ni, nj = ci+di, cj+dj
                if 0<=ni<x and 0<=nj<y and visited[ni][nj]==0 and arr[ni][nj]=="|":
                    visited[ni][nj] =1
                    q.append((ni,nj))

    # check()
    return 1


cnt = 0
for i in range(x):
    for j in range(y):
        if visited[i][j] == 0:
            bfs(i,j)
            cnt +=1
print(cnt)