import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
door = []
mirror = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '#':
            door.append((i,j))
        elif arr[i][j] == '!':
            mirror.append((i,j))

# print(door)
# print(mirror)
si, sj = door[0]
ei, ej = door[1]
visited = [[-1 for _ in range(N)] for _ in range(N)]
from collections import deque
def bfs(si, sj):
    global visited
    q = deque([(si,sj)])
    visited[si][sj] = 0
    while q:
        ci, cj  = q.popleft()
        if ci == ei and cj == ej:
            break
        
        for di, dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and visited[ni][nj] == -1 and arr[ni][nj] != '*':
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni,nj))
bfs(si, sj)
from collections import defaultdict
num_dict = defaultdict(list)
for i in range(N):
    for j in range(N):
        if visited[i][j] != -1 and arr[i][j] == '!':
            num = visited[i][j]
            num_dict[num].append((i,j))
print(len(num_dict.keys()))



            
