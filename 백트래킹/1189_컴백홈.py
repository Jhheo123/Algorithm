import sys
sys.stdin=open("./input.txt","r") # 로컬 테스트용
input = sys.stdin.readline

R, C, K = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]


sr, sc = R-1, 0
# print(sr, sc)
er, ec = 0, C-1
# print(er, ec)

visited =[[False for _ in range(C)] for _ in range(R)]
cnt = 0
visited[sr][sc] = True
def dfs(ci, cj, dist):
    global cnt
    if ci == er and cj == ec and dist == K:
        cnt+=1
        return
    for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
        ni, nj = ci+di, cj+dj
        if 0<=ni<R and 0<=nj<C and visited[ni][nj] == False and arr[ni][nj] != 'T':
            visited[ni][nj] = True
            dfs(ni, nj, dist+1)
            visited[ni][nj] = False
dfs(sr, sc, 1)
print(cnt)