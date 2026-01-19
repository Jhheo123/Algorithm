import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

def check(a):
    for i in a:
        print(i) 

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
# check(arr)
# print("===========")
def spread():
    add = [[0]*C for _ in range(R)]
    for ci in range(R):
        for cj in range(C):
            if arr[ci][cj]>0: # 공기청정기가 아니고 미세먼지가 있을때
                amount = arr[ci][cj] // 5
                if amount == 0:
                    continue
                cnt = 0
                for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
                    ni, nj = ci+di, cj+dj
                    if 0<=ni<R and 0<=nj<C and arr[ni][nj] != -1:
                        cnt+=1
                        add[ni][nj] += amount
                add[ci][cj] = add[ci][cj]-(amount*cnt)
    
    for i in range(R):
        for j in range(C):
            if arr[i][j] != -1:
                arr[i][j] += add[i][j]

# 공기 청정기 위치 찾기
def search():
    lst = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == -1:
                lst.append((i,j))
    return lst

def up_clear(lst):
    ci, cj = lst[0]
    # 위 -> 아래 (왼쪽 벽)
    for i in range(ci-1, 0, -1):
        arr[i][0] = arr[i-1][0]
    # 왼 ->  오른 (윗줄)
    for j in range(C-1):
        arr[0][j] = arr[0][j+1]
    
    # 아래 -> 위 (오른쪽 벽)
    for i in range(ci):
        arr[i][C-1] = arr[i+1][C-1]
    
    # 오른 -> 왼 (청정기행)
    for j in range(C-1, 1, -1):
        arr[ci][j] = arr[ci][j-1]
    arr[ci][1] = 0



def down_clear(lst):
    ci, cj = lst[1]
    # 아래 -> 위 (왼쪽 벽)
    for i in range(ci+1, R-1):
        arr[i][0] = arr[i+1][0]
    # 왼 -> 오른 (아래줄)
    for j in range(C-1):
        arr[R-1][j] = arr[R-1][j+1]
    # 위 -> 아래 (오른쪽 벽)
    for i in range(R-1, ci, -1):
        arr[i][C-1] = arr[i-1][C-1]
    # 오른 -> 왼 (청정기 행)
    for j in range(C-1, 1, -1):
        arr[ci][j] = arr[ci][j-1]
    arr[ci][1] = 0
for _ in range(T):
    # 1. 미세먼지 확산
    spread()
    # check(arr)
    # 2. 공기 청정기 작동
    lst = search()
    # print(lst)
    # 위 공기 청정기 반시계 순환
    up_clear(lst)
    # 아래 공기 청정기 시계 순환
    down_clear(lst)
    # print("===========")
    # check(arr)
ans = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] != -1:
            ans += arr[i][j]
print(ans)