import sys
sys.stdin = open("./input.txt", "r") 
input = sys.stdin.readline

R, C, N = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]

# 1. 초기 폭탄 위치 저장
start_boom = []
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'O':
            start_boom.append((i,j))

def fill_boom(arr):
    for i in range(R):
        for j in range(C):
            arr[i][j] = 'O' 
    return arr

def boom(arr_copy, start_boom):
    for ci, cj in start_boom:
        arr_copy[ci][cj] = '.'
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<R and 0<=nj<C:
                arr_copy[ni][nj] = '.'
                
    next_boom = [] 
    for i in range(R):
        for j in range(C):
            if arr_copy[i][j] == 'O':
                next_boom.append((i,j))
    return arr_copy, next_boom

# 2. 시뮬레이션 (N > 1일 때만 수행)
if N > 1:
    cnt = 1
    while True:
        # 설치 단계 (2, 4, 6초...)
        arr = fill_boom(arr)
        cnt += 1
        if cnt == N: break
        
        # 폭발 단계 (3, 5, 7초...)
        arr, start_boom = boom(arr, start_boom)
        cnt += 1
        if cnt == N: break

# 3. 최종 출력 (N=1일 때도 여기로 와서 정상 출력됨)
for i in arr:
    print("".join(i))