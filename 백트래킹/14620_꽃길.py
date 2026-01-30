import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 200*N*N+1
visited = [[False for _ in range(N)] for _ in range(N)]
def correct(si,sj):
    for di, dj in ((0,0),(-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = si+di, sj+dj
        if visited[ni][nj]:
            return False
    return True
            


def count_cost(si, sj):
    cost = 0
    for di, dj in ((0,0),(-1,0),(1,0),(0,-1),(0,1)):
        ni, nj = si+di, sj+dj
        cost += arr[ni][nj]
    return cost

def set_visited(si, sj, val):
    for di, dj in ((0,0),(-1,0),(1,0),(0,-1),(0,1)):
        visited[si+di][sj+dj] = val


def dfs(cnt, cost):
    global ans
    if cost > ans:
        return
    if cnt == 3: # 꽃 3개를 다 심을 수 있다면
        ans = min(ans, cost) # 현재 가격과 비교
        # print(ans)
        return

    for ci in range(1, N-1):
        for cj in range(1, N-1): # 씨앗을 심을 수 있는 장소 전체
            if not visited[ci][cj]:
                if correct(ci,cj): # 5칸 모두 비어있다면
                    set_visited(ci, cj, True)
                    dfs(cnt+1, cost+count_cost(ci,cj))
                    set_visited(ci,cj,False)



dfs(0, 0)
print(ans)