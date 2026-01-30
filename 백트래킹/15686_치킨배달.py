import sys
sys.stdin=open("./input.txt","r") # 로컬 테스트용
input = sys.stdin.readline

# N: 지도의 크기, M: 살릴 치킨집의 최대 개수
N, M = map(int, input().split())

# 지도 정보 입력 (0: 빈칸, 1: 집, 2: 치킨집)
arr = [list(map(int, input().split())) for _ in range(N)]

ch_dir = [] # 모든 치킨집의 좌표를 저장할 리스트
house = []  # 모든 집의 좌표를 저장할 리스트

# 전체 지도를 돌며 집과 치킨집의 위치(좌표)를 미리 파악
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            ch_dir.append((i, j))
        elif arr[i][j] == 1:
            house.append((i, j))

# 선택된 치킨집 리스트(select)를 바탕으로 도시의 치킨 거리를 계산하는 함수
def sum_func(select):
    total_dist = 0
    for hi, hj in house: # 각 집을 하나씩 확인
        min_dist = float('inf') # 해당 집에서 가장 가까운 치킨집까지의 거리
        for si, sj in select: # 선택된 치킨집들을 순회
            dist = abs(hi - si) + abs(hj - sj) # 맨해튼 거리 계산
            if dist < min_dist:
                min_dist = dist
        total_dist += min_dist # 각 집의 최소 거리를 도시 전체 거리에 합산
    return total_dist

ans = float('inf') # 최소값을 찾기 위해 아주 큰 값으로 초기화

def dfs(idx, select):
    global ans
    
    # [종료 조건 1] M개의 치킨집을 모두 골랐을 때
    if len(select) == M:
        ans = min(ans, sum_func(select)) # 현재 조합의 치킨 거리를 구해 최소값 갱신
        return
    
    # [종료 조건 2] 모든 치킨집을 다 훑었을 때 (더 이상 고를 게 없을 때)
    if idx == len(ch_dir):
        return
    
    # --- 갈림길 1: 현재 치킨집(ch_dir[idx])을 고르는 경우 ---
    select.append(ch_dir[idx])  # 일단 장바구니에 담기
    dfs(idx + 1, select)        # 담은 상태로 다음 단계 진행
    
    # --- 갈림길 2: 현재 치킨집(ch_dir[idx])을 고르지 않는 경우 ---
    select.pop()                # 방금 담았던 걸 다시 빼기 (원상복구)
    dfs(idx + 1, select)        # 안 담은 상태로 다음 단계 진행 (건너뛰기)

# 인덱스 0번 치킨집부터 시작, 빈 리스트 전달
dfs(0, [])
print(ans)