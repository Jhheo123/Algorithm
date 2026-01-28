import sys
sys.stdin=open("./input.txt","r")
input = sys.stdin.readline


import copy
# 0,1,2,3,4,5,6,7,8
dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, -1, -1, -1, 0, 1, 1, 1]

arr = [[[] for _ in range(4)] for _ in range(4)]
for i in range(4):
    line = list(map(int, input().split()))
    for j in range(4):
        # [번호, 방향]
        arr[i][j] = [line[j*2], line[j*2+1]]

# 물고기 위치 저장
fish_pos = [[] for _ in range(17)]

for i in range(4):
    for j in range(4):
        num = arr[i][j][0]
        # print(num)
        fish_pos[num] = [i,j]
# print(fish_pos)

def move_fish(current_arr, current_fish_pos, shark_r, shark_c):
    for i in range(1, 17):
        if not current_fish_pos[i]: continue # 먹힌 물고기 패쓰

        ci, cj = current_fish_pos[i]
        # print(ci, cj)
        
        num, dr = current_arr[ci][cj][0], current_arr[ci][cj][1]
        for _ in range(8):
            ni, nj = ci + dx[dr], cj + dy[dr]
            # 격차 안이고 상어가 없는 칸이라면 이동 가능
            if 0<=ni<4 and 0<=nj<4 and (ni, nj)!= (shark_r, shark_c):
                # 상대방 물고기 번호 확인 (빈칸이면 0)
                target_num = current_arr[ni][nj][0]

                # fish_pos 업데이트
                current_fish_pos[i] = [ni,nj]
                if target_num != 0: # 빈칸이 아니라면 상대 위치도 변경
                    current_fish_pos[target_num] = [ci,cj]
                
                # arr 업데이트
                current_arr[ci][cj][1] = dr # 바뀐 방향 반영
                current_arr[ci][cj], current_arr[ni][nj] = current_arr[ni][nj], current_arr[ci][cj]
                break
            # 방향 돌리기
            dr = dr % 8 + 1

max_score = 0

def solve(arr, fish_pos, shark_r, shark_c, total):
    global max_score
    # 백트래킹을 위해 현재 상태 복사
    arr = copy.deepcopy(arr)
    fish_pos = copy.deepcopy(fish_pos)

    # 상어가 물고기 먹음
    fish_num, shark_dr = arr[shark_r][shark_c]
    total += fish_num
    max_score = max(max_score, total)

    # 먹힌 물고기 처리
    arr[shark_r][shark_c][0] = 0
    fish_pos[fish_num] = []

    # 물고기 이동 
    move_fish(arr, fish_pos, shark_r, shark_c)

    # 상어 이동 (물고기 있는 칸으로)
    for i in range(1, 4):
        ni, nj = shark_r + dx[shark_dr]*i, shark_c+dy[shark_dr]*i
        if 0<= ni<4 and 0<=nj<4 and arr[ni][nj][0] > 0:
            solve(arr, fish_pos, ni,nj,total)

solve(arr, fish_pos, 0, 0, 0)
print(max_score)