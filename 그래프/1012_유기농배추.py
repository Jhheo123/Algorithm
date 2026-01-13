import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    q = deque([(i, j)])
    visited[i][j] = 1
    while q:
        ci, cj = q.popleft()
        for d in range(4):
            ni, nj = ci + dx[d], cj + dy[d]
            if 0 <= ni < n and 0 <= nj < m:
                if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni, nj))

T = int(input())
for _ in range(T):
    # m: 가로(열), n: 세로(행), k: 배추 개수
    m, n, k = map(int, input().split())

    arr = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        # (x,y) = (열,행) 이므로 arr[행][열]
        arr[y][x] = 1

    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j)
                cnt += 1

    print(cnt)