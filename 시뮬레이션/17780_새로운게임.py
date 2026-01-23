import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline

from collections import defaultdict # k 담는 용도

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

stack = defaultdict(list)
for i in range(1, K+1):
    ci, cj, dr = map(int, input().split())
    stack[i].append([ci-1, cj-1, dr-1])
# print(stack)

# 방향 (오, 왼, 위, 아래)
dx = [0,0,-1,1]
dy = [1,-1,0,0]

# stack 쌓을 배열 -> 개수 세기
arr_lst = [[[] for _ in range(N)] for _ in range(N)]
finish = False
# 초기 배치
for k in range(1, K+1):
    ci, cj, dr = stack[k][0]
    arr_lst[ci][cj].append(k)

# 방향 반대로 바꾸기
def reverse_dir(dr: int) -> int:
    if dr%2 == 0:
        return dr+1
    else:
        return dr-1
# 최대 1000 턴 4개 이상 쌓이면 출력, 아니면 -1    
for turn in range(1, 1001):
    for k in range(1, K+1):
        ci, cj, dr = stack[k][0]
        # 현재 위치가 배열의 마지막 순번이 맞는지? 

        # 맞다면
        cell = arr_lst[ci][cj]
        idx = cell.index(k)
        
        # 아래 바탁이 아니면 이동 안하기
        if idx !=0 : continue

        ni, nj = ci+dx[dr], cj+dy[dr]
        # 1) 다음 칸이 범위 밖이거나 파란색이면 반전 후 다시 시도
        if not (0<=ni<N and 0<=nj<N) or (arr[ni][nj] == 2): 
            dr = reverse_dir(dr)
            stack[k][0][2] = dr # 방향 변경

            # 반전된 방향으로 다시 한칸 계싼 
            ni, nj = ci + dx[dr], cj+dy[dr]
            # 다시 가려는 칸도 범위 밖 or 파란색 이동 안하고 종료
            if not (0<=ni<N and 0<=nj<N) or (arr[ni][nj] == 2): 
                continue
        # (ni,nj)는 이동 가능한 칸(흰/빨)
        # k가 맨 아래이므로 idx = 0부터 통째로 이동
        moving = arr_lst[ci][cj][idx:]
        arr_lst[ci][cj] = arr_lst[ci][cj][:idx] # 비워두기

        # 빨간색이면 이동 순서 뒤집기
        if arr[ni][nj] == 1:
            moving.reverse()
        arr_lst[ni][nj].extend(moving)

        for moved_k in moving:
            stack[moved_k][0][0] = ni
            stack[moved_k][0][1] = nj
        
        if len(arr_lst[ni][nj]) >= 4:
            print(turn)
            finish = True
            break
    if finish:
        break
if not finish:
    print(-1)